# Snakefile
# Rule to final result 
rule all:
    input:
        "Results/filter_alignement.phy",
        "Results/mapping.csv"

# Rule to merge all SSU seq file into one single file
rule combine_fasta:
    input:
        directories = [
            "Data/Egypt",
            "Data/Lebanon",
            "Data/Saudi",
            "Data/Jordan"
        ]
    output:
        "Results/combined.fasta",
        "Results/annotation.csv"
    params:
        script1 = "combine_fasta_seq.py",
        script2 = "tree_annotation.py"
    shell:
        """
        python {params.script1} {output[0]} {input.directories}
        python {params.script2} {output[1]} {input.directories}
        """

# Rule Multi sequence Alignment (Using Mafft) 
rule MSA:
    input:
        "Results/combined.fasta"
    output:
        "Results/aligned.fasta"
    shell:
        """
        /home/ubuntu/miniconda3/bin/./mafft --retree 2 --parttree --maxiterate 1000 --globalpair --thread 4 {input} > {output}
        """

# Rule for checking redundancy and missing loci 
rule filtering:
    input:
        "Results/aligned.fasta"
    output:
        "Results/filter_alignement.phy",
        "Results/mapping.csv"
    params:
        script = "filter_alignment.py"
    shell:
        """
        python {params.script} {input} {output[0]} {output[1]}
        """