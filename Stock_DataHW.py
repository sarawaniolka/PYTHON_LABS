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
    Closings = [] #list for closing values
    Openings = [] #list for opening values
    for row in csv_file:
        Closings.append(row.split(',')[4]) #add a closing value to the list
        Openings.append(row.split(',')[1]) #add an opening value to the list
    Closings.pop(0) #delete the header from closing values
    Openings.pop(0) #delete the header from opening values
    Closings = [*map(float, Closings)] #change closing values to a float
    Openings = [*map(float, Openings)] #change opening values to a float
    for x in range(0, len(Closings)): #for every row in a file
        Change = str((Closings[x]-Openings[x])/Closings[x]) #calculate the change
        print(Change)










