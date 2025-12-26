import os
import sys
import json


def chart_mode1(name):  #方法1：暴力遍历统计各音符数量，返回各音符数量列表，格式为[tap,drag,hold,flick]
    file = open(name,mode='r',encoding="utf-8")
    res = file.readline()
    notes_chart = [0,0,0,0]
    n = len(res)
    for i in range(n-7):
        if res[i:i+6:] == '"type"':
            j = int(res[i+7])
            notes_chart[j-1] += 1
    file.close()
    return notes_chart


def chart_mode2(name):  #方法2：暴力遍历统计总音符数量,返回总音符数量(int)
    file = open(name,mode='r',encoding="utf-8")
    res = file.readline()
    notes_chart = 0
    n = len(res)
    for i in range(n-7):
        if res[i:i+6:] == '"type"':
            notes_chart += 1
    file.close()
    return notes_chart


def chart_mode3(name):  #方法3：使用JSON解析统计总音符数量,返回总音符数量(int)
    file = open(name,mode='r',encoding="utf-8")
    res = file.readline()
    notes_chart = 0
    res_python = json.loads(res)
    judgelines = res_python["judgeLineList"]
    for judgeline in judgelines:
        notes_chart += (len(judgeline["notesAbove"]) + len(judgeline["notesBelow"]))
    file.close()
    return notes_chart


def chart_mode4(name):  #方法4：使用JSON解析统计各音符数量,返回各音符数量列表，格式为[tap,drag,hold,flick]
    file = open(name,mode='r',encoding="utf-8")
    res = file.readline()
    notes_chart = [0,0,0,0]
    res_python = json.loads(res)
    judgelines = res_python["judgeLineList"]
    for judgeline in judgelines:
        for notesAbove in judgeline["notesAbove"]:
            notes_chart[notesAbove["type"]-1] += 1
        for notesBelow in judgeline["notesBelow"]:
            notes_chart[notesBelow["type"]-1] += 1
    file.close()
    return notes_chart


print("Phigros Chart Search V1.2.2")
charts_directory = input("Please enter the directory of the charts(Empty input means current directory):")
if charts_directory == "":
    charts_directory = os.getcwd()
if not os.path.exists(charts_directory):
    print("The directory you entered does not exist!")
    toexit = input("Press Enter to exit...")
    sys.exit(0)
if not os.path.isdir(charts_directory):
    print("The directory you entered is not a directory!")
    toexit = input("Press Enter to exit...")
    sys.exit(0)
if not os.listdir(path = charts_directory):
    print("The directory you entered is empty!")
    toexit = input("Press Enter to exit...")
    sys.exit(0)
print("Mode 1:By each notes total")
print("Mode 2:By total notes")
print("Mode 3:By total notes(Using JSON parsing)(Recommended)")
print("Mode 4:By each notes total(Using JSON parsing)(Recommended)")
mode = input("Please select mode:")
if mode == "1":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    tap = int(input("tap:"))
    drag = int(input("drag:"))
    hold = int(input("hold:"))
    flick = int(input("flick:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    notes_input = [tap,drag,hold,flick]
    count = 0
    difficulty_num = input("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :")
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Your input is wrong!")
    else:
        difficulty = difficulty_dict[int(difficulty_num)]
        print("Please wait...(maybe more than 10 minutes)")
        list = os.listdir(path = charts_directory)
        for i in list:
            charts_directory_one = charts_directory + "\\" + i
            if os.path.isfile(charts_directory_one) == False: #判断是否为文件，若为文件夹则跳过当前循环
                continue
            if difficulty in i:
                notes_true = chart_mode1(charts_directory_one)
                if notes_input == notes_true:
                    ans.append(i)
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{len(list)} charts...")
        print(ans)
elif mode == "2":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    notes_input = int(input("Total notes:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    count = 0
    difficulty_num = input("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :")
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Your input is wrong!")
    else:
        print("Please wait...(maybe more than 10 minutes)")
        difficulty = difficulty_dict[int(difficulty_num)]
        list = os.listdir(path = charts_directory)
        for i in list:
            charts_directory_one = charts_directory + "\\" + i
            if os.path.isfile(charts_directory_one) == False:  #判断是否为文件，若为文件夹则跳过当前循环
                continue
            if difficulty in i:
                notes_true = chart_mode2(charts_directory_one)
                if notes_input == notes_true:
                    ans.append(i)
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{len(list)} charts...")
        print(ans)
elif mode == "3":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    notes_input = int(input("Total notes:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    count = 0
    difficulty_num = input("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :")
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Your input is wrong!")
    else:
        print("Please wait...(maybe more than 1 minutes)")
        difficulty = difficulty_dict[int(difficulty_num)]
        list = os.listdir(path = charts_directory)
        for i in list:
            charts_directory_one = charts_directory + "\\" + i
            if os.path.isfile(charts_directory_one) == False:  #判断是否为文件，若为文件夹则跳过当前循环
                continue
            if difficulty in i:
                notes_true = chart_mode3(charts_directory_one)
                if notes_input == notes_true:
                    ans.append(i)
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{len(list)} charts...")
        print(ans)
elif mode == "4":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    tap = int(input("tap:"))
    drag = int(input("drag:"))
    hold = int(input("hold:"))
    flick = int(input("flick:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    notes_input = [tap,drag,hold,flick]
    count = 0
    difficulty_num = input("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :")
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Your input is wrong!")
    else:
        difficulty = difficulty_dict[int(difficulty_num)]
        print("Please wait...(maybe more than 1 minutes)")
        list = os.listdir(path = charts_directory)
        for i in list:
            charts_directory_one = charts_directory + "\\" + i
            if os.path.isfile(charts_directory_one) == False:  #判断是否为文件，若为文件夹则跳过当前循环
                continue
            if difficulty in i:
                notes_true = chart_mode4(charts_directory_one)
                if notes_input == notes_true:
                    ans.append(i)
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{len(list)} charts...")
        print(ans)
else:
    print("Your input is error!")
toexit = input("Press Enter to exit...")
sys.exit(0)