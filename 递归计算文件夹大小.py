# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

#获取文件夹内每个子文件/子文件夹的路径，并以列表存储
def get_file_path(dir_path):
    file_path_list = []
    for file_name in os.listdir(dir_path):    #获取子文件/子文件夹名
        file_path = dir_path + '\\' + file_name    #组成子文件/子文件夹的绝对路径
        file_path_list.append(file_path)    #塞入列表中
    return file_path_list


#统计文件夹内子文件的大小总和(深度为1，不包括子文件夹)
def count_file_size(dir_path):
    size = 0
    for file_path in get_file_path(dir_path):    #循环调取每个子文件路径
        if os.path.isfile(file_path):    #判断是否为文件（忽略文件夹）
            size += os.path.getsize(file_path)    #统计文件大小
    return size
    

#统计文件夹内子文件夹的个数
def count_subdir(dir_path):
    count = 0
    for file_path in get_file_path(dir_path):    #循环调取每个子文件夹路径
        if os.path.isdir(file_path):    #判断是否为文件夹
            count += 1    #统计子文件夹的个数
    return count
        

#递归统计文件夹大小     
def get_dir_size(path,dir_size=0):
    if count_subdir(path) == 0:    #判断有无子文件夹（递归终点）
        dir_size += count_file_size(path)
        return dir_size    #没有子文件夹直接返回该文件夹的大小
    else:
        dir_size += count_file_size(path)    #先计算子文件的大小（不含子文件夹）
        for file_path in get_file_path(path):    #循环计算每个每个子文件夹的大小  
            if os.path.isdir(file_path):  
                dir_size += get_dir_size(file_path)    #递归计算文件大小
        return dir_size

#使用
path = r'F:\\AVG'
get_dir_size(path)
    