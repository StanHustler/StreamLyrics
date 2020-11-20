# -*- coding: utf-8 -*-
import requests
import json
from prettytable import PrettyTable

sname = input("请输入歌曲名称:")
url = "http://musicapi.leanapp.cn/search?keywords=" + sname

x = PrettyTable(field_names=["id", "歌名", "歌手", "专辑"])
x.padding_width = 1
for i in range(0, 10):
    x.add_row([i+1,
               json.loads(requests.get(url).text)["result"]["songs"][i]["name"],
               json.loads(requests.get(url).text)["result"]["songs"][i]["artists"][0]["name"],
               json.loads(requests.get(url).text)["result"]["songs"][i]["album"]["name"]])
x.align["id"] = "l"


print(x.get_string())
index = input("请输入序号（默认为1）:")

sid = str(json.loads(requests.get(url).text)["result"]["songs"][int(index)-1]["id"])
print("已定位歌曲，id为"+sid)
status = input("①CN ②原文:")
url = "http://music.163.com/api/song/lyric?os=pc&id="

url += sid

if status == "1":  # cn
    url += "&tv=-1"
    lyric = json.loads(requests.get(url).text)["tlyric"]["lyric"]

elif status == "2":  # orgin
    url += "&lv=-1"
    lyric = json.loads(requests.get(url).text)["lrc"]["lyric"]

else:
    url += "&tv=-1&lv=-1"

file_handle = open(sname + '-' + sid + '.txt', mode='w+')
print("正在写入")
file_handle.write(lyric)
file_handle.close()
print("写入完成")
