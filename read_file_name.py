import os
from converter_xlsx_to_csv import excel_to_csv
from replacement_of_header import headerChangeMapping
from replacement_of_header import headerChangeMaster_user
from replacement_of_header import headerChangeHierrachy
from replacement_of_header import headerChangeWd_master
from replacement_of_header import moveFileIfNotExcel
from fileCheck import zeroInUserLocation
from fileCheck import positionOfBlankSpaces
from fileCheck import countBlankSpace
from fileCheck import herValidation
from uplodFile import uatUploadUser
from uplodFile import productionUploadUser
from uplodFile import uatUploadWdMaster
from uplodFile import productionUploadWdMaster
from uplodFile import uatUploadHier
from uplodFile import productionUploadHier
from uplodFile import productionUploadMapping
from uplodFile import uatUploadMapping

# /home/tspl/Documents/Script_baz_lol/jadugar
pa="/home/tspl/Documents/Script_baz_lol/csv_jadugar/"
folder_path = "/home/tspl/Documents/Script_baz_lol/jadugar"
mapping_file=["WD_SKU_M","Add_WD_S","wd_sku_m","wd_sku_m","Add_WD_S","ADD WD_S","WD SKU M","Wd_SKU_M","ADD_WD_S",'ADD WD S',"ADD WD S"]

useR=False
uMaster=False
uHier=False
uMap=False
n=4

# useR=False
# uMaster=True
# uHier=False
# uMap=False
# # n=1


file_names = os.listdir(folder_path)
for i in file_names:
    if i.startswith(".~lock."):
        file_names.remove(i)

if(len(file_names)==1 and len(file_names[0])>=8 and file_names[0][:8] in mapping_file):
    useR=True
    uMaster=True
    uHier=True
