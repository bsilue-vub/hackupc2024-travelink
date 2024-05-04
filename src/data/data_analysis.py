import pandas as pd


# Check for duplicate travellers
# ------------------------------

# Load the dataset
df = pd.read_csv('./data/datasets/original_dataset.csv')

# Check for duplicates in the 'Traveller Name' column
duplicates = df['Traveller Name'].duplicated(keep=False)

# Print out duplicate names, if any
if duplicates.any():
    print('\nDuplicate travellers found:\n')
    print(df.loc[duplicates, 'Traveller Name'])
else:
    print('\nNo duplicate travellers found.\n')
