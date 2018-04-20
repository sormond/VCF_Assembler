wkdirectory = "/Users/sormond/Desktop"
reference_file = "reference.fna"
fastq_file = "test.fq"
fasta_file = "test.fa"
vcf_file = "name of output vcf file"

import os
os.chdir(wkdirectory)
with open(reference_file, 'r') as r:
    r = r.readlines()
    ref = r[1]

with open(fastq_file, 'r') as f:
    fastq_list = f.readlines()

# function which breaks list elements into chunks (list of lists) of a chosen size
def chunks(l, n):
    """Yield successive n-sized chunks from l"""
    newlist = []
    for i in range(0, len(l), n) :
        newlist.append(l[i:i + n])
    return newlist

""" Convert Fastq to Fasta file """

# perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 2 lines, and output to a list 'fqn'
fqn = chunks(fastq_list, 2)  

# delete every second chunk of two in fastq_list to remove read quality info
c = 0
for i in range(1, len(fqn), 2) :
    # for each 'chunk' in 'fqn', delete 
    del (fqn[i - c]) # 'c' variable adjusts for list index changes that occur every loop
    c = c + 1

print(len(fqn))  # check, len should = 10

fqn2 = []
for i in range(0, len(fqn)) :
    fqn2.append(fqn[i][0])
    fqn2.append(fqn[i][1])

print(fqn2)
print(len(fqn2))

fastafile = open(fasta_file, 'w')
# fastafile.write(str(fqn))
for item in fqn2:
  fastafile.write(item)
fastafile.close()
# must close connection to file:    outfile.close()

""" VCF file compiler """

# perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 4 lines
new = chunks(fastq_list, 4)

# add code for headers for outfile here

# with open("filename.txt", "w") as outfile:
for i in range(0, 1) :
    a = new[i][1]
    for j in range(0, len(a)) :
        if a[j] == ref[j] :
            print("true" + (a[j]) + ref[j])
        else :
            print("false" + a[j] + ref[j])
            # outfile.write(

## \t = tab (use for making vcf file)
## writing things to file : outfile = open('filename, 'w')

## in vcf file, ID header will be there but will be '.'