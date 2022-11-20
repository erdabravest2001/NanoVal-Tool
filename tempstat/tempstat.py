from tempstat.idtapi import IDTOligoAnalyzer
import pandas as pd
import numpy as np
from pathlib import Path
import json

class TempStat(IDTOligoAnalyzer):
    def __init__(self, Na_conc:int = 50, Mg_conc:int = 0, dNTP_conc:int = 0, oligo_conc:float = 0.25):
        super(TempStat, self).__init__()
        
        if (Na_conc == 50) & (Mg_conc == 0) & (dNTP_conc == 0) & (oligo_conc == 0):
            print("PROCESS: Initialized TempStat object with default settings.")
        else:
            print(f"PROCESS: Initialized tempstat object with settings: \n\t[Na]: {Na_conc}\n\t[Mg]: {Mg_conc}\n\t[dNTP]: {dNTP_conc}\n\t[oligo]: {oligo_conc}")

        self.Na = Na_conc
        self.Mg = Mg_conc
        self.dNTP = dNTP_conc
        self.oligo = oligo_conc

        self.meltemps = []

        self.meltemp_cache_path = Path(__file__).parent / "Data/melting_temps_cache.json"

    def cache_analysis_response(self, response_text:dict) -> None:
        cache_key = f"{self.Na}{self.Mg}{self.dNTP}{self.oligo}{str(response_text['Sequence']).replace(' ', '')}"
        with open(self.meltemp_cache_path, 'r') as cache_f:
            cache_f = cache_f.read()
            if cache_f == "":
                cache = {}
            else:
                cache = json.loads(cache_f)
        cache[cache_key] = response_text
        
        with open(self.meltemp_cache_path, 'w') as cache_w:
            cache_w.write(json.dumps(cache, indent = 4))

        return None

    def search_mt_in_cache(self, cache_key:str) -> bool:
        with open(self.meltemp_cache_path, 'r') as cache_f:
            cache_f = cache_f.read()
            if cache_f == "":
                return False
            else:
                cache = json.loads(cache_f)
        try:
            melting_temperature = cache[cache_key]['MeltTemp']
            return melting_temperature

        except KeyError:
            return False

    def get_melt_temp(self, oligo_sequence:str) -> float:
        '''
        Settings/parameters such as [Na+] and [dNTP] should be set upon initialization of the TempStat object. If custom settings are desired following initialization,
        the object attribute should be reassigned before running this function.
        '''
        cache_key = f"{self.Na}{self.Mg}{self.dNTP}{self.oligo}{oligo_sequence}"
        cache_search = self.search_mt_in_cache(cache_key)
        if cache_search == False:
            oligo_analysis_result = self.post_analyzer_request(oligo_sequence, self.Na, self.Mg, self.oligo, self.dNTP)
            self.cache_analysis_response(oligo_analysis_result)
            melt_temp = oligo_analysis_result['MeltTemp']
        else:
            melt_temp = cache_search

        return melt_temp
    
    def seq_temp_analyses(self, seqtable:pd.DataFrame, save_hist:bool = True) -> pd.DataFrame:
        sequences = seqtable['Sequence']
        melting_temps = []
        for sequence in sequences:
            melttemp = self.get_melt_temp(sequence)
            melting_temps.append(melttemp)
        seqtable['MeltTemps'] = melting_temps
        seq_ax = seqtable['MeltTemps'].plot.hist(bins = np.arange(min(melting_temps), max(melting_temps)+1, 1))
        seq_ax.set_xlabel("Melting Temperature (C)")
        seq_ax.set_title("Staple Melting Temperatures in 1C Bins")
        if save_hist:
            seq_ax.figure.savefig(r"C:\Users\fumi7\Desktop\test_fig.png", dpi = 300)

        return seqtable