import os
import sys
from pathlib import Path
import re
import time

EXTENTIONS = {
    'images': ('.jpeg', '.png', '.jpg', '.svg', '.dng'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsx', '.pptx', '.djvu', '.rtf'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar'),
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"

TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

def check_files(folder: Path):
    for file in folder.iterdir():

        if file.is_file():
           sort(file)
        if file.is_dir():
            check_files(file)
        if not any(file.iterdir()):
            file.rmdir()
            print(f'{file} deleting')
def sort(file: Path):
    path = Path(file)
    file_suffix = file.suffix.lower()
    
    file_name = file.stem
    zero_station = 0
     
    for key, values in EXTENTIONS.items():
        if file_suffix in values:
            zero_station = key 
    if zero_station != 0: 
        norm_name = normalize(file_name)
        new_file_name = norm_name + file_suffix
        
        end_folder = folder.joinpath(zero_station)

        
        end_folder.mkdir(exist_ok=True)
        new_file_path = end_folder.joinpath(new_file_name) 
        try:
            file.rename(new_file_path)
        except FileExistsError:
            time_stamp = time.time()
            new_file_path = end_folder.joinpath(norm_name + '_' + str(time_stamp) + file_suffix)
            file.rename(new_file_path)
    else:
        norm_name = normalize(file_name)
        new_file_name = norm_name + file_suffix
        
        end_folder = folder.joinpath('another')

        
        end_folder.mkdir(exist_ok=True)
        new_file_path = end_folder.joinpath(new_file_name) 
        try:
            file.rename(new_file_path)
        except FileExistsError:
            time_stamp = time.time()
            new_file_path = end_folder.joinpath(norm_name + '_' + str(time_stamp) + file_suffix)
            file.rename(new_file_path)

def translate():
    for cyril, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cyril)] = latin
        TRANS[ord(cyril.upper())] = latin.upper()

def normalize(file_name: str) -> str:
    result = ""
    
    name =  file_name.split('.')
    global ext 
    ext = name.pop(-1)
    name = '_'.join(name)
    name = name.lower()
    new_name = file_name.translate(TRANS)
    
    
    some = re.findall(r'[a-zA-Z0-9]', new_name)
    
    for littera in name:
        if littera not in some:
            result += '_'
            continue 
        else:
            result += littera
    result =  result + '.' + ext 
    namedir = os.path.dirname(file_name)
    new_filepath = os.path.join(namedir, result)
    
    
    if str(file_name) == str(new_filepath):
        print("| No need changes")
        print("|{}".format("-"*50))
    
    for symvol in new_name:
        if not symvol.isdigit() and not symvol.isalpha() and symvol != '_':
            new_name = new_name.replace(symvol, '_')
    print(result,'Adekvetne imya')
    return new_name
def sorting():
    global folder
    folder = input('Enter path to folders')

    if __name__ == '__main__':
    
        check_files(folder)
        
        print("|{}".format("-"*50))
sorting("C:\Users\romac\Downloads")
#mda