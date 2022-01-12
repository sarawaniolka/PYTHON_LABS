import urllib.request
import os
import csv

path = os.getcwd()

#1.Downloading the file
def download_file(name):
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+name+'?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
    with urllib.request.urlopen(url) as response, open(name + '.csv', 'wb') as out_file:
        out_file.write(response.read())

#2.Finding csv files in directory
def find_csv(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

print(file_name)

for file_name in find_csv(path):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = []
        dict_list = []
        try:
            for row in csv_reader:
                    change = (float(row["Close"]) - float(row["Open"])) / float(row["Open"])
                    change_dict = {"Change": change}
                    row.update(change_dict)
                    headers = list(row.keys())
                    dict_list.append(row)
        except:
            pass

    with open(file_name, mode='w', newline='') as csv_filew:
        writer = 'csv'.DictWriter(csv_filew, fieldnames=headers)
        writer.writeheader()

        for data in dict_list:
            writer.writerow(data)