import urllib.request
import os

dir_name = os.getcwd()

#Downloading the file
def download_file(name):
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+name+'?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
    with urllib.request.urlopen(url) as response, open(name + '.csv', 'wb') as out_file:
        out_file.write(response.read())

#Finding csv files in directory
def find_csv(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

#Calculating the change value and adding to data
def calculate_change(file):
    out_data = []
    with open(file, 'r') as f:
        rows = f.readlines()
        headers = rows.pop(0)
        out_data.append(headers.strip().split(',') + ['Change'])
    for row in rows:
        indata = row.strip().split(',')
        opening = float(indata[1])
        closing = float(indata[4])
        change = (closing - opening)/closing
        out_data.append(indata + [str(change)])
    return out_data

#Writing the file
def save_file(file,data):
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        for x in data:
            f.write(','.join(x) + '\n')


#Calling functions
if __name__ == '__main__':
    files = ['GOOG','IBM', 'MSFT']
    for z in files:
        download_file(z)
    for file in find_csv(dir_name):
        save_file(file, calculate_change(file))
