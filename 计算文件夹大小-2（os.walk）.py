# -*- coding: utf-8 -*-
import os

#遍历所有文件，并生成文件的路径名
def get_file_paths(path):
    file_paths = []
    for foldername,subfolders,filenames in os.walk(path):  #使用os.walk()遍历
        for filename in filenames:
            file_paths.append(foldername+'\\'+filename)
    return file_paths

#计算文件夹大小
def get_total_size(path):
    total_size = 0
    for file_path in get_file_paths(path):
        total_size += os.path.getsize(file_path)
    return total_size

path = r'F:\AVG'
get_total_size(path)
    