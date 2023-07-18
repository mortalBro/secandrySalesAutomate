import pandas as pd
def excel_to_csv(rasta,a):
    excel_file_path = rasta
    csv_file_path = "/home/tspl/Documents/Script_baz_lol/csv_jadugar/"+a[:len(a)-4]+"csv"
    data_frame = pd.read_excel(excel_file_path)
    data_frame.to_csv(csv_file_path, index=False)
    print("Conversion from Excel to CSV completed!")
# excel_to_csv("/home/tspl/Documents/Script_baz_lol/WD_SKU_Mapping.xlsx","WD_SKU_Mapping.xlsx")