def BoomBamm():
    pa="/home/tspl/Documents/Script_baz_lol/csv_jadugar/"
    folder_path = "/home/tspl/Documents/Script_baz_lol/jadugar"
    mapping_file=["WD_SKU_M","Add_WD_S","wd_sku_m","wd_sku_m","Add_WD_S","ADD WD_S","WD SKU M","Wd_SKU_M","ADD_WD_S",'ADD WD S',"ADD WD S"]

    useR=False
    uMaster=False
    uHier=False
    uMap=False
    n=4

    # useR=True
    # uMaster=True
    # uHier=False
    # uMap=False
    # # n=1


    file_names = os.listdir(folder_path)
    for i in file_names:
        if i.startswith(".~lock."):
            file_names.remove(i)

    if(len(file_names)==1 and len(file_names[0])>=8 and file_names[0][:8] in mapping_file):
        useR=True
        uMaster=True
        uHier=True
        uMap=False
        n=1
    for i in range(n):
        for file_name in file_names:
            # if ((file_name.startswith("sales") or checkHer(file_name.split())) and useR and uMaster and uHier==False):
            if (file_name.startswith("sales") and useR and uMaster and uHier==False):
                uHier=True
                if((file_name[-1:-4:-1][::-1])!="csv"):
                    excel_to_csv("jadugar"+file_name,file_name)
                    headerChangeHierrachy(pa+file_name)
                    # "/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv"
                    value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv")
                    if(value):
                        herValidation("/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv")
                        outputPath= "/home/tspl/Documents/Script_baz_lol/fileCheck/herOP.csv"
                        uatUploadHier(outputPath)
                        productionUploadHier(outputPath)
                else:
                    moveFileIfNotExcel("jadugar/"+file_name,file_name)
                    headerChangeHierrachy(pa+file_name)
                    # "/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv"
                    countBlankSpace("/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv")
                    herValidation("/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv")
                    outputPath= "/home/tspl/Documents/Script_baz_lol/fileCheck/herOP.csv"
                    uatUploadHier(outputPath)
                    productionUploadHier(outputPath)

            elif(file_name.startswith("user") and useR==False):
                useR=True
                if((file_name[-1:-4:-1][::-1])!="csv"):
                    excel_to_csv("jadugar"+file_name,file_name)
                    headerChangeMaster_user(pa+file_name)
                    value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/final_jadugar/user.csv")
                    if(value):
                        zeroInUserLocation("/home/tspl/Documents/Script_baz_lol/final_jadugar/user.csv")
                        outPUT="/home/tspl/Documents/Script_baz_lol/fileCheck/userOP.csv"
                        uatUploadUser(outPUT)
                        productionUploadUser(outPUT)
                else:
                    moveFileIfNotExcel("jadugar/"+file_name,file_name)
                    headerChangeMaster_user(pa+file_name)
                    value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/final_jadugar/user.csv")
                    if (value):
                        zeroInUserLocation("/home/tspl/Documents/Script_baz_lol/final_jadugar/user.csv")
                        outPUT="/home/tspl/Documents/Script_baz_lol/fileCheck/userOP.csv"
                        uatUploadUser(outPUT)
                        productionUploadUser(outPUT)
                    

            elif(file_name.startswith("wd_m") and useR and uMaster==False):
                uMaster=True
                if((file_name[-1:-4:-1][::-1])!="csv"):
                    excel_to_csv("jadugar"+file_name,file_name)
                    # print(pa+file_name[:len(file_name)-4]+"csv")
                    headerChangeWd_master(pa+file_name[:len(file_name)-4]+"csv")
                    outPUT="/home/tspl/Documents/Script_baz_lol/fileCheck/master.csv"
                    value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/fileCheck/master.csv")
                    if(value):
                        uatUploadWdMaster(outPUT)
                        productionUploadWdMaster(outPUT)
                else:
                    moveFileIfNotExcel("jadugar/"+file_name,file_name)
                    headerChangeWd_master(pa+file_name)
                    outPUT="/home/tspl/Documents/Script_baz_lol/fileCheck/master.csv"
                    value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/fileCheck/master.csv")
                    if(value):
                        uatUploadWdMaster(outPUT)
                        productionUploadWdMaster(outPUT)


            elif len(file_name)>=8:
                if(file_name[:8] in mapping_file and uHier and uMaster and useR and uMap==False):
                    uMap=True
                    if((file_name[-1:-4:-1][::-1])!="csv"):
                        excel_to_csv("jadugar/"+file_name,file_name)
                        headerChangeMapping(pa+file_name[:len(file_name)-4]+"csv")
                        output="/home/tspl/Documents/Script_baz_lol/fileCheck/mapping.csv"
                        value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/fileCheck/mapping.csv")
                        if(value):
                            productionUploadMapping(output)
                            uatUploadMapping(output)
                    else:
                        moveFileIfNotExcel("jadugar/"+file_name,file_name)
                        headerChangeMapping(pa+file_name)
                        output="/home/tspl/Documents/Script_baz_lol/fileCheck/mapping.csv"
                        value=countBlankSpace("/home/tspl/Documents/Script_baz_lol/fileCheck/mapping.csv")
                        if(value):
                            productionUploadMapping(output)
                            uatUploadMapping(output)
        print("File Name:ABHI", file_name)




BoomBamm()




# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8069200, '6126376', '2997328', '581625', '2023-11-30', 6.69, 0.0, 0.0, 0.0, 2.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, '2023-12-02 15:48:54.628920', '', NULL, NULL, 1, 2.05, 8.740, 0.0, 6.69, 0.0, 'CIG', 1, 'Week4', '2749', 'IPM', 'HYDERABAD BRANCH', 6431.67, 56212.7958, 'CIG0002037', 'MARLBORO GOLD ADVANCE KS BOX 10 (ST UPG)', '0489000', 'HARI HARA KIRANAM & GENERAL STORES', 'SFA_Lite', 'KARIMNAGAR-0489000', NULL, 'ROS-1040007', 'ROS-1040007', NULL);










# ######################################################################3

# SELECT * from  gpil_db.transaction_salesdata x
# WHERE wd_id =2697229    and sales_date_time between '2023-11-22' and '2023-11-30' and transaction_type in ("Week4")
# ORDER BY x.id DESC





# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097767, '6212403', '2697229', '153989', '2023-11-30', 0.42, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435599', 'ap@0456', NULL, NULL, 1, 0.0, 0.420, 0.0, 0.42, 0.0, 'CIG', 1, 'Week4', '3852', 'GPI', 'HYDERABAD BRANCH', 1888.23, 793.0566, 'CIG0005528', 'STELLAR SHIFT ME-SS RC-97MM', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097766, '6055868', '2697229', '153989', '2023-11-30', 0.07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435598', 'ap@0456', NULL, NULL, 1, 0.0, 0.070, 0.0, 0.07, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 3348.97, 234.42790000000002, 'CIG0002076', 'PARLIAMENT GOLD KS 10', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097765, '5198426', '2697229', '153989', '2023-11-30', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435598', 'ap@0456', NULL, NULL, 1, 0.0, 0.000, 0.0, 0.0, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6431.67, 0.0, 'CIG0002020', 'MARLBORO FUSE BEYOND (2.0) KS BOX 10', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097764, '6030149', '2697229', '153989', '2023-11-30', 0.09, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435597', 'ap@0456', NULL, NULL, 1, 0.0, 0.090, 0.0, 0.09, 0.0, 'CIG', 1, 'Week4', '3852', 'GPI', 'HYDERABAD BRANCH', 1476.71, 132.9039, 'CIG0005507', 'Stellar Icy Blast 10s', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097763, '5958214', '2697229', '153989', '2023-11-30', 0.35, 0.0, 0.0, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435596', 'ap@0456', NULL, NULL, 1, 0.05, 0.400, 0.0, 0.35, 0.0, 'CIG', 1, 'Week4', '3852', 'GPI', 'HYDERABAD BRANCH', 751.6, 300.64000000000004, 'CIG0002101', 'Originals 64MM', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097762, '5637081', '2697229', '153989', '2023-11-30', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435596', 'ap@0456', NULL, NULL, 1, 0.0, 0.000, 0.0, 0.0, 0.0, 'CIG', 1, 'Week4', '3852', 'GPI', 'HYDERABAD BRANCH', 2027.08, 0.0, 'CIG0005519', 'STELLAR DEFINE SUPER SLIM 20s PACK', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097761, '5531061', '2697229', '153989', '2023-11-30', 6.17, 0.0, 0.0, 0.0, 2.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435595', 'ap@0456', NULL, NULL, 1, 2.01, 8.180, 0.0, 6.17, 0.0, 'CIG', 1, 'Week4', '3812', 'IPM', 'HYDERABAD BRANCH', 3348.98, 27394.6564, 'CIG0002030', 'MARLBORO FINE TOUCH 10s', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097760, '730084', '2697229', '153989', '2023-11-30', 0.68, 0.0, 0.0, 0.0, 0.22, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435594', 'ap@0456', NULL, NULL, 1, 0.22, 0.900, 0.0, 0.68, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6431.67, 5788.503000000001, 'CIG0002001', 'MARLBORO (RED FWD) KS BOX 20', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097759, '2248085', '2697229', '153989', '2023-11-30', 1.04, 0.0, 0.0, 0.0, 0.14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435593', 'ap@0456', NULL, NULL, 1, 0.14, 1.180, 0.0, 1.04, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6697.09, 7902.5662, 'CIG0002051', 'MARLBORO GOLD (3.5 ORIGINAL) KS BOX 20', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097758, '5637080', '2697229', '153989', '2023-11-30', 1.18, 0.0, 0.0, 0.0, 0.38, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435592', 'ap@0456', NULL, NULL, 1, 0.38, 1.560, 0.0, 1.18, 0.0, 'CIG', 1, 'Week4', '3852', 'GPI', 'HYDERABAD BRANCH', 2027.08, 3162.2448, 'CIG0005518', 'STELLAR SHIFT SUPER SLIM 20s PACK', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097757, '6088244', '2697229', '153989', '2023-11-30', 2.78, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435592', 'ap@0456', NULL, NULL, 1, 0.25, 3.030, 0.0, 2.78, 0.0, 'CIG', 1, 'Week4', '4033', 'GPI', 'HYDERABAD BRANCH', 1075.89, 3259.9467, 'CIG0001115', 'FOCUS MINT UP SQ 10s', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097756, '6126376', '2697229', '153989', '2023-11-30', 0.0, 0.0, 0.0, 0.0, 0.06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435591', 'ap@0456', NULL, NULL, 1, 0.06, 0.060, 0.0, 0.0, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6697.09, 401.8254, 'CIG0002037', 'MARLBORO GOLD ADVANCE KS BOX 10 (ST UPG)', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097755, '5198427', '2697229', '153989', '2023-11-30', 5.4, 0.0, 0.0, 0.0, 2.48, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435590', 'ap@0456', NULL, NULL, 1, 2.48, 7.880, 0.0, 5.4, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6101.97, 48083.5236, 'CIG0002021', 'MARLBORO FUSE BEYOND (2.0) KS BOX 20', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097754, '5620057', '2697229', '153989', '2023-11-30', 4.368, 0.0, 0.0, 0.0, 0.816, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435589', 'ap@0456', NULL, NULL, 1, 0.816, 5.184, 0.0, 4.368, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 3805.22, 19726.26048, 'CIG0002033', 'MARLBORO FILTER BLACK -12s PACK', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097753, '5569023', '2697229', '153989', '2023-11-30', 25.57, 10.0, 0.0, 0.0, 8.56, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435588', 'ap@0456', NULL, NULL, 1, 13.56, 49.130, 0.0, 35.57, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 3313.0, 162767.69, 'CIG0002031', 'Marlboro Advance Compact FT 10''s', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097752, '6126375', '2697229', '153989', '2023-11-30', 24.66, 0.0, 0.0, 0.0, 14.56, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435580', 'ap@0456', NULL, NULL, 1, 14.56, 39.220, 0.0, 24.66, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6697.09, 262659.8698, 'CIG0002036', 'MARLBORO GOLD ADVANCE KS BOX 20 (ST UPG)', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);




