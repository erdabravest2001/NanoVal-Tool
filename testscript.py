from nanoval.analysis import Analyzer
import numpy as np
from pathlib import Path
import json

current = Path(__file__)

design_filepath = Path("")
path2 = current.parent / 'DONA/Tests' / 'Test_Kt_n_Sandwich.json'
path3 = current.parent / 'DONA/Tests/50Scaff2Break.json'


analyzer = Analyzer(design_filepath)
results = analyzer.construct_all_staples()

