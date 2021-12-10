import urllib.request
import os
from os import listdir

dir_name = os.getcwd()

# 1. Downloading the files
url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1607611052&period2=1639147052&interval=1d' \
      '&events=history&includeAdjustedClose=true '
with urllib.request.urlopen(url) as response, open("GOOG.csv", 'wb') as out_file:
    data = response.read()  # a `bytes` object
    out_file.write(data)

url = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607611129&period2=1639147129&interval=1d' \
      '&events=history&includeAdjustedClose=true '
with urllib.request.urlopen(url) as response, open("IBM.csv", 'wb') as out_file:
    data = response.read()  # a `bytes` object
    out_file.write(data)

url = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1607611176&period2=1639147176&interval=1d' \
      '&events=history&includeAdjustedClose=true '
with urllib.request.urlopen(url) as response, open("MSFT.csv", 'wb') as out_file:
    data = response.read()  # a `bytes` object
    out_file.write(data)


# 2. Searching for .csv files
def find_csv(path_to_dir, suffix=".csv"):
    filenames = listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]


print(find_csv(dir_name))

# 3. Calculating the percentage change between Close and Open price and
# adding these values as another column to this CSV file.

for file in find_csv(dir_name):
    csv_file = open(file)
    for row in csv_file:
        Closings = row.split(',')[4]



