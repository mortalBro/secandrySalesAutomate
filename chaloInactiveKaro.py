import os
from converter_xlsx_to_csv import excel_to_csvINACTIVE
from replacement_of_header import moveFileIfNotExcelInactive
from uplodFile import uatUploadHier,uatInactive,productionInactive
from uplodFile import productionUploadHier



pa="/home/tspl/Documents/Script_baz_lol/inactiveSTARTCSV/"
folder_path = "/home/tspl/Documents/Script_baz_lol/inactiveSTART"
mapping_file=["WD_SKU_M","Add_WD_S","wd_sku_m","wd_sku_m","Add_WD_S"]
# "kbze tvwu ogcf zdwk" 
print("Dddd")
file_names = os.listdir(folder_path)
for i in file_names:
    if i.startswith(".~lock."):
        file_names.remove(i)


for file_name in file_names:
    if((file_name[-1:-4:-1][::-1])!="csv"):
        print("JJJ")
        excel_to_csvINACTIVE("/home/tspl/Documents/Script_baz_lol/inactiveSTART/"+file_name,file_name)
        outputPath= "/home/tspl/Documents/Script_baz_lol/inactiveSTARTCSV/inactive.csv"
        uatInactive(outputPath)
        productionInactive(outputPath)
    else:
        print("csjx")
        moveFileIfNotExcelInactive("inactiveSTART/"+file_name,file_name)
        outputPath= "/home/tspl/Documents/Script_baz_lol/inactiveSTARTCSV/inactive.csv"
        uatInactive(outputPath)
        productionInactive(outputPath)
