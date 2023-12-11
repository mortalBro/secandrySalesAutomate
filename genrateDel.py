import pandas as pd

csv_file = '/home/tspl/Documents/Script_baz_lol/mumbaikoop.csv'
df = pd.read_csv(csv_file)
i=0
for index, row in df.iterrows():
   brand=str(row["Brand Codes"])
   brand=brand[1:len(brand)-1]
   tow=row["Town"]
   print(f'''DELETE FROM gpil_db.transaction_salesdata x
WHERE sku_code  NOT  in ({brand}) and sales_date_time ="2023-11-30" and region ="MUMBAI BRANCH"  AND  transaction_type ="Week4" and  town_name ="{tow}";''')
   print()
   # i+=1
   # if(i==2):
   #    break
   
   
   
   
# DELETE FROM gpil_db.transaction_salesdata
# WHERE id=2008113;

# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(2008113, '6060220', '2278215', '135489', '2023-03-21', 36.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SFA', '2023-03-23 17:19:15.184708', 'auto_scheduler', NULL, NULL, 1, 0.0, 36.000, 0.0, 36.0, 0.0, 'CDI', 1, 'Week3', '141', 'GPI', 'AHEMDABAD BRANCH', 66.79, 2404.44, 'CDICOV1112', 'Funda C Orange Jar(315Gms)', 'VADODARANE', 'NEXUS ENTERPRISE', 'SFA', 'VADODARANE-VADODARANE', '2278215-VADODARANE', NULL, NULL, NULL);

# SELECT x.* FROM gpi_ss.transaction_salesdata x
# WHERE sku_code  NOT  in ("CIG0003111", "CIG0003085", "CIG0001112", "CIG0001113", "CIG0002096",
#     "CIG0002746", "CIG0002761", "CIG0002628", "CIG0002632", "CIG0009378",
#     "CIG0002748", "CIG0002047", "CIG0002069", "CDICOV1112", "CDICOV1111",
#     "CDICGM1111", "CDINEJ1115", "CDINEJ1116", "CIG0002014", "CIG0002001",
#     "CIG0002010", "CIG0002033", "CIG0002030", "CIG0002077", "CIG0002020",
#     "CIG0002021", "CIG0002051", "CIG0002037", "CIG0002036", "CIG0002052",
#     "CIG0002076", "CIG0002075", "CIG0005525", "CIG0005510", "CIG0005530",
#     "CIG0005528") and sales_date_time ="2023-11-30"   AND  transaction_type ="Week4" and  town_name ="PAtna"