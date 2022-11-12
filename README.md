# caDNAno Design Validation Tool

## Prerequisites
This documentation assumes basic knowledge of caDNAno2, and DNA origami concepts including thermodynamics, structure, design etc.   
Users should be familiar with the caDNAno2 interface and the representations of staple/scaffold strands.

## Introduction
caDNAno is a very popular tool for computer-aided DNA origami design. This project aims to analyze caDNAno design files (.json), identifying potentially problematic staple strands such as 'kinetic traps', or 'sandwich strands', a term coined by Dr.Stephanie Lauback. The inclusion of such strands in the design are thought to affect parameters of the DNA origami structure formed in the lab such as stability and formation yield. This tool was developed for the DNA origami design pipeline during my time at UBC BIOMOD.

## Usage  
### Dependencies  
```
numpy
```  
### Workflow
After users have a design file exported from caDNAno2, users can analyze their designs for staple strands which may be potentially problematic to the formation of the structure <i>in vitro</i>. These strands are explained in the <a href = "#bg">Background</a> section below.   
Users should run the following command from the location where this program is downloaded. 

```
C:\Users\username\download_location> python mainscript.py path\to\design\file.json
username@macos download_location ~ % python3 mainscript.py path/to/design/file.json
username@ubuntu download_location ~ $ python3 mainscript.py path/to/design/file.json
```
Providing the path to the caDNAno design file when running the script from terminal is optional. If it is not provided, the script will display a prompt where users can browse through their filesystem to search for the design file to analyze.  
```
C:\Users\username\download_location> python mainscript.py
username@macos download_location ~ % python3 mainscript
username@ubuntu ~ $ python3 mainscript.py
```

Once the analysis is complete, users can reopen the design file on caDNAno2, and will see that the problematic strands are colored red, while the others are colored green. The script also outputs a text file <i>name_of_design_file_summary</i>.txt, with the date and time of the analysis, along with the coordinates fo the problematic strands provided in the format <b>"helix_number[longitudinal_index]"</b>. Sample analyses files and results are available in the Examples folder.

<div id = 'bg'>
<h2>Background</h2>
DNA Origami nanostructures are formed typically using one long 'scaffold' DNA strand (3000 - 8000 bp) and hundreds of smaller 'staple' DNA strands (24 - 64 bp) which bind to specific regions of the scaffold strand, holding it in a programmable structure/conformation. 
<br><br>
An important concept in the formation of DNA origami structures are 'cross overs'. This is when a single DNA strand in a double-stranded DNA (dsDNA) double helix crosses over from one dsDNA helix to another, resulting in one DNA strand being a part of two or more double helices. 
</div>