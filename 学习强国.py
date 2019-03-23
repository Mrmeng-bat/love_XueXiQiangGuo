#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time  # 用来延时
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #引入Keys类包
import random
import schedule
"""
info:
author:Mrmeng
github:https://github.com/Mrmeng-bat/
update_time:2019-3-24
"""
driver = webdriver.Chrome()  # 选择浏览器，此处我选择的Chrome
driver.get('https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/')
#driver.implicitly_wait (30)#自动休眠30s范围内
input("请先登录，登录完成后回车键继续：")
all_of_link_item = driver.find_elements_by_class_name('word-item')
all_of_picture_item = driver.find_elements_by_class_name('background-img-stretching')#视频链接为
study_text_link = None
def find_study_text_link():      #返回学习时评的元素
    global study_text_link
    open_link = []#open_link[1]为学习时评
    for item in all_of_link_item:
        print("正在遍历所有文字链接。。。。")
        if item.text == "打开":
                open_link.append(item)
                print("发现打开连接。。。")
    study_text_link  = open_link[1]       
    return(open_link[1])
def get_study_text_link():
    return study_text_link

def get_move_link():#返回视频专辑打开元素
    return(all_of_picture_item[2])


def roll_page(y,sleep_time):             #模拟网页下滚操作，sleep time s
    for i in range(0,y,3):
        driver.execute_script("window.scrollTo(0,"+str(i)+");")
    time.sleep(sleep_time)

def close_page():   #关闭最后一个窗口，并把焦点转回倒数第二个
    driver.close()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
def go_to_last_window():
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    
def open_TXT_link_and_close(link):
    get_study_text_link().click ()#打开学习文章目录
    print(link.text)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    all_of_text_item = driver.find_elements_by_class_name('word-item')
    text_list = []
    for item in all_of_text_item:
        if len(item.text) == 10:
            print(item.text)
            text_list.append(item)
    random.shuffle (text_list)
    try:
        for i in range(6):
            text_list[i].click ()
            go_to_last_window()
            roll_page(1300,60)
            close_page()
    except Exception as err:
        print(err)
    close_page()
def open_move_link():
    link = get_move_link()
    link.click ()
    print(link.text)
    go_to_last_window()
    all_of_move_item = driver.find_elements_by_class_name('word-item')
    move_list = []
    for item in all_of_move_item:
        if len(item.text) == 16:
            print(item.text)
            move_list.append(item)
    random.shuffle (move_list)
    try:
        for i in range(6):
            move_list[i].click ()
            go_to_last_window()
            roll_page(500,60)
            close_page()
    except Exception as err:
        print(err)
    close_page()
def job():
    open_TXT_link_and_close(study_text_link)
    open_move_link()
def print_log():
    print("等待任务执行")
if __name__ == '__main__':
    find_study_text_link()
    print("分析完成")
    #job()
    schedule.every().day.at("06:30").do(job)
    schedule.every().minutes.do(print_log)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
