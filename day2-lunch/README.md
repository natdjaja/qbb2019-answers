(for exercise 1)
(for exercise a)

 head -40000 SRR072893.fastq > SRR072893.10k.fastq
(checked the lines)

 wc -l SRR072893.10k.fastq 
 
 
 
 (for exercise b)
 
 fastqc SRR072893.10k.fastq 
 
 
 
 (for exercise c)
 
 hisat2 -x BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam
 
 
 (for exercise d)
 
 
 samtools sort -@ 4 SRR072893.10k.sam -o SRR072893.10k.bam
 (converts this to output path file which we create)
 samtools index SRR072893.10k.bam SRR072893.10k.bam.bai
 (index and then just write in new file that we want)
 
 (for exercise e)
 
 stringtie SRR072893.10k.bam -e -B -p 4 -G ../genomes/BDGP6.Ensembl.81.gtf -o BDGP6sortedbam
 
 
 
 
 (for exercise 3)
 
 sort SRR072893.sam | cut -f 1 | uniq -c > SRR072893.txt
 
 (we want to sort our sam file which is readable and is the product of converting the hisat2 files which has a header and an aligment section. we don't use the bam file since this is a compressed binary file and can't be read)
 
 a slower way could be to...
 a faster way would be to...
 
 
 
 (for exercise 4)
 
 samtools view SRR072893.sam | awk '{print NF}' | sort SRR072893.sam | uniq -c > SRR072893.columns
 
 
 
 
 
 
 
 
 