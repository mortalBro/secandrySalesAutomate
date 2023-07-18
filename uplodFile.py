
import json
import csv
import requests



def uatUploadUser(path):
    url = "https://uatsecondarysales.godfreyphillips.co:8000/api/v1/master_user_upload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/uatRemark/uatUser.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)


def productionUploadUser(path):
    url = "https://secondarysales.godfreyphillips.co:8000/api/v1/master_user_upload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/productionRemark/productionUser.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)


def uatUploadWdMaster(path):
    url = "https://uatsecondarysales.godfreyphillips.co:8000/api/v1/wd_master_upload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/uatRemark/uatMaster.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)



def productionUploadWdMaster(path):
    url = "https://secondarysales.godfreyphillips.co:8000/api/v1/wd_master_upload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/productionRemark/productionMaster.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)


def uatUploadHier(path):
    url = "https://uatsecondarysales.godfreyphillips.co:8000/api/v1/heirarchy_master_upload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/uatRemark/uat_heirarchy_master_upload.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)


def productionUploadHier(path):
    url = "https://secondarysales.godfreyphillips.co:8000/api/v1/heirarchy_master_upload/"


    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/productionRemark/production_heirarchy_master_upload.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)


def productionUploadMapping(path):
    url = "https://secondarysales.godfreyphillips.co:8000/api/v1/masterwdskucategoryupload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/productionRemark/productionMapping.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)


def uatUploadMapping(path):
    url = "https://uatsecondarysales.godfreyphillips.co:8000/api/v1/masterwdskucategoryupload/"

    payload = {}
    files=[
    ('file',('user.csv',open(path,'rb'),'text/csv'))
    ]
    headers = {
    'Cookie': '5c905=1687946670496-360844997; cf485=1685535234920-305002843; 5c9003=xgZHFCT2gJpE1TTXFTvFSd4EeAcLPsgwzv1fbxqQ6E2V6Lk4rynTYEIdiuEkLUhbs7iYcg22CHqvaGeYArlpGJFH2dKB8saA3azOkPJNVdPv8v+Ofh7++fbgCaX9ow/JSS1yEsakn2TSwq4xiPbiYjRX7KHzdL6qoQpfJXYM3R+ow8qy'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_json = response.json()
    data = response_json["data"]
    output_csv_path = "/home/tspl/Documents/Script_baz_lol/uatRemark/uatMapping.csv"
    fieldnames = data[0].keys()
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created:", output_csv_path)
