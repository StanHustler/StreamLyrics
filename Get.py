# -*- coding: utf-8 -*-

import requests
import json

sid = input("请输入歌曲ID:")
status = input("请输入status:")
# url = "http://music.163.com/api/song/lyric?os=pc&id="
url = "http://music.163.com/api/song/lyric?os=pc&id=1488270927&tv=-1"
url += sid
if status == "1":
    url += "&tv=-1"
elif status == "2":
    url += "&tv=-1"
else:
    url += "&tv=-1&lv=-1"

lyric = json.loads(requests.get(url).text)["lrc"]["lyric"]
print(lyric)