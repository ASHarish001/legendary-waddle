import os
from scrapper import fetch_anime_titles
from natsort import natsorted
# import scrapper

def sanitize_filename(name):
    # Remove or replace characters that are not allowed in filenames
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        name = name.replace(char, '')
    return name

def rename_files_in_directory(directory):
    files = os.listdir(directory)
    files = natsorted(files)
    scraped_titles = fetch_anime_titles("naruto")

    for count, filename in enumerate(files):
        # file_extension = os.path.splitext(filename)[1]
        new_name = f"{count + 1} - {scraped_titles[count]}.mkv"
        new_name = sanitize_filename(new_name).strip()
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} to {new_name}")


directory = r"E:/t"
# rename_files_in_directory(directory)

titles = fetch_anime_titles("dragon ball z")
rename_files_in_directory(directory)