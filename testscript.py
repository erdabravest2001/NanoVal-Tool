from unittest import result
from DONA.Analyzer.KineticTrapIdentifier import KineticTrapDefuser
from DONA.Utils.Messenger import SemanticTranslator
import numpy as np
from pathlib import Path
import json

current = Path(__file__)

path2 = current.parent / 'DONA/Tests' / 'Test_Kt_n_Sandwich.json'
path3 = current.parent / 'DONA/Tests/50Scaff2Break.json'
path = "/Users/fumiy/Desktop/Research/BIOMOD_root/Designs/Nanohinge/V4_V5/V4-p8064-RTO-3_No-Lock.json"
'''
kint = KineticTrapDefuser(path2)
trans = SemanticTranslator()

detected = kint.kinetic_trap_scan()
print(detected)
translated = SemanticTranslator.translate_kinetic_trap(detected)
for translate in translated:
    print(translate)
'''
'''
from DONA.Analyzer.Parser import JSONParser
parser = JSONParser(path2)

parsed_staple_helix = parser.parse_all_helices()
print(json.dumps(parser.links, indent = 4))
print(len(parser.links))
'''
'''
from DONA.Analyzer.SequenceAnalyzer import SandwichEater
seat = SandwichEater(path2)
seat.assemble_all_staples()
all_detected_sandwich_strands = seat.sandwich_staples_scan()
translated_lst = SemanticTranslator.translate_detected_sandwiches(all_detected_sandwich_strands)
for item in translated_lst:
    print(item)
'''

from DONA.Analyzer.MainAnalyzer import AnalyzerMain
analyzer = AnalyzerMain(path)
results = analyzer.analyze()
analyzer.visualizer.visualize_kinetic_traps(results[0])
analyzer.visualizer.visualize_sandwich_strands(results[1])
