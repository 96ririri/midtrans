import pandas as pd

# Read the CSV file
df = pd.read_csv('payout.csv')

# List of columns to remove
columns_to_remove = ['Customer Email', 'Credit Card Number Mask', '3D Secure', 'Card Association',
                     'Bank On Us/ Off Us', 'Coins Share', 'Transaction ID', 'TREF ID']

# Drop the specified columns
df = df.drop(columns=columns_to_remove)

# Reorder columns
df = df[['Order', 'Payment Type', 'Transaction Time', 'Settlement Time', 'Refund Amount', 'Amount',
         'Acquiring Bank', 'Transaction Fee', 'Merchant Has', 'Refund', 'Payment Options']]

# Save the modified DataFrame back to a CSV file
df.to_csv('payout_reconcile.csv', index=False)
