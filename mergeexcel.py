import pandas as pd

# File paths
main_file = 'ContactDetails.csv'
file2 = 'ContactDetails2.csv'
file3 = 'ContactDetails3.csv'
file4 = 'ContactDetails4.csv'
file5 = 'ContactDetails5.csv'

# Read the main file
main_df = pd.read_csv(main_file)

# Read the other files
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)
df5 = pd.read_csv(file5)

# Merge all data into the main dataframe
merged_df = pd.concat([main_df, df2, df3, df4, df5], ignore_index=True)

# Remove duplicates if necessary (optional)
merged_df.drop_duplicates(inplace=True)

# Save the merged dataframe back to the main file
merged_df.to_csv(main_file, index=False)

print(f"Data merged successfully into {main_file}")
