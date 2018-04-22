import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fastq', help = "fastq file to be processed")
parser.add_argument('-V', '--VCF', help = "If reference.fasta passed, creates a VCF file. Otherwise, fasta will be generated from fastq file.")

args = parser.parse_args()
reference_file = ""
if args.VCF :
    reference_file = args.vcf

# wkdirectory = "C:/Users\Shannon\Desktop\Programming_Assignment_A\TestFiles1" # add working directory here
# reference_file = "reference.fna" # add reference sequence here
fastq_file = args.fastq  # add fastq file here
# fasta_file = "output.fa" # specify output fasta file name here
# vcf_file = "outputvcf.vcf" # specify output VCF file name here

# opens reference file and extracts line containing sequence and inserts it into a list, 'ref'
with open(reference_file, 'r') as r:
    r = r.readlines()
    ref = r[1]

# opens fastq file
with open(fastq_file, 'r') as f:
    fastq_list = f.readlines()

# function which breaks list items into chunks (list of lists) of a chosen size
def chunks(l, n):
    """Yield successive n-sized chunks from l"""
    newlist = []
    for i in range(0, len(l), n) :
        newlist.append(l[i:i + n])
    return newlist

""" VCF file compiler """

if args.VCF :
    # perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 4 lines
    new = chunks(fastq_list, 4)

    # creates vcf file with headers
    headers = ["#CHROM\t", "POS\t", "ID\t", "REF\t", "ALT\t", "QUAL\t", "FILTER\t", "INFO\t"]
    vcffile = open(vcf_file, 'w')
    for item in headers:
        vcffile.write(item)

    # with open("filename.txt", "wb") as outfile:
    uniqueList = []
    for i in range(0, len(new)):
        a = new[i][1]
        for j in range(0, len(a)):
            uniqueStr = "%s,%s" % (str(j), str(a[j]))
            if a[j] == ref[j]:
                pass
                # print("true" + (a[j]) + ref[j])
            elif uniqueStr not in uniqueList:
                POS = str(j)
                ID = str(new[i][0])
                ID = ID.rstrip()  # removes '/n' from ID string
                REF = a[j]
                ALT = ref[j]
                vcffile.write("\n1\t%s\t%s\t%s\t%s\t" % (POS, ID, REF, ALT))
                uniqueList.append(uniqueStr)
               # vcffile.write("1\t")
                #vcffile.write("%s\t" % POS)
                #vcffile.write("%s\t" % ID)
                #vcffile.write("%s\t" % REF)
                #vcffile.write("%s\t" % ALT)
                # print("false" + a[j] + ref[j])
    vcffile.close()
    print(uniqueList)

# need to stop variants being added to vcf file if they already exist in vcf file

## \t = tab (use for making vcf file)
## writing things to file : outfile = open('filename, 'w')

## in vcf file, ID header will be there but will be '.'

""" Convert Fastq to Fasta file """
else :
    # perform 'chunks' on 'fastq_list' to break the fastq file into chunks of 2 lines, and output to a list 'fqn'
    fqn = chunks(fastq_list, 2)

    # delete every second chunk of two in fastq_list to remove read quality info
    c = 0
    for i in range(1, len(fqn), 2) :
        # for each 'chunk' in 'fqn', delete
        del (fqn[i - c]) # 'c' variable adjusts for list index changes that occur every loop
        c = c + 1

    # extract all items from lists wthin lists of 'fqn' and create list, 'fqn2'
    fqn2 = []
    for i in range(0, len(fqn)) :
        fqn2.append(fqn[i][0])
        fqn2.append(fqn[i][1])

    # write new fasta file
    fastafile = open(fasta_file, 'w')
    for item in fqn2:
        # for each item of fqn2, write new line in fasta file
        fastafile.write(item)
    fastafile.close()
