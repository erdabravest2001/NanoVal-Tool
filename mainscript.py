import sys 
import tkinter as tk
from tkinter import filedialog as fd
from pathlib import Path
import time

from nanoval.analysis import Analyzer

def mainscript_fx():
    start_stamp = time.time()
    if len(sys.argv) > 1:
        design_filepath = Path(sys.argv[1])
        analyzer = Analyzer(design_filepath)
    else:
        root = tk.Tk(); root.withdraw()
        design_filepath = Path(fd.askopenfilename(title = "Select caDNAno design file (.json)"))
        analyzer = Analyzer(design_filepath)
    
    analyzer.construct_all_staples()
    analyzer.visualize_vulnerabilities('all')
    analyzer.summary()
    end_stamp = time.time()
    print(f"Analysis completed in {end_stamp - start_stamp} seconds.")

if __name__ == "__main__":
    mainscript_fx()