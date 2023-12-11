import pandas as pd

heirarchy = pd.read_csv('master_sales_hierarchy_master_202312051225.csv')   # read csv as dataframe
mapping = pd.read_csv('master_wdskucatagory_202312051226.csv')

# print(mapping.columns)
# print(heirarchy.columns)
# print(len(heirarchy),"======================================",heirarchy.shape[0]) # print rows count or len of rows
hei_unique = heirarchy.drop_duplicates(subset=['wd_id', 'wd_town_id','town_code', 'town'],keep='last') # if any duplicate rows as per the subset it will drop the other excluding last one
# print(len(hei_unique),'====================================',hei_unique.shape[0],"--------------",hei_unique.columns)
mapping_unique = mapping.drop_duplicates(subset=['sku_code', 'wd_town_id', 'sku_id'],keep='last') # if any duplicate rows as per the subset it will drop the other excluding last one
# print(len(mapping_unique),'====================================',mapping_unique.shape[0],"--------------",mapping_unique.columns)


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
mapping_n_heirarchy.to_csv('pan_mapping1.xls', header=True, index=False) 
# dataframe to raw file
# mapping_n_heirarchy_rev.to_csv('pan_mapping_rev.xls', header=True, index=False) # dataframe to raw file