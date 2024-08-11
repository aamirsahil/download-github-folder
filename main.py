import re
import os

def main():
    # get input from file
    with open("download_files.txt", "r") as f:
        data = f.readlines()
    
    # extracting data and storing in a dictionary
    data_dict = {}
    for key_value in data:
        key_pattern = r"^(.+)\s:\s.+$"
        key = re.findall(key_pattern, key_value)[0]
        value_pattern = r"^.+\s:\s(.+)\n?$"
        value = re.findall(value_pattern, key_value)[0].split(",")
        data_dict[key] = value
    # download git dir/file
    # make new dir to store the files
    if not os.path.isdir(data_dict['save_dir'][0]):
        os.mkdir('./' + data_dict['save_dir'][0])
        print(f"./{data_dict['save_dir'][0]} created")
    
    print(data_dict)
    # move downloaded dir/file to required location
    # delete the downloaded dir

if __name__ == "__main__":
    main()