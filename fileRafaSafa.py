import os
import pandas as pd

folder_list=[]
csv_jadugar="/home/tspl/Documents/Script_baz_lol/csv_jadugar"
fileCheck="/home/tspl/Documents/Script_baz_lol/fileCheck"
final_jadugar="/home/tspl/Documents/Script_baz_lol/final_jadugar"
jadugar="/home/tspl/Documents/Script_baz_lol/jadugar"
productionRemark="/home/tspl/Documents/Script_baz_lol/productionRemark"
uatRemark="/home/tspl/Documents/Script_baz_lol/uatRemark"

inactiveSTART="/home/tspl/Documents/Script_baz_lol/inactiveSTART"
inactiveSTARTCSV="/home/tspl/Documents/Script_baz_lol/inactiveSTARTCSV"
prodInactiveRemark="/home/tspl/Documents/Script_baz_lol/prodInactiveRemark"
uatInactiveRemark="/home/tspl/Documents/Script_baz_lol/uatInactiveRemark"

loginRepAttendance="/home/tspl/Documents/Script_baz_lol/loginReportCal"
panmapping = "/home/tspl/Documents/Script_baz_lol/panmapping"

folder_list.append(loginRepAttendance)
folder_list.append(panmapping)
folder_list.append(csv_jadugar)
folder_list.append(fileCheck)
folder_list.append(final_jadugar)
folder_list.append(jadugar)
folder_list.append(productionRemark)
folder_list.append(uatRemark)

folder_list.append(inactiveSTART)
folder_list.append(inactiveSTARTCSV)
folder_list.append(prodInactiveRemark)
folder_list.append(uatInactiveRemark)

for i in folder_list:
    
    file_names = os.listdir(i)
    for j in file_names:
        file_path=i+"/"+j
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{j}' deleted successfully.")
        else:
            print(f"File '{j}' does not exist.")

def sawakshBharat():
    folder_list=[]
    csv_jadugar="/home/tspl/Documents/Script_baz_lol/csv_jadugar"
    fileCheck="/home/tspl/Documents/Script_baz_lol/fileCheck"
    final_jadugar="/home/tspl/Documents/Script_baz_lol/final_jadugar"
    jadugar="/home/tspl/Documents/Script_baz_lol/jadugar"
    productionRemark="/home/tspl/Documents/Script_baz_lol/productionRemark"
    uatRemark="/home/tspl/Documents/Script_baz_lol/uatRemark"

    inactiveSTART="/home/tspl/Documents/Script_baz_lol/inactiveSTART"
    inactiveSTARTCSV="/home/tspl/Documents/Script_baz_lol/inactiveSTARTCSV"
    prodInactiveRemark="/home/tspl/Documents/Script_baz_lol/prodInactiveRemark"
    uatInactiveRemark="/home/tspl/Documents/Script_baz_lol/uatInactiveRemark"

    loginRepAttendance="/home/tspl/Documents/Script_baz_lol/loginReportCal"
    panmapping = "/home/tspl/Documents/Script_baz_lol/panmapping"

    folder_list.append(loginRepAttendance)
    folder_list.append(panmapping)
    folder_list.append(csv_jadugar)
    folder_list.append(fileCheck)
    folder_list.append(final_jadugar)
    folder_list.append(jadugar)
    folder_list.append(productionRemark)
    folder_list.append(uatRemark)

    folder_list.append(inactiveSTART)
    folder_list.append(inactiveSTARTCSV)
    folder_list.append(prodInactiveRemark)
    folder_list.append(uatInactiveRemark)

    for i in folder_list:
        
        file_names = os.listdir(i)
        for j in file_names:
            file_path=i+"/"+j
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{j}' deleted successfully.")
            else:
                print(f"File '{j}' does not exist.")

sawakshBharat()
