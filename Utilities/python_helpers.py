#!/usr/bin/python3

def append_item_or_list_to_list(to_append, _list):
    if type(to_append) == list:
        _list += to_append
    else:
        _list.append(to_append)
