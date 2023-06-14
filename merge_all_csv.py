import os
import pandas as pd

# Set the directory where the CSV files are located
directory = 'C:/Users/risya/OneDrive/Documents/partner'

# Get a list of all the CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
print(csv_files)
# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate through each CSV file
for file in csv_files:
    file_path = os.path.join(directory, file)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    df.drop(["student_id_number", "bank", "datetime_disbursed"], axis=1, inplace=True)


    # Append the data to the merged_data DataFrame
    merged_data = merged_data._append(df, ignore_index=True)

# Save the merged data to a new CSV file
merged_file_path = 'C:/Users/risya/OneDrive/Documents/merged data/datagabungan.csv'
merged_data.to_csv(merged_file_path, index=False)

print("Merging of CSV files completed!")
