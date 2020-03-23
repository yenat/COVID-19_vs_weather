"""
 Python Script:
  Combine/Merge multiple CSV files using the Pandas library
"""
from os import chdir
from glob import glob
import pandas as pd

# Produce a single CSV after combining all files
def produceOneCSV(list_of_files, file_out):
   # Consolidate all CSV files into one object
   result_obj = pd.concat([pd.read_csv(file) for file in list_of_files])
   # Convert the above object into a csv file and export
   result_obj.to_csv(file_out, index=False, encoding="utf-8")

# Move to the path that holds our CSV files
#csv_file_path = 'c:/temp/csv_dir/'
csv_file_path = '/home/bitseat/COVID-19_vs_weather/all_countries_weather_jan_mar/'
chdir(csv_file_path)

# List all CSV files in the working dir
file_pattern = ".csv"
list_of_files = [file for file in glob('*.{}'.format(file_pattern))]
print(list_of_files)

file_out = "ConsolidateOutput.csv"
produceOneCSV(list_of_files, file_out)