#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import datetime
import os
import random

def modify():
    file = open('zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()

def add():
    subprocess.call('git add .',shell=True)

def commit():
   subprocess.call('git commit -m "modify code"', shell=True)

def set_sys_time(year, month, day):
    os.system('date -s %04d%02d%02d' % (year, month, day))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    add()
    commit()

def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        if(random.randint(1,10) > 7):
            trick_commit(cur_date.year, cur_date.month, cur_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2015, 6, 5), datetime.date(2017, 8, 6))
