import sys
from Bio import AlignIO, SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align import MultipleSeqAlignment
import csv

def remove_redundant_sequences(sequences):
    """Remove redundant sequences from the list."""
    unique_sequences = {}
    redundant_count = 0
    
    for seq_record in sequences:
        seq_str = str(seq_record.seq)
        if seq_str not in unique_sequences:
            unique_sequences[seq_str] = seq_record
        else:
            redundant_count += 1
    
    filtered_sequences = list(unique_sequences.values())
    
    return filtered_sequences, redundant_count

def process_sequences(input_file, output_file_phylip, mapping_file):
    # Read the sequences from the input file
    sequences = list(SeqIO.parse(input_file, "fasta"))
    
    # Remove redundant sequences
    filtered_sequences, redundant_count = remove_redundant_sequences(sequences)
    
    # Create a mapping dictionary and rename sequences to shorter, unique identifiers
    mapping = {}
    unique_records = []
    for i, record in enumerate(filtered_sequences):
        new_id = f"seq{i+1}"
        mapping[new_id] = record.id
        new_record = SeqRecord(Seq(str(record.seq)), id=new_id, description="")
        unique_records.append(new_record)
    
    # Create a MultipleSeqAlignment object
    unique_alignment = MultipleSeqAlignment(unique_records)
    
    # Write the alignment to a PHYLIP file
    AlignIO.write(unique_alignment, output_file_phylip, "phylip")
    
    # Save the mapping to a CSV file
    with open(mapping_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["New Identifier", "Original Identifier"])
        for new_id, original_id in mapping.items():
            writer.writerow([new_id, original_id])
    
    # Print the summary
    print(f"Total sequences: {len(sequences)}")
    print(f"Redundant sequences removed: {redundant_count}")
    print(f"Remaining sequences: {len(filtered_sequences)}")
    print(f"Conversion complete. PHYLIP file saved as {output_file_phylip}")
    print(f"Identifier mapping saved as {mapping_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_fasta> <output_phylip> <mapping_csv>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file_phylip = sys.argv[2]
    mapping_file = sys.argv[3]
    
    process_sequences(input_file, output_file_phylip, mapping_file)
