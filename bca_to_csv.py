import csv
import re
import os

# Define your input directory here
input_dir = "txt"
output_file = "all_transactions_filtered.csv"


# Function to process each line and extract transaction data
def process_line(line):
    data = re.split(r'\s{2,}', line.strip())
    return data


# Write transaction data to the output CSV file, excluding specified columns
with open(output_file, "w", newline='') as out_f:
    writer = csv.writer(out_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Write header row without the specified columns
    writer.writerow(["NO", "NAMA PELANGGAN", " ", "IDR", "TANGGAL", "JAM", "LOKASI", "KETERANGAN2"])

    # Loop through all text files in input_dir
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)

            # Read input text file and process
            with open(file_path, "r") as f:
                lines = f.readlines()

            # Process transactions and write rows without the specified columns
            for line in lines:
                if re.match(r'\s+\d+\s+\d+', line):
                    data = process_line(line)
                    filtered_data = [data[0], data[2], "", data[4], data[5], data[6], data[7], data[8]]
                    writer.writerow(filtered_data)
