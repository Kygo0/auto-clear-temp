import os
import shutil
import subprocess
import time

def open_temp_folder():
    command = 'explorer shell:AppsFolder\\Microsoft.Windows.ShellExperienceHost_cw5n1h2txyewy!App'
    subprocess.Popen(command, shell=True)
    time.sleep(2)  # Wait for the folder to open

# Delete contents in %temp%
def delete_temp_contents():
    temp_path = os.getenv('TEMP')
    for root, dirs, files in os.walk(temp_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path)
            except Exception as e:
                print(f"Error deleting directory {dir_path}: {e}")

# Main script execution
if __name__ == "__main__":
    open_temp_folder()
    delete_temp_contents()
