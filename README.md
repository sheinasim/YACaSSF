# YACaSSF: Yet Another Contig and Scaffold Stat Finder 
Report number of assembly pieces (contigs or scaffolds) and length of piece to make up a genome percentage of your choosing.

This script is designed to be run on a genome assembly in .fasta format 

Dependencies:

* Python3 
* Biopython
* Python pandas package

> export PATH=$PATH:[PATH TO YACaSSF]  

### Usage
  
> python nlStats.py \\
	\<genome percentage as an integer (50 for N50, 95 for N95)\> \\
	\<assembly.fasta\> \\
	[Optional: --noheader (stdout has no header, good for running in for loop with multiple assemblies) default: header] 

(pipe to `column -t` for more uniform looking tab separated output)

If no arguments are provided, the script will return help message.

## Outputs

* Number of pieces and length of piece required for a percentage of your assembly size of your choosing as stdout 

### Citation

If this script is useful to you, please cite the following in your publication:

```
@software{YACaSSF,
  author = {Sim, Sheina B.},
  title = {YACaSSF},
  url = {https://github.com/sheinasim/YACaSSF}
}
```

Sheina B. Sim  
USDA-ARS  
US Pacific Basin Agricultural Research Service  
Hilo, Hawaii, 96720 USA  
sheina.sim@usda.gov  

This script is in the public domain in the United States per 17 U.S.C. § 105
