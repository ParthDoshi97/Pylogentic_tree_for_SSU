# Snakefile

# Rule to final result 
rule all:
    input:
         "Results/combined.fasta",
         "Results/annotation.csv"

# Rule to merge all SSU seq file into one single file
rule combine_fasta:
    input:
        directories = ["Data",
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