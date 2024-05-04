import pandas as pd


# Check for duplicate travellers
# ------------------------------

# Load the dataset
df = pd.read_csv('./data/dataset.csv')

# Check for duplicates in the "Traveller Name" column
duplicates = df['Traveller Name'].duplicated(keep=False)  # 'keep=False' marks all duplicates as True

# Print out duplicate names, if any
if duplicates.any():
    print("Duplicate names found in 'Traveller Name' column:")
    print(df.loc[duplicates, 'Traveller Name'])
else:
    print("No duplicate names found in 'Traveller Name' column.")

