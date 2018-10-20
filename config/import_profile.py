from selenium import webdriver

import os
import sys
import threading
import time
import pytz
tz = pytz.timezone('Asia/Shanghai')
import datetime
sys.path.append("/Users/wangzhen/project/learning/python/jokes/jokes")

'''
这个脚本用于，新建一个Django项目之后，对于数据库进行其他操作
所以这里是个baidu.settings,因为我之前创建了一个叫做baidu的app
'''
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jokes.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jokes.settings")

import django
from django.db.models import Count
from django.db.models import QuerySet
import uuid
from django.contrib.auth.hashers import make_password, check_password
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

def import_profile_data(profile):

    for query_index in range(1,67325):
        print(query_index)
        user_id = query_index
        item = profile(user_id = query_index)
        item.save()





def main():

    from django.contrib.auth.models import User
    from bootcamp.authentication.models import Profile
    import_profile_data(Profile)

if __name__ == "__main__":
    main()





