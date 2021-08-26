import argparse
import logging
import re
import shutil
import sys
import os
from pathlib import Path

log_format = ('[%(asctime)s] %(levelname)s %(module)s %(lineno)d: %(message)s')
log = logging.getLogger(__name__)

def get_files(target_path, file_pattern):
    #Check if Target path exists
    path_object = Path(target_path)
    if not path_object.is_dir():
        log.error('Invalid Directory!')
        sys.exit(1)
    
    list_files = os.listdir(target_path) #Obtain filenames in target directory
    #Obtain filenames that matched target pattern
    compiled_pattern = re.compile(file_pattern)
    matched_pattern = []
    for item in list_files:
        if compiled_pattern.fullmatch(item):
            matched_pattern.append(item)
    
    #Check if any file mathced the file pattern
    if matched_pattern == []:
        logging.error('No file matched the given pattern')
        sys.exit(1)
    
    log.info(f'Files to be renamed: {matched_pattern}') #Enumerate files to be renamed
    return matched_pattern
    
def rename_file(filename, pattern, target_dir, copy=False, ctr=None):
    extension = os.path.splitext(filename) #Obtain file extension
    new_filename = pattern + ctr + extension[1] #New filename format
    if re.search(pattern, filename): #Check if filename already matches the target pattern
        log.warning(f'Target file: {filename} already has pattern: {pattern}!')
    elif copy:
        shutil.copy(target_dir + filename, target_dir + new_filename)
        log.info(f'{filename} has been renamed and copied as {new_filename} in {target_dir}')
    else:
        os.rename(target_dir + filename, target_dir + new_filename)
        log.info(f'{filename} has been renamed as {new_filename} in {target_dir}')
    
def rename_bulk(file_pattern, new_pattern, target_dir, copy='False'):
    #Check if Copy is either True or False
    if copy != 'True' and copy != 'False':
        log.error('Invalid copy parameter. Must be either True or False!')
        sys.exit(1)
    if copy == 'False':
        copy = False
    
    #Obtain file list
    file_list = get_files(target_dir, file_pattern) 
    file_list.sort()
    
    #Rename Files
    ctr=1
    for item in file_list[0:]:
        rename_file(item, new_pattern, target_dir, copy=bool(copy), ctr=str(ctr))
        ctr += 1
        
def main(args):
    rename_bulk(args.file_pattern, args.new_pattern, args.target_dir, args.copy)
    log.info('Done')
    sys.exit(0)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('new_pattern', help='Filename pattern to replace the target files')
    parser.add_argument('file_pattern', help='Filename pattern of the target files')
    parser.add_argument('target_dir', help='Directory of the files to be renamed')
    parser.add_argument('--log-level', help='Sets the log hierarchy level', default=logging.INFO)
    parser.add_argument('--copy', help='Sets the log hierarchy level', default='False')
    args = parser.parse_args()
    try:
        logging.basicConfig(level=args.log_level, format=log_format)
    except ValueError:
        print('Invalid log heirarchy level!\nValid Arguments: NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL')
        sys.exit(1)
    main(args)
    
    