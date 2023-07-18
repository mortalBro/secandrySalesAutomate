import os

folder_list=[]
csv_jadugar="/home/tspl/Documents/Script_baz_lol/csv_jadugar"
fileCheck="/home/tspl/Documents/Script_baz_lol/fileCheck"
final_jadugar="/home/tspl/Documents/Script_baz_lol/final_jadugar"
jadugar="/home/tspl/Documents/Script_baz_lol/jadugar"
productionRemark="/home/tspl/Documents/Script_baz_lol/productionRemark"
uatRemark="/home/tspl/Documents/Script_baz_lol/uatRemark"
folder_list.append(csv_jadugar)
folder_list.append(fileCheck)
folder_list.append(final_jadugar)
folder_list.append(jadugar)
folder_list.append(productionRemark)
folder_list.append(uatRemark)

for i in folder_list:
    
    file_names = os.listdir(i)
    for j in file_names:
        file_path=i+"/"+j
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{j}' deleted successfully.")
        else:
            print(f"File '{j}' does not exist.")

