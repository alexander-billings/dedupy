#!/usr/bin/python3
import os, hashlib

# Currently errors on denied permissions
def hash_files(path):
    '''Returns an MD5 hash for all files in a given path.'''

    hasher = hashlib.md5()

    if path == None:
        return "No path given"
    elif os.path.isdir(path) == False:
        return "Invalid path"

    path_list = []
    symlink_list = []
    problem_list = []
    file_hash_dict = {}
    files = os.listdir(path)

    for file in files:

        full_path = os.path.join(path, file)
        
        if os.path.islink(full_path):
            symlink_list.append(full_path)
        elif os.path.isdir(full_path):
            path_list.append(full_path)
        elif not os.path.isdir(full_path):
            with open(full_path, 'rb') as prehash_file:
                buffer = prehash_file.read()
                hasher.update(buffer)
            file_hash_dict.update({full_path: hasher.hexdigest()})
        else:
            problem_list.append(full_path)

    for file_path, file_hash in file_hash_dict.items():
        print("{} is the hash of {}".format(file_hash, file_path))

    for path in path_list:
        hash_files(path)

    return file_hash_dict

def main(arg):
    #if arg[1] == '-h' or arg[1] == '--help' or len(arg) > 2:
    if not len(arg) == 2:
        return print("dedupy.py will hash all the files in a given path and subpaths")
    result = hash_files(arg[1])
    print(result)

if __name__ == '__main__':
  main(os.sys.argv)