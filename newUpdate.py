import pandas as pd

df1 = pd.read_csv('/home/tspl/Documents/Script_baz_lol/mumbaiGPI.csv')
df2 = pd.read_csv("/home/tspl/Documents/Script_baz_lol/transaction_salesdata_202312111847.csv")



compare_columns = ['column1', 'column2']

# Find rows that are unique to each DataFrame based on the chosen columns
unique_df1 = df1[~df1.set_index(compare_columns).index.isin(df2.set_index(compare_columns).index)]
unique_df2 = df2[~df2.set_index(compare_columns).index.isin(df1.set_index(compare_columns).index)]

# Concatenate the results
result = pd.concat([unique_df1, unique_df2])

# Save the result to a new CSV file
result.to_csv('unique_data.csv', index=False)
