#!/usr/bin/python3
def remove_char_at(str, n):
    cnt = 0
    new_str = ""
    if n < 0:
        return str
    for i in str:
        if n == cnt:
            cnt += 1
            continue
        new_str = new_str + str[cnt]
        cnt += 1
    return new_str
