import os
os.chdir('C:/Users/Shannon/Desktop/')
with open('Programming_Assignment_A/TestFiles1/reference.fna', 'r') as r:
    r = r.readlines()
    ref = r[1]

with open('Programming_Assignment_A/TestFiles1/input.fq', 'r') as f:
    fastq_list = f.readlines()

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    newlist = []
    for i in range(0, len(l), n):
        newlist.append(l[i:i + n])
    return newlist


""" Convert Fastq to Fasta file """
fqn = chunks(fastq_list, 2)  # perform above function 'chunks' on 'fastq_list', which will

c = 0
for i in range(1, len(fqn), 2):
    del (fqn[i - c])
    c = c + 1

print(len(fqn))  # check

fastafile = open('fasta.fa', 'w')
fastafile.write(str(fqn))
fastafile.close()
# must close connection to file:    outfile.close()


""" VCF file compiler """

new = chunks(fastq_list, 4)  # perform above function 'chunks' on 'fastq_list', which will

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