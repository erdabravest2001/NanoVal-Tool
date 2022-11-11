# caDNAno Design Validation Tool

## Introduction
caDNAno is a very popular tool for computer-aided DNA origami design. This project aims to analyze caDNAno design files (.json), identifying potentially problematic staple strands such as 'kinetic traps', or 'sandwich strands', a term coined by Dr.Stephanie Lauback. The inclusion of such strands in the design are thought to affect parameters of the DNA origami structure formed in the lab such as stability and formation yield. This tool was developed for the DNA origami design pipeline during my time at UBC BIOMOD.

## Background 
DNA Origami nanostructures are formed typically using one long 'scaffold' DNA strand (3000 - 8000 bp) and hundreds of smaller 'staple' DNA strands (24 - 64 bp) which bind to specific regions of the scaffold strand, holding it in a programmable structure/conformation. 

An important concept in the formation of DNA origami structures are 'cross overs'. This is when a single DNA strand in a double-stranded DNA (dsDNA) double helix crosses over from one dsDNA helix to another, resulting in one DNA strand being a part of two or more double helices. 