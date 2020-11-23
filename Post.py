# -*- coding: utf-8 -*-
import requests
import time


def post(_msg_):
    postData = {
        'color': '16777215',
        'fontsize': '25',
        'mode': '1',
        'msg': _msg_,
        'rnd': str(int(time.time())),
        'roomid': 5210228,  # need data
        'csrf_token': '',  # need data
        'csrf': '',  # need data
        'bubble': '1'
    }
    cookie = {'Cookie': ''''''}  # need data
    sendurl = 'http://api.live.bilibili.com/msg/send'
    requests.post(sendurl, data=postData, cookies=cookie)
