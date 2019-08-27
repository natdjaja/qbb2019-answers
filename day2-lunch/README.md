(for exercise 1)
(for exercise a)

 head -40000 SRR072893.fastq > SRR072893.10k.fastq
(checked the lines)

 wc -l SRR072893.10k.fastq 
 
 
 
 (for exercise b)
 gi
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
 
 grep "^SRR072893" SRR072893.sam | cut -f 3 | sort | uniq -c > SRR072893.txt
 
 cut -f 3 SRR072893.sam | sort | uniq -c
 
  1 211000022278750
    2 211000022278876
    1 211000022278877
    1 211000022278878
    5 211000022278879
    1 211000022278881
    2 211000022279055
    1 211000022279100
    2 211000022279109
    1 211000022279132
    2 211000022279222
    3 211000022279343
    1 211000022279420
    1 211000022279446
    1 211000022279540
    3 211000022279676
    1 211000022279708
    1 211000022279810
    2 211000022280043
    2 211000022280304
    1 211000022280508
    1 211000022280645
 5724 2L
 6821 2R
 6117 3L
 7990 3R
  444 4
    1 Unmapped_Scaffold_58
 5848 X
   32 Y
   73 dmel_mitochondrion_genome
   35 rDNA

 
 (we want to sort our sam file which is readable and is the product of converting the hisat2 files which has a header and an aligment section. we don't use the bam file since this is a compressed binary file and can't be read)
 
 a slower way could be to...
 a faster way would be to...
 
 
 
 (for exercise 4)
 
 samtools view SRR072893.sam | awk '{print NF}' | sort SRR072893.sam | uniq -c > SRR072893.columns
 
 

 
 
 
 
 
 