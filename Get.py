# -*- coding: utf-8 -*-
import requests
import json
from prettytable import PrettyTable


def getlyrics(sname, status):
    url = "http://musicapi.leanapp.cn/search?keywords=" + sname

    x = PrettyTable(field_names=["id", "歌名", "歌手", "专辑"])
    x.padding_width = 1

    try:
        for i in range(0, 10):
            x.add_row([i + 1,
                       json.loads(requests.get(url).text)["result"]["songs"][i]["name"],
                       json.loads(requests.get(url).text)["result"]["songs"][i]["artists"][0]["name"],
                       json.loads(requests.get(url).text)["result"]["songs"][i]["album"]["name"]])

    except IndexError:
        print("唯一匹配，自动选择")
        sid = str(json.loads(requests.get(url).text)["result"]["songs"][0]["id"])
        print("已定位歌曲，id为" + sid)

    except KeyError:
        print("没有数据，任意键退出")
        input()
        exit()

    else:
        x.align["id"] = "l"
        print(x.get_string())
        index = input("请输入序号（默认为1）:")
        if index == "":
            index = "1"
        sid = str(json.loads(requests.get(url).text)["result"]["songs"][int(index) - 1]["id"])
        print("已定位歌曲，id为" + sid)

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
        # Waiting for commit
    return lyric

