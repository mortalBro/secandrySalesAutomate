import pandas as pd

csv_file = '/home/tspl/Documents/Script_baz_lol/mumbai.csv'
df = pd.read_csv(csv_file)
i=0
for index, row in df.iterrows():
   row['Sales Date'] = pd.to_datetime(row['Sales Date'], format='%d-%b-%y')
   sale=str(row['Sales Date'])
   sale=sale[:len(sale)-9]
   brandcode=row["Brand Code"]
   # saledate=row[""]
   regi=row["Region"]
   stat=row["State"]
   tow=row["Town"]
   brand=row["Category"]
   localRet=row["Local Retailer"]
   localDel=row["Local Dealer"]
   localmod=row["Local Modern"]
   localHow=row["Local Hawker"]
   outst=row["Outstation Retailer"]
   total1=float(localRet)+float(localDel)+float(localmod)+float(localHow)
   # total1=0
   outDel=row["Outstation Dealer"]
   outModer=row["Outstation Modern"]
   outHow=row["Outstation Hawker"]
   total2=float(outst)+float(outDel)+float(outModer)+float(outHow)
   # total2=2
   otherRet=row["Other Retailer"]
   otherDel=row["Other Dealer"]
   otherMod=row["Other Modern"]
   total3=float(otherRet)+float(otherDel)+float(otherMod)
   # total3=0
   grandTotal=total1+total2+total3
   # grandTotal=0
   print(f'''UPDATE gpil_db.transaction_salesdata
SET  local_sales_retail={localRet}, local_sales_dealer={localDel}, local_sales_modern_trade={localmod}, local_sales_hawker={localHow}, total_local_sales={total1}, outstation_sales_reatil={outst}, outstation_sales_dealer={outDel}, outstation_sales_modern_trade={outModer}, outstation_sales_hawker={outHow}, total_outstation_sales={total2}, other_sales_retail={otherRet}, other_sales_dealer={otherDel}, other_sales_modern_trade={otherMod}, total_other_sales={total3}, other_issues_damage=0.0, other_issues_return=0.0, other_issues_other=0.0, total_issue=0.0, grand_total=ROUND({grandTotal},3), unit_price=3174.7, value=unit_price * {grandTotal} 
WHERE sku_code ="{brandcode}" AND  sales_date_time ="{sale}" and transaction_type ="Week4" and  region ="{regi}" and statename ="{stat}" and town_name  ="{tow}";''' )
   print()
