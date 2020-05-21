import time
import pandas as pd
from Data_processing import clean_data, process_data, concatenate, geo_code

start = time.time()
start_year = 2015
end_year = 2019

source_extension = '.txt'
destination_extension = '.csv'

# Should be modified with relative paths
root_source_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Brut/valeursfoncieres-'
root_cleaned_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Temp/cleaned_'
root_geocoded_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Temp/geocoded_'
root_processed_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Temp/processed_'

destination_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Processed/Destination_' + str(start_year) + '_' + str(end_year) + destination_extension


# I create a list of dict of paths for each type of file (source, cleaned and processed) and each year
paths_list = []

for year in range(start_year, end_year+1):
    paths_list.append(
        {"year" : year,
        "source_path": root_source_path + str(year) + source_extension,
        "cleaned_path": root_cleaned_path + str(year) + destination_extension,
        "geocoded_path": root_geocoded_path + str(year) + destination_extension,
        "processed_path": root_processed_path + str(year) + destination_extension}
    )

adresses_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Brut/adresses-france.csv'

# I iterate over the lists of paths and process the data using the diffrent functions (clean, process, consolidate) imported from Data_processing.py

# First we clean the data using the function clean_data
for path in paths_list:
    clean_data(path['source_path'], path['cleaned_path'])
print("Cleaning completed in ", int(time.time() - start), " sec")

# And we add geolocation information to our dataset
# for path in paths_list:
#     geo_code(path['cleaned_path'], path['geocoded_path'])
# print("Geolocation completed in ", int(time.time() - start), " sec")

# Then we process and transform the data using the function process_data
# for path in paths_list:
#     process_data(path['geocoded_path'], path['processed_path'])
# print("Processing completed in ", int(time.time() - start), " sec")

# And finally concatenat the diffrent files (one file per year) into one global file
concatenate(paths_list, destination_path)
print("Concatenation completed in ", int(time.time() - start), " sec")


duration = int(time.time() - start)

# print('len(df) = ', len(df))
print(duration, ' sec')