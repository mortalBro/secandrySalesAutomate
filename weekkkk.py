import pandas as pd

csv_file = '/home/tspl/Documents/Script_baz_lol/dataxp.csv'

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
    outDel=row["Outstation Dealer"]
    outModer=["Outstation Modern"]
    outHow=row["Outstation Hawker"]
    total2=float(outst)+float(outDel)+float(outModer)+float(outHow)
    otherRet=row["Other Retailer"]
    otherDel=row["Other Dealer"]
    otherMod=row["Other Modern"]
    total3=float(otherRet)+float(otherDel)+float(otherMod)
    grandTotal=total1+total2+total3
    print('''UPDATE gpi_ss.transaction_salesdata
SET brand_category='{brand}', sku_id='73103', wd_id='3558395', town_id='1356942', sales_date_time='{sale}', local_sales_retail={localRet}, local_sales_dealer={localDel}, local_sales_modern_trade={localmod}, local_sales_hawker={localHow}, total_local_sales={total1}, outstation_sales_reatil={outst}, outstation_sales_dealer={outDel}, outstation_sales_modern_trade={outModer}, outstation_sales_hawker={outHow}, total_outstation_sales={total2}, other_sales_retail={otherRet}, other_sales_dealer={otherDel}, other_sales_modern_trade={otherMod}, total_other_sales={total3}, other_issues_damage=0.0, other_issues_return=0.0, other_issues_other=0.0, total_issue=0.0, grand_total={grandTotal}, created_by='auto scheduler', last_updated=NULL, transaction_source=NULL, created_date='2023-12-02 23:30:06.706370', last_updated_date=NULL, status=1, freeze_status=0, transaction_type='Week4', company='GPI', unit_price=3174.7, region='AHEMDABAD BRANCH', cnf_id='141', value=27556.395999999997, wd_name='A.D. ENTERPRISE', distrcode=NULL, sku_code='CIG0003111', sku_short_name='CVGL', town_code='PATAN', town_name='PATAN-PATAN', wd_type='SFA_Lite', gpi_state='GUJARAT /UT-0331', statename='GUJARAT /UT-0331', `zone`=NULL
WHERE sku_code ="{brandcode}" AND  sales_date_time ="{sale}" and transaction_type ="Week4" and  region ="{regi}" and statename ="{stat}" and town_name  ="{tow}";''' )



    print(row["State"])
    if(i==2):
        break
    i+=1

            # csv_df['total_other_sales'] = csv_df['other_sales_retail'] + csv_df['other_sales_dealer'] + csv_df['other_sales_modern_trade']
            
            # csv_df['grand_total'] = csv_df['total_local_sales'] + csv_df['total_outstation_sales'] + csv_df['total_other_sales']

            # csv_df['total_issue'] = csv_df['other_issues_damage'] + csv_df['other_issues_other'] + csv_df['other_issues_return']

# UPDATE gpi_ss.transaction_salesdata
# SET brand_category='CIG', sku_id='73103', wd_id='3558395', town_id='1356942', sales_date_time='2023-11-30', local_sales_retail=1.68, local_sales_dealer=6.0, local_sales_modern_trade=0.0, local_sales_hawker=1.0, total_local_sales=8.68, outstation_sales_reatil=0.0, outstation_sales_dealer=0.0, outstation_sales_modern_trade=0.0, outstation_sales_hawker=0.0, total_outstation_sales=0.0, other_sales_retail=0.0, other_sales_dealer=0.0, other_sales_modern_trade=0.0, total_other_sales=0.0, other_issues_damage=0.0, other_issues_return=0.0, other_issues_other=0.0, total_issue=0.0, grand_total=8.680, created_by='auto scheduler', last_updated=NULL, transaction_source=NULL, created_date='2023-12-02 23:30:06.706370', last_updated_date=NULL, status=1, freeze_status=0, transaction_type='Week4', company='GPI', unit_price=3174.7, region='AHEMDABAD BRANCH', cnf_id='141', value=27556.395999999997, wd_name='A.D. ENTERPRISE', distrcode=NULL, sku_code='CIG0003111', sku_short_name='CVGL', town_code='PATAN', town_name='PATAN-PATAN', wd_type='SFA_Lite', gpi_state='GUJARAT /UT-0331', statename='GUJARAT /UT-0331', `zone`=NULL
# WHERE sku_code ="CIG0003111" AND  sales_date_time ="2023-11-30" and transaction_type ="Week4" and  region ="AHEMDABAD BRANCH" and statename ="GUJARAT /UT-0331" and town_name  ="PATAN-PATAN";


# SELECT x.* FROM gpi_ss.transaction_salesdata x
# WHERE sku_code ="CIG0003111" AND  sales_date_time ="2023-11-30" and transaction_type ="Week4" and  region ="AHEMDABAD BRANCH" and statename ="GUJARAT /UT-0331" and town_name  ="PATAN-PATAN"