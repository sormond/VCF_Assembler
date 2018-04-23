# VCF_Assembler
A *programme* to modify VCF and FASTQ files

This programme converts a fastq file to a fasta file and creates VCF files.


## Dependencies
This programme requires Python 3


## File inputs and outputs

* Fastq file (required): The fastq input file must be in standard four-line-per-sequence format, with the second line containing the sequence.


* Fasta file: The output fasta file will be standard fasta file format.


* Reference fasta file:
This file must contain only two lines, with the second containing the reference sequence. The sequence length must be equal to the sequence length of all fastq sequence reads.


* VCF file: The output VCF file will not contain meta data. It will contain the minimum eight standard VCF headers: ‘#CHROM’, ‘POS’, ‘ID’, ‘REF’, ‘ALT’, ‘QUAL’, ‘FILTER’, ‘INFO’. By default, each variant line added will contain ‘1’ in the #CHROM field. ID, QUAL, FILTER and INFO fields will contain ‘.’ in their fields.


## Fastq to Fasta file conversion
By default, running the programme with just a single fastq file argument will execute the fasta to fastq file conversion programme only. The command to execute this is:

     ./VCF_Assembler.py *input.fq*

## VCF file creator
This programme will  be executed if the flag '-V' is used in the command along with both an input fastq file and a reference fasta file. An example is:
	
     ./VCF_Assembler.py *input.fq* -V *reference.fasta*
   
## Example
Example test files are avialable in the directory: test.fq and testref.fasta. Outputs using this script, using both programmes, are available as: testvcf.vcf and test.fasta

To run a fastq to fasta file conversion (must be in working directory containing VCF_Assembler.py):

     ./VCF_Assembler.py test.fq

This adds *test.fa* to the working directory. The read quality information has been removed and the '@' character at the beginning of the read ID string has been replaced with '>'.

To create a VCF file using the fastq file and the reference fasta file (must be in working directory containing VCF_Assembler.py):

     ./VCF_Assembler.py test.fq -V testref.fasta
     
This adds *testvcf.vcf* to the working directory, which contains sequence variant information such as position, ref and alt sequence.
