import os
import collections
from pprint import pprint

#extension types
ext_audio = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
ext_video = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
ext_imgs = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
ext_docs = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
ext_archive = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
ext_install = ['dmg', 'exe', 'iso']

#create directories where we want to move the files to
base_path = os.path.expanduser('~')
dest_dirs = ['Music', 'Videos', 'Pictures', 'Documents', 'Applications', 'Other']

for d in dest_dirs:
    dir_path = os.path.join(base_path, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

#create a list of files in downloads folder and map based on file extension
downloads_path = os.path.join(base_path, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(downloads_path)

for file_name in files_list:
    file_ext = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)

pprint(files_mapping)

#move all files given a file ext to a target directory

for f_ext, f_list in files_mapping.items():
    
    if f_ext in ext_install:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(base_path, 'Applications', file))

    elif f_ext in ext_audio:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(base_path, 'Music', file))

    elif f_ext in ext_video:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(base_path, 'Videos', file))

    elif f_ext in ext_imgs:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(base_path, 'Pictures', file))

    elif f_ext in ext_docs or f_ext in ext_archive:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(base_path, 'Documents', file))

    else:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(base_path, 'Other', file))


            