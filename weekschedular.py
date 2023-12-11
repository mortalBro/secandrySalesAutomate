# UPDATE gpil_db.transaction_salesdata
# SET sku_id='6088244', wd_id='3208342', town_id='879682', sales_date_time='2023-12-07', local_sales_retail=0.63, local_sales_dealer=0.0, local_sales_modern_trade=0.0, local_sales_hawker=0.0, outstation_sales_reatil=0.45, outstation_sales_dealer=0.0, outstation_sales_modern_trade=0.0, outstation_sales_hawker=0.0, other_sales_retail=0.0, other_sales_dealer=0.0, other_sales_modern_trade=0.0, other_issues_other=0.0, other_issues_damage=0.0, other_issues_return=0.0, transaction_source=NULL, created_date='2023-12-08 18:56:59.122627', created_by='ap@0456', last_updated_date=NULL, last_updated=NULL, status=1, total_outstation_sales=0.45, grand_total=1.080, total_issue=0.0, total_local_sales=0.63, total_other_sales=0.0, brand_category='CIG', freeze_status=0, transaction_type='Week1', cnf_id='3812', company='GPI', region='HYDERABAD BRANCH', unit_price=1356.82, value=1465.3655999999999, sku_code='CIG0001115', sku_short_name='FOCUS MINT UP SQ 10s', town_code='488400', wd_name='THATIPALLI AGAENCIES', wd_type='SFA_Lite', town_name='KHAMMAM-0488400', distrcode=NULL, gpi_state='ROS-1040007', statename='ROS-1040007', `zone`=NULL
# WHERE id=8249654;














import pandas as pd
 
user_path = '/home/tspl/Documents/Script_baz_lol/fik/userA.csv'
csv_path = '/home/tspl/Documents/Script_baz_lol/fik/csvfile.csv'
 
# Read the CSV files into DataFrames
user_df = pd.read_csv(user_path)
csv_df = pd.read_csv(csv_path)
 
# Merge the DataFrames on the common column 'WD Name'
merged_df = pd.merge(csv_df, user_df, left_on='WD Name', right_on='first_name', how='left')
 
# Rename the new column to 'wd_id'
merged_df.rename(columns={'user_id': 'wd_id'}, inplace=True)
 
# Drop the extra columns from the merge
merged_df.drop(columns=['first_name'], inplace=True)
 
# Save the updated DataFrame to a new CSV file
merged_df.to_csv('/home/tspl/Documents/Script_baz_lol/fik/optimized_output.csv', index=False)


 sku_code   ="CIG0003111" AND  sales_date_time    ="2023-11-30"  and   transaction_type    ="Week4"  and region  ="AHEMDABAD BRANCH"  and  statename    ="GUJARAT /UT-0331" and  town_name    ="PATAN-PATAN"
