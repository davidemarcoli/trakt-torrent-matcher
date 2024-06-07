import os
import time

from trakt import get_collections
from RTN.parser import parse, title_match

torrent_folder = "/mnt/zurg/__all__"

start_time_collections = time.time()
collected_items = get_collections()
end_time_collections = time.time()
print(f"Time to get collections: {end_time_collections - start_time_collections} seconds")

parsed_files = []

start_time_parsing = time.time()
# Loop through all subfolders in the torrent_folder
for root, dirs, files in os.walk(torrent_folder):
    for name in dirs:
        subfolder_path = os.path.join(root, name)
        #print(f"Processing subfolder: {subfolder_path}")
        # Loop through all files in the current subfolder
        for file in os.listdir(subfolder_path):
            #print(f"File: {file}")
            parsed_files.append(parse(file))
end_time_parsing = time.time()
print(f"Time to list and parse files: {end_time_parsing - start_time_parsing} seconds")

start_time_comparison = time.time()
for item in collected_items:
    for parsed_file in parsed_files:
        if title_match(item['title'], parsed_file.parsed_title):
            print(f"Found: {item['title']} in library!")
end_time_comparison = time.time()
print(f"Time for comparison: {end_time_comparison - start_time_comparison} seconds")
