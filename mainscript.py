import sys 
import tkinter as tk
from tkinter import filedialog as fd
from pathlib import Path
import time

from nanoval.analyzer import StrandAnalyzer
from tempstat.tempstat import TempStat

def mainscript_fx() -> None:
    if len(sys.argv) > 1:
        design_filepath = Path(sys.argv[1])
        analyzer = StrandAnalyzer(design_filepath)
    else:
        root = tk.Tk(); root.withdraw()
        design_filepath = Path(fd.askopenfilename(title = "Select caDNAno design file (.json)"))
        analyzer = StrandAnalyzer(design_filepath)
    start_stamp = time.time()
    # ----- Visualize staple connectivity vulnerabilities ----- #
    analyzer.visualize_vulnerabilities('all')
    analyzer.summary()
    end_stamp = time.time()
    print(f"Analysis completed in {end_stamp - start_stamp} seconds.")
    # ----- Melting Temperature Statistics ----- # 
    # Lab settings: 
    NaConc = 50
    MgConc = 0
    dNTPConc = 0
    oligoConc = 0.25
    tempstat = TempStat(NaConc, MgConc, dNTPConc, oligoConc)
    tempstat.seq_temp_analyses(analyzer.seqtable, save_hist=True)

if __name__ == "__main__":
    mainscript_fx()