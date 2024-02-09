from utils import get_modified_time, remove_yesterday_file
import os

directory = "your path here"
os.chdir(directory)

for file in os.listdir():
    created_time = get_modified_time(file)
    yersterday = remove_yesterday_file(file, created_time)
    
    print(f'{file}: {yersterday}')
