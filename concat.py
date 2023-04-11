import pandas as pd

# Read the data from the first Excel sheet into a DataFrame
df1 = pd.read_excel('first_excel_sheet.xlsx')

# Read the data from the second Excel sheet into another DataFrame
df2 = pd.read_excel('second_excel_sheet.xlsx')

# Combine the two DataFrames into a single DataFrame
df = pd.concat([df1, df2], ignore_index=True)

# Group the data by employee name and assign sequential unique IDs to each group
employee_groups = df.groupby('Employee Name')
unique_id_counter = 1
for name, group in employee_groups:
    group_size = len(group)
    group_indices = group.index.to_list()
    for i in range(group_size):
        if pd.isna(group.loc[group_indices[i], 'Unique ID']):
            new_unique_id = f"{unique_id_counter:03d}-{group.iloc[0]['Unique ID'].split('-')[1]}"
            df.at[group_indices[i], 'Unique ID'] = new_unique_id
            unique_id_counter += 1

# Save the updated data to a new Excel sheet
df.to_excel('updated_excel_sheet.xlsx', index=False)
