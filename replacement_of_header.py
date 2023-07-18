import csv
import shutil

def moveFileIfNotExcel(a,b):
    source_file_path = a
    destination_file_path = "/home/tspl/Documents/Script_baz_lol/csv_jadugar/"+b
    shutil.move(source_file_path, destination_file_path)


def headerChangeMapping(path):
    mapping=["SKU_CODE","WD_TOWN_ID","SKU_ID","ACTIVE_FLAG","MAX(B.UNIT_PRICE)","CNF_NAME","CNF_ID","WD_ID","TOWN","REGION"]

    csv_file_path = path

    output_file_path = "/home/tspl/Documents/Script_baz_lol/fileCheck/mapping.csv"
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = mapping
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")


def headerChangeMaster_user(path):
    master_user=["USER_ID","NAME","LOCATION","USER_TYPE"]			
    csv_file_path = path
    output_file_path = "/home/tspl/Documents/Script_baz_lol/final_jadugar/user.csv"
    data = []
    print("Gggggggggggggggg")
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = master_user
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")


def headerChangeWd_master(path):		
    wd_master=["WD_ID","WD_NAME","WD_ADDRESS1","WD_ADDRESS2","TOWN","WD_POSTAL_CODE","WD_STATE","WD_COUNTRY_ID","WD_TYPE"]

    csv_file_path = path
    output_file_path = "/home/tspl/Documents/Script_baz_lol/fileCheck/master.csv"
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = wd_master
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")


def headerChangeHierrachy(path):
    hierrachy=["WD_ID","WD_TOWN_ID","REGION_CODE","REGION","TOWN","TOWN_CODE","SKU_CATEGORY_CODE",'WD_TOWN_CODE']

    csv_file_path =path
    output_file_path = "/home/tspl/Documents/Script_baz_lol/final_jadugar/her.csv"
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = hierrachy
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")
