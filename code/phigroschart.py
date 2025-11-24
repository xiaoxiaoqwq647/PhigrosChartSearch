import os
import sys

def chart_mode1(name):
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


def chart_mode2(name):
    file = open(name,mode='r',encoding="utf-8")
    res = file.readline()
    notes_chart = 0
    n = len(res)
    for i in range(n-7):
        if res[i:i+6:] == '"type"':
            notes_chart += 1
    file.close()
    return notes_chart


print("Phigros Chart Search V1.0")
charts_directory = input("Please enter the directory of the charts(Empty input means current directory):")
print("Mode 1:By each notes total")
print("Mode 2:By total notes")
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
    difficulty_num = input("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :")
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Your input is wrong!")
    else:
        difficulty = difficulty_dict[int(difficulty_num)]
        print("Please wait...(maybe more than 10 minutes)")
        list = os.listdir(path = charts_directory)
        for i in list:
            if difficulty in i:
                charts_directory_one = charts_directory + "\\" + i
                notes_true = chart_mode1(charts_directory_one)
                if notes_input == notes_true:
                    ans.append(i)
        print(ans)
elif mode == "2":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    notes_input = int(input("Total notes:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    difficulty_num = input("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :")
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Your input is wrong!")
    else:
        print("Please wait...(maybe more than 10 minutes)")
        difficulty = difficulty_dict[int(difficulty_num)]
        list = os.listdir(path = charts_directory)
        for i in list:
            if difficulty in i:
                charts_directory_one = charts_directory + "\\" + i
                notes_true = chart_mode2(charts_directory_one)
                if notes_input == notes_true:
                    ans.append(i)
        print(ans)
else:
    print("Your input is error!")
toexit = input("Press Enter to exit...")
sys.exit(0)