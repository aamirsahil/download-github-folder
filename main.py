import re
import os
import subprocess
import shutil

def run_subprocess(command:str):
    # run the commandline command
    param = command.split(" ")
    subprocess.run(param)

def get_input_data(data):
    data_dict = {}
    for key_value in data:
        key_pattern = r"^(.+)\s:\s.+$"
        key = re.findall(key_pattern, key_value)[0]
        value_pattern = r"^.+\s:\s(.+)\n?$"
        value = re.findall(value_pattern, key_value)[0].split(",")
        data_dict[key] = value
    return data_dict

def main():
    # get input from file
    with open("download_files.txt", "r") as f:
        data = f.readlines()
    
    # extracting data and storing in a dictionary
    data_dict = get_input_data(data)
    
    # download git dir/file
    # make new dir to store the files
    save_dir = "./" + data_dict['save_dir'][0]
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)
        print(f"{save_dir} created")
    
    os.chdir(save_dir)

    git_url = data_dict['git_url'][0]
    run_subprocess(f"git clone --filter=blob:none --no-checkout {git_url}")
    git_repo_dir = ""
    os.chdir(git_repo_dir)
    run_subprocess("git sparse-checkout set --cone")
    run_subprocess("git checkout master")
    # download dir
    for dir in data_dict["dir_to_download"]:
        run_subprocess(f"git sparse-checkout set {dir}")
        shutil.move("./" + dir, "../")
    # delete the downloaded dir
    shutil.rmtree("./")

if __name__ == "__main__":
    main()