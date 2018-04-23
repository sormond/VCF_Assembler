#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('fastq', help = "fastq file to be processed")
parser.add_argument('-V', '--VCF', help = "If reference.fasta passed, creates a VCF file. Otherwise, fasta will be generated from fastq file.")

args = parser.parse_args()
reference_file = "" # defines reference_file
if args.VCF : # if a VCF file given, loads file into 'reference_file'
    reference_file = args.VCF

fastq_file = args.fastq
fasta_file = "output.fa"
vcf_file = "outputvcf.vcf"

# opens fastq file
with open(fastq_file, 'r') as f:
    fastq_list = f.readlines()

# function which breaks list items into chunks (list of lists) of a chosen size (modified from code retrieved from "https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks")
def chunks(l, n):
    # Yield successive n-sized chunks from l
    newlist = []
    for i in range(0, len(l), n) :
        newlist.append(l[i:i + n])
    return newlist


    """ VCF file compiler """
    # this script will run if the -V flag is given in the command line, in addition to an input fastq and a reference.fasta file

if args.VCF :
    #  extracts line containing sequence from 'reference_file' and inserts it into a list, 'ref'
    with open(reference_file, 'r') as r:
        r = r.readlines()
        ref = r[1]

    # perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 4 lines
    new = chunks(fastq_list, 4)

    # creates vcf file with headers
    headers = ["#CHROM\t", "POS\t", "ID\t", "REF\t", "ALT\t", "QUAL\t", "FILTER\t", "INFO\t"]
    vcffile = open(vcf_file, 'w')
    for item in headers:
        vcffile.write(item)

    # with open("filename.txt", "wb") as outfile:
    uniqueList = [] # creates an empty list in which unique variants will be appended
    for i in range(0, len(new)):
        a = new[i][1] # puts sequence (second list item for each list in new) into variable 'a'
        for j in range(0, len(a)):
            uniqueStr = "%s,%s" % (str(j), str(a[j])) #creates a string containing the sequence position and read base
            if a[j] == ref[j]: # pass if sequence at position 'j' is identical
                pass
            elif uniqueStr not in uniqueList: # if sequence at position 'j' is non-identical, and if 'uniqueStr' does not exist in 'uniqueList', add a new line to the VCF file
                POS = str(j+1) # +1 to position number due to python 0-based indexing
                REF = a[j]
                ALT = ref[j]
                vcffile.write("\n1\t%s\t.\t%s\t%s\t.\t.\t.\t" % (POS, REF, ALT))
                uniqueList.append(uniqueStr) # adds uniqueStr to uniqueList if string is unique
    vcffile.close()

    
    """ Convert Fastq to Fasta file """
    # note: script that can carry out this same conversion exists elsewhere, such as on Biopython
    # This script will be carried out if the -V flag is not used in command line

else :
    # perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 2 lines, and output to a list 'fqn'
    fqn = chunks(fastq_list, 2)

    # delete every second chunk of two in fastq_list to remove read quality info
    c = 0
    for i in range(1, len(fqn), 2) :
        # delete every second chunk of the list 'fqn' (every second chunk contains read quality information)
        del (fqn[i - c]) # 'c' variable adjusts for list index changes that occur every loop due to deletion of a chunk
        c = c + 1

    # extract all items from lists wthin lists of 'fqn' and create list, 'fqn2'
    fqn2 = []
    for i in range(0, len(fqn)) :
        fqn2.append(fqn[i][0])
        fqn2.append(fqn[i][1])

    # removes beginning '@' character of read ID and prepends '>' to convert to proper fasta file format
    for i in range(0, len(fqn2), 2):
        fqn2[i] = fqn2[i][1:]
        fqn2[i] = ">" + fqn2[i]

    # write new fasta file
    fastafile = open(fasta_file, 'w')
    for item in fqn2:
        # for each item of fqn2, write new line in fasta file
        fastafile.write(item)
    fastafile.close()
