import os
import sys
import json



def exit_program():
    input("Press Enter to exit...")
    sys.exit(0)

def get_achart_difficulty(achart_dir = ""): #方法：获取谱面难度，返回难度字符串("EZ","HD","IN","AT","Legacy")
    difficulty_list = ["EZ", "HD", "IN", "AT", "Legacy"]
    difficulty = achart_dir.split("\\")[-1].split("_")[1][0:2]
    if difficulty in difficulty_list: #若获取到的难度在预设列表中，则返回该难度，否则抛出错误
        return difficulty
    else:
        difficulty = achart_dir.split("\\")[-1].split("_")[1][0:6]
        if difficulty in difficulty_list:
            return difficulty
        else:
            raise Exception(f"Unknown chart difficulty in chart file name '{achart_dir}'. Maybe it's not a valid chart file.") 


class ChartsDirectory:
    def __init__(self, charts_dir = ""):
        self.charts_dir = charts_dir
        if charts_dir == "":
            self.charts_dir = os.getcwd()
        self.charts_list = []
    
    def get_charts_list(self): #方法：获取目录下所有谱面文件的路径列表，返回列表
        for root, dirs, files in os.walk(self.charts_dir):
            for file in files:
                if "Chart_" in file:
                    self.charts_list.append(os.path.join(root, file))
        if not self.charts_list: #如果没有找到任何谱面文件，则抛出错误
            raise Exception(f"No chart files found in the specified directory '{self.charts_dir}'.")
        return self.charts_list
    
    def charts_directory_check(self): #方法：检查目录是否存在、是否为目录、是否为空，若不满足条件则提示错误并退出程序
        if not os.path.exists(self.charts_dir):
            print(f"Error: The directory '{self.charts_dir}' does not exist!")
            exit_program()
        if not os.path.isdir(self.charts_dir):
            print(f"Error: The directory '{self.charts_dir}' is not a directory!")
            exit_program()
        if not os.listdir(path = self.charts_dir):
            print(f"Error: The directory '{self.charts_dir}' is empty!")
            exit_program()


class aChartSearch:
    def __init__(self, dir = ""):
        self.dir = dir
        self.notes_achart = {"tap":0,"drag":0,"hold":0,"flick":0}
        self.notes_type = {1:"tap",2:"drag",3:"hold",4:"flick"}
        self.notes_total = 0
        self.difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
        self.difficulty = ""
        self.count = 0
    
    def json_search_byeach(self):  #方法：使用JSON解析统计各音符数量,返回各音符数量字典，格式为{"tap":0,"drag":0,"hold":0,"flick":0}
        file = open(self.dir, mode='r', encoding="utf-8") #可能会抛出FileNotFoundError或OSError异常
        res = file.readline()
        res_python = json.loads(res) #可能会抛出json.JSONDecodeError异常
        judgelines = res_python["judgeLineList"] #可能会抛出KeyError异常，如果JSON中没有"judgeLineList"键，则抛出错误，提示可能不是有效的谱面文件
        for judgeline in judgelines:
            for notesAbove in judgeline["notesAbove"]:
                self.notes_achart[self.notes_type[notesAbove["type"]]] += 1
            for notesBelow in judgeline["notesBelow"]:
                self.notes_achart[self.notes_type[notesBelow["type"]]] += 1
        file.close()
        return self.notes_achart
    
    def json_search_bytotal(self):  #方法：使用JSON解析统计总音符数量,返回总音符数量(int)
        file = open(self.dir, mode='r', encoding="utf-8") #可能会抛出FileNotFoundError或OSError异常
        res = file.readline()
        res_python = json.loads(res) #可能会抛出json.JSONDecodeError异常
        judgelines = res_python["judgeLineList"] #可能会抛出KeyError异常，如果JSON中没有"judgeLineList"键，则抛出错误，提示可能不是有效的谱面文件
        for judgeline in judgelines:
            self.notes_total += (len(judgeline["notesAbove"]) + len(judgeline["notesBelow"]))
        file.close()
        return self.notes_total
