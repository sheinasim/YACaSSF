#!/usr/bin/python

import argparse
import pandas as pd
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("genomePercentage", type=int, help="Percentage of genome you want reported, eg: 95 for N95/L95")
parser.add_argument("fasta", help=".fasta file you want the stats of.")
parser.add_argument("--noheader", help="do not display header (default: display header)", action="store_true")
args = parser.parse_args()


def findNL(fasta, n):
	df = pd.DataFrame(columns=('Sequence', 'Length'))
	for record in SeqIO.parse(fasta, "fasta"):
		df = df.append({'Sequence' : record.name, 'Length' : len(record.seq)}, ignore_index = True)
	df['Length'] = df['Length'].apply(pd.to_numeric)
	df_sorted = df.sort_values('Length', ascending=False).reset_index()
	df_sorted = df_sorted[['Sequence', 'Length']]
	df_sorted['Cumulative Length'] = df_sorted['Length'].cumsum()
	
	asm_size = sum(df_sorted['Length'])
	prop_asm_size = asm_size*(n/100)

	idx = (df_sorted['Cumulative Length'] > prop_asm_size).argmax()
	ctglength = df_sorted['Length'].loc[idx]

	if ctglength <= 1000000:
		length = ctglength/1000
		lengthstr = str(length) + " KB"
	elif ctglength > 1000000:
		length = ctglength/1000000
		lengthstr = str(length) + " MB"
	fastaname = args.fasta.split('/')[-1]

	if args.noheader:
		print(fastaname + "\t" + str(idx+1) + "\t" + lengthstr + "\t" + str(asm_size/1000000) + " MB")
	else:	
		print("##file" + "\t" + "N" + str(n) + "\t" + "L" + str(n) + "\t" + "Size (MB)" + "\n" + fastaname + "\t" + str(idx+1) + "\t" + lengthstr + "\t" + str(asm_size/1000000))

findNL(args.fasta, args.genomePercentage)
