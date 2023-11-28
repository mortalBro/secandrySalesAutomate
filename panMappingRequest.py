import pandas as pd
import os


folderpath = "/home/tspl/Documents/Script_baz_lol/panmapping"
file_names = os.listdir(folderpath)

herlocation =""
mapplocation =""

heirarchy = pd.read_csv('master_sales_hierarchy_master_202309251057.csv')  
mapping = pd.read_csv('master_wdskucatagory_202309251057.csv')
hei_unique = heirarchy.drop_duplicates(subset=['wd_id', 'wd_town_id','town_code', 'town'],keep='last')
mapping_unique = mapping.drop_duplicates(subset=['sku_code', 'wd_town_id', 'sku_id'],keep='last')


''' merge on the basis of different column name'''
mapping_n_heirarchy = pd.merge(mapping_unique, hei_unique[['wd_id', 'wd_town_id', 'region_code', 'region', 'town_code', 'town']], left_on='wd_town_id', right_on='wd_town_id', how='left')

# create the duplicate named column , if any duplicateec row as per the subset it will keep placesed True and if no-duplicate keep placesed False otherwise empty.
mapping_n_heirarchy['Duplicate'] = mapping_n_heirarchy.duplicated(subset=['wd_id','wd_town_id','sku_id'])
# duplicated('A')
highlight = lambda x: 'background-color: yellow' if x else ''
mapping_n_heirarchy.style.applymap(highlight, subset=['Duplicate'])
mapping_n_heirarchy = mapping_n_heirarchy.astype(str)
print(mapping_n_heirarchy.dtypes) # check datatype
# merge_rows(cells, rows, values, collapse = " ")
mapping_n_heirarchy_rev = mapping_n_heirarchy.tail(4) # keep only last 4 rows of dataframe
sums = mapping_n_heirarchy_rev['last_price'].sum(axis=0)
# mapping_n_heirarchy_rev = mapping_n_heirarchy_rev.append(sums)
# mapping_n_heirarchy_rev = mapping_n_heirarchy.iloc[::-1] # reverse the dataframe with use of sliceing
mapping_n_heirarchy.to_csv('/home/tspl/Documents/Script_baz_lol/panmapping/pan_mapping1.xls', header=True, index=False) 
# dataframe to raw file
# mapping_n_heirarchy_rev.to_csv('pan_mapping_rev.xls', header=True, index=False) # dataframe to raw file