wkdirectory = "/Users/sormond/Desktop"
reference_file = "reference.fna"
fastq_file = "input.fq"
fasta_file = "output.fa"
vcf_file = "outputvcf.vcf"

import os
os.chdir(wkdirectory)
with open(reference_file, 'r') as r:
    r = r.readlines()
    ref = r[1]

with open(fastq_file, 'r') as f:
    fastq_list = f.readlines()

# function which breaks list items into chunks (list of lists) of a chosen size
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

# extract all items from lists wthin lists of 'fqn' and create list, 'fqn2'
fqn2 = []
for i in range(0, len(fqn)) :
    fqn2.append(fqn[i][0])
    fqn2.append(fqn[i][1])

print(fqn2) # just a check
print(len(fqn2)) # just a check

# write new fasta file
fastafile = open(fasta_file, 'w')
for item in fqn2:
    # for each item of fqn2, write new line in fasta file
    fastafile.write(item)
fastafile.close()


""" VCF file compiler """

# perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 4 lines
new = chunks(fastq_list, 4)

# creates vcf file with headers
headers = ["#CHROM\t", "POS\t", "ID\t", "REF\t", "ALT\t", "QUAL\t", "FILTER\t", "INFO\t"]
vcffile = open(vcf_file, 'w')
for item in headers:
    vcffile.write(item)

# with open("filename.txt", "w") as outfile:
for i in range(0, len(new)) :
    a = new[i][1]
    for j in range(0, len(a)) :
        if a[j] == ref[j] :
            pass
            # print("true" + (a[j]) + ref[j])
        else :
            POS = str(j)
            ID = str(new[i][0])
            ID = ID.rstrip()  # removes '/n' from ID string
            REF = a[j]
            ALT = ref[j]
            vcffile.write("\n")
            vcffile.write("1\t")
            vcffile.write("%s\t" % POS)
            vcffile.write("%s\t" % ID)
            vcffile.write("%s\t" % REF)
            vcffile.write("%s\t" % ALT)
            # print("false" + a[j] + ref[j])
vcffile.close()

# need to stop variants being added to vcf file if they already exist in vcf file

## \t = tab (use for making vcf file)
## writing things to file : outfile = open('filename, 'w')

## in vcf file, ID header will be there but will be '.'