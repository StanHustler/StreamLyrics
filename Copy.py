# -*- coding: utf-8 -*-
import win32con
import win32clipboard as w


def readtxt():

    w.OpenClipboard()
    b = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return b


def inputtxt(_string):
    w.OpenClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, _string)
    w.CloseClipboard()
