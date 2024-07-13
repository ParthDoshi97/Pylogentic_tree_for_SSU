# Snakefile

# Rule to specify the final target files
rule all:
    input:
        "Results/RAxML_bestTree.nwk"

# Rule to merge all SSU sequence files into one single file
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
        # Combine all FASTA sequences into one file
        python {params.script1} {output[0]} {input.directories}
        
        # Generate annotation for the combined sequences
        python {params.script2} {output[1]} {input.directories}
        """

# Rule for Multi-Sequence Alignment (Using MAFFT)
rule MSA:
    input:
        "Results/combined.fasta"
    output:
        "Results/aligned.fasta"
    shell:
        """
        # Perform multiple sequence alignment using MAFFT
        /home/ubuntu/miniconda3/bin/./mafft --retree 2 --parttree --maxiterate 1000 --globalpair --thread 4 {input} > {output}
        """

# Rule for checking redundancy and missing loci
rule filtering:
    input:
        "Results/aligned.fasta"
    output:
        "Results/filter_alignment.phy",
        "Results/mapping.csv"
    params:
        script = "filter_alignment.py"
    shell:
        """
        # Filter the aligned sequences to check for redundancy and missing loci
        python {params.script} {input} {output[0]} {output[1]}
        """

# Rule for generating the phylogenetic tree
rule Phylogenetic_tree:
    input:
        "Results/filter_alignment.phy"
    output:
        "Results/RAxML_bestTree.nwk"
    shell:
        """
        # Generate bootstrap replicates
        /home/ubuntu/standard-RAxML/./raxmlHPC -s {input} -n bootstraps -m GTRGAMMA -p 12345 -x 12345 -# 1000 -w /home/ubuntu/Pylogentic_tree_for_SSU/Results/
        
        # Generate the best tree with branch lengths using the bootstrap replicates
        /home/ubuntu/standard-RAxML/./raxmlHPC -s {input} -n bestTree -m GTRGAMMA -p 12345 -f d -t /home/ubuntu/Pylogentic_tree_for_SSU/Results/RAxML_bootstrap.bootstraps -w /home/ubuntu/Pylogentic_tree_for_SSU/Results/
        
        # Rename the best tree output to Newick format
        mv Results/RAxML_bestTree.bestTree {output}
        """
