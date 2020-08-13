# VCF_Assembler
This programme was created for a post-graduate university course in computational biology.
A programme to create VCF files and convert FASTQ files to FASTA file format.


## Dependencies
This programme requires Python 3


## File inputs and outputs

* Fastq file (required): The fastq input file must be in standard four-line-per-sequence format, with the second line containing the sequence.


* Fasta file: The output fasta file will be standard fasta file format and the stem name of this file must be specified after the '-o' flag.


* Reference fasta file: The file used to call variants. This file must contain only two lines, with the second containing the reference sequence. The sequence length must be equal to the sequence length of all fastq sequence reads.


* VCF file: The output VCF file will not contain meta data. It will contain the minimum eight standard VCF headers: ‘#CHROM’, ‘POS’, ‘ID’, ‘REF’, ‘ALT’, ‘QUAL’, ‘FILTER’, ‘INFO’. By default, each variant line added will contain ‘1’ in the #CHROM field. ID, QUAL, FILTER and INFO fields will contain ‘.’ in their fields. The stem name of this file must be specified after the '-o' flag.


## Fastq to Fasta file conversion
By default, running the programme with just a single fastq file argument, the '-o' flag and an output file stem name will execute the fastq to fasta file conversion programme only. The command to execute this is:

   ./VCF_Assembler.py *input.fq* -o *outputFASTAname*

## VCF file creator
This programme will  be executed if the flag '-r' is used in the command along with both an input fastq file and a reference fasta file, as well as the '-o' flag and an output file stem name. An example is:
	
   ./VCF_Assembler.py *input.fq* -r *reference.fasta* -o *outputVCFname*
   
## Example
Example test files are avialable in the directory: 'test.fq' and 'testref.fa'.

To run a fastq to fasta file conversion (must be in working directory containing VCF_Assembler.py):

   ./VCF_Assembler.py test.fq -o *output*

This adds 'output.fa' to the working directory. The read quality information has been removed and the '@' character at the beginning of the read ID string has been replaced with '>'.

To create a VCF file using the fastq file and the reference fasta file (must be in working directory containing VCF_Assembler.py):

   ./VCF_Assembler.py test.fq -r testref.fa -o *output*
     
This adds 'output.vcf' to the working directory, which contains sequence variant information such as position, ref and alt sequence. In this case, 5 variants will be listed in the VCF file.
