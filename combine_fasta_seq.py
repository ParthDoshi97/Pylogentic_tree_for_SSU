import os
from Bio import SeqIO

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Set the working directory to the 'Data' subdirectory within the current directory
desired_path = os.path.join(current_dir, "Data")
os.chdir(desired_path)


# Function to Fasta files and Merge them
def find_fasta_files(directory):
    """Find all FASTA files in the specified directory and its subdirectories."""
    fasta_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".fasta") or file.endswith(".fa"):
                fasta_files.append(os.path.join(root, file))
    return fasta_files

def combine_fasta_files(output_file, *directories):
    """Combine all FASTA files from specified directories into a single output file."""
    with open(output_file, 'w') as outfile:
        for directory in directories:
            fasta_files = find_fasta_files(directory)
            for fasta_file in fasta_files:
                with open(fasta_file, 'r') as infile:
                    for record in SeqIO.parse(infile, 'fasta'):
                        SeqIO.write(record, outfile, 'fasta')

# Specify the directories containing the FASTA files
directories = ["Egypt SSU", "Lebanon SSU", "Saudi SSU", "Staph Jordan SSU"]

# Specify the output file
output_file = "combined.fasta"

# Combine the FASTA files
combine_fasta_files(output_file, *directories)
