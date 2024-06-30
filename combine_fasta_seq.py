import sys
import os
from Bio import SeqIO

def find_fasta_files(directory):
    """Find all FASTA files in the specified directory and its subdirectories."""
    fasta_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".fasta") or file.endswith(".fa"):
                fasta_files.append(os.path.join(root, file))
    return fasta_files

def combine_fasta_files(output_file, directories):
    """Combine all FASTA files from specified directories into a single output file."""
    with open(output_file, 'w') as outfile:
        for directory in directories:
            fasta_files = find_fasta_files(directory)
            for fasta_file in fasta_files:
                with open(fasta_file, 'r') as infile:
                    for record in SeqIO.parse(infile, 'fasta'):
                        SeqIO.write(record, outfile, 'fasta')

if __name__ == "__main__":
    # Get directories and output file from command line arguments
    output_file = sys.argv[1]
    directories = sys.argv[2:]

    # Check if any directories were entered
    if not directories:
        print("No directories were entered. Exiting.")
    else:
        # Combine the FASTA files
        combine_fasta_files(output_file, directories)
        print(f"FASTA files have been combined into {output_file}")
