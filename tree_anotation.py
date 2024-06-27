import os
import csv
from Bio import SeqIO

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Set the working directory to the 'Data' subdirectory within the current directory
desired_path = os.path.join(current_dir, "Data")
os.chdir(desired_path)

# Function Formate Annotation 
def format_annotation(record, country):
    """
    Format the annotation string for a sequence record and include the country information.
    """
    description_parts = record.description.split(' ')
    unique_id = description_parts[0]
    gene_info = ' '.join(description_parts[1:]).split('[')[0].strip()
    species_info = ' '.join(record.description.split('[')[1].split(']')[0].split('|')[0].split(' ')[:-1])

    annotation = {
        "Identifier": unique_id,
        "Function": gene_info,
        "Species": species_info,
        "Country": country
    }
    
    return annotation

# Specify the folder structure
folders = ["Egypt SSU", "Lebanon SSU", "Saudi SSU", "Staph Jordan SSU"]  # Replace with actual folder names

# Initialize an empty list to store annotations
annotations = []

# Process each folder
for folder in folders:
    country = folder  # Use folder name as country name
    fasta_files = [f for f in os.listdir(folder) if f.endswith('.fasta')]

    for fasta_file in fasta_files:
        file_path = os.path.join(folder, fasta_file)
        sequences = list(SeqIO.parse(file_path, "fasta"))

        for record in sequences:
            annotation = format_annotation(record, country)
            annotations.append(annotation)

# Define CSV file columns
columns = ["Identifier", "Function", "Species", "Country"]

# Write annotations to a CSV file
output_csv = "sequence_annotations.csv"
with open(output_csv, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for annotation in annotations:
        writer.writerow(annotation)

print(f"Annotations have been written to {output_csv}")
