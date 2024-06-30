import os
import csv
from Bio import SeqIO
import sys

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

def process_folders(directories, output_csv):
    # Initialize an empty list to store annotations
    annotations = []

    # Process each folder
    for folder in directories:
        country = os.path.basename(folder)  # Use folder name as country name
        fasta_files = [f for f in os.listdir(folder) if f.endswith('.fasta') and f != 'Reference genome.fasta']

        for fasta_file in fasta_files:
            file_path = os.path.join(folder, fasta_file)
            sequences = list(SeqIO.parse(file_path, "fasta"))

            for record in sequences:
                annotation = format_annotation(record, country)
                annotations.append(annotation)

    # Define CSV file columns
    columns = ["Identifier", "Function", "Species", "Country"]

    # Write annotations to a CSV file
    with open(output_csv, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for annotation in annotations:
            writer.writerow(annotation)

    print(f"Annotations have been written to {output_csv}")

if __name__ == "__main__":
    # Get directories and output file from command line arguments
    directories = sys.argv[2:]
    output_csv = sys.argv[1]

    # Check if any directories were entered
    if not directories:
        print("No directories were entered. Exiting.")
    else:
        # Process the directories and write annotations to the output CSV file
        process_folders(directories, output_csv)