# INSERT INTO gpil_db.transaction_salesdata
# (id, sku_id, wd_id, town_id, sales_date_time, local_sales_retail, local_sales_dealer, local_sales_modern_trade, local_sales_hawker, outstation_sales_reatil, outstation_sales_dealer, outstation_sales_modern_trade, outstation_sales_hawker, other_sales_retail, other_sales_dealer, other_sales_modern_trade, other_issues_other, other_issues_damage, other_issues_return, transaction_source, created_date, created_by, last_updated_date, last_updated, status, total_outstation_sales, grand_total, total_issue, total_local_sales, total_other_sales, brand_category, freeze_status, transaction_type, cnf_id, company, region, unit_price, value, sku_code, sku_short_name, town_code, wd_name, wd_type, town_name, distrcode, gpi_state, statename, `zone`)
# VALUES(8097752, '6126375', '2697229', '153989', '2023-11-30', 24.66, 0.0, 0.0, 0.0, 14.56, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'SS', '2023-12-04 11:44:28.435580', 'ap@0456', NULL, NULL, 1, 14.56, 39.220, 0.0, 24.66, 0.0, 'CIG', 1, 'Week4', '3852', 'IPM', 'HYDERABAD BRANCH', 6697.09, 262659.8698, 'CIG0002036', 'MARLBORO GOLD ADVANCE KS BOX 20 (ST UPG)', '0492600', 'SOWMYA SRI ENTERPRISES', 'SFA_Lite', 'VIJAYAWADA-0492600', NULL, 'ROS-1040007', 'ROS-1040007', NULL);
