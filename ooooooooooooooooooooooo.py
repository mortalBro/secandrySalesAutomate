import csv
def zeroInUserLocation(path):
    csv_file_path = path
    output_file_path = "/home/tspl/Documents/Script_baz_lol/fileCheck/userOP.csv"
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        modified_rows = []
        for row in reader:
            location = row['LOCATION']
            if '0' not in location:
                row['LOCATION'] = '0' + location
            modified_rows.append(row)
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(modified_rows)

    print("Processing complete. Modified file saved at:", output_file_path)