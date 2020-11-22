# -*- coding: utf-8 -*-

def out(_oname_, lyric):
    file_handle = open(_oname_, mode='w+')
    print("正在写入")
    file_handle.write(lyric)
    file_handle.close()
    print("写入完成")
