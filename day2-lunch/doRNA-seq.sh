#!/bin/bash

GENOME=../qbb2019-answers/day2-lunch/BDGP6
ANNOTATION=../qbb2019-answers/day2-lunch/BDGP6sortedbam.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq
  fastqc $SAMPLE.fastq 
  hisat2 -p 4 -x BDGP6 -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -@ 4 $SAMPLE.sam -o $SAMPLE.bam
  samtools index $SAMPLE.bam
  stringtie $SAMPLE.bam -e -B -p 4 -G ../genomes/BDGP6.Ensembl.81.gtf -o $SAMPLE.gtf
done

