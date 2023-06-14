import csv

input_file = "input.csv"
output_file = "output.csv"

with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.writer(csv_output)

    # Get the header row
    header = next(reader)

    # Remove the "Item ID #2" column from the header
    header.pop(12)

    # Modify the header to add the copied column
    header.insert(0, "Ref Code")

    # Write the modified header to the output file
    writer.writerow(header)

    # Read the remaining rows
    rows = list(reader)

    # Sort the rows by Transaction time in descending order
    sorted_rows = sorted(rows, key=lambda x: x[4], reverse=False)

    # Iterate over the sorted rows
    for row in sorted_rows:
        # Copy the "Item name #1" value
        copied_value = row[9]

        # Remove "pembayaran bulanan" from the copied value
        copied_value = copied_value.replace("Pembayaran Bulanan", "").strip()

        # Insert the modified value as the first column
        row.insert(0, copied_value)

        # Fill the blank "Acquiring Bank" value with the corresponding "Payment Type" value
        if not row[7]:
            payment = row[2]
            row[7] = payment

        # Remove the "Item ID #2" column
        row.pop(12)

        # Remove the single quotes from the Order ID column
        row[1] = row[1].replace("'", "")

        # Write the modified row to the output file
        writer.writerow(row)

print("CSV file processing complete. Output written to", output_file)
