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


pa="/home/tspl/Documents/Script_baz_lol/csv_jadugar/"
folder_path = "/home/tspl/Documents/Script_baz_lol/jadugar"
mapping_file=["WD_SKU_M","Add_WD_S","wd_sku_m","wd_sku_m","Add_WD_S","ADD WD_S","WD SKU M","Wd_SKU_M"]
useR=False
uMaster=False
uHier=False
uMap=False
n=4

# #Uncommet if you have mapping and hererchy7 only
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
