import chart_search_lib
import json

print("Phigros Chart Search V1.3.0")
print("Please enter the directory of the charts(Empty input means current directory):", end="")
charts_directory = chart_search_lib.ChartsDirectory(input())
charts_directory.charts_directory_check()
try: #获取目录下所有谱面文件的路径列表，若没有找到任何谱面文件，则抛出错误
    charts_list = charts_directory.get_charts_list()
except Exception as e:
    print(f"Error: {e}")
    chart_search_lib.exit_program()
print("Mode 1:By each notes total")
print("Mode 2:By total notes")
mode = input("Please select mode(Enter number):")
if mode == "1":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    achart_input = chart_search_lib.aChartSearch()
    achart_input.notes_achart["tap"] = int(input("tap:"))
    achart_input.notes_achart["drag"] = int(input("drag:"))
    achart_input.notes_achart["hold"] = int(input("hold:"))
    achart_input.notes_achart["flick"] = int(input("flick:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    count = 0
    print("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :", end="")
    difficulty_num = input()
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Error: Invalid input!")
        chart_search_lib.exit_program()
    else:
        achart_input.difficulty = difficulty_dict[int(difficulty_num)]
        for achart_dir in charts_list:
            achart_search = chart_search_lib.aChartSearch(achart_dir)
            try: #获取谱面难度，若获取到的难度不在预设列表中，则抛出错误
                achart_search.difficulty = chart_search_lib.get_achart_difficulty(achart_dir)
            except Exception as e:
                print(f"Warning: {e} Skipping this chart.")
                continue
            if not achart_input.difficulty == achart_search.difficulty:
                count += 1
                continue
            else:
                try: #使用JSON解析统计各音符数量,若文件无法打开或为非JSON文件或JSON中没有"judgeLineList"键，则抛出错误
                    achart_search.json_search_byeach()
                except Exception as e:
                    if isinstance(e, FileNotFoundError):
                        print(f"Warning: An FileNotFoundError occurred while processing '{achart_dir}', maybe it's not a valid chart file. Skipping this chart.")
                    elif isinstance(e, OSError):
                        print(f"Warning: An OS error occurred while processing '{achart_dir}'. Skipping this chart.")
                    elif isinstance(e, json.JSONDecodeError):
                        print(f"Warning: A JSONDecodeError occurred while processing '{achart_dir}'. Maybe it's not a valid chart file. Skipping this chart.")
                    elif isinstance(e, KeyError):
                        print(f"Warning: A KeyError occurred while processing '{achart_dir}'. The file does not contain 'judgeLineList'. Maybe it's not a valid chart file. Skipping this chart.")
                    continue
                if achart_input.notes_achart == achart_search.notes_achart:
                    ans.append(achart_dir)
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{len(charts_list)} charts...")
elif mode == "2":
    print("Please enter the number of notes which chart you want to search.")
    print("For notes number,you can watch https://www.bilibili.com/video/BV1P1ZsYaEyS/ to find out.")
    achart_input = chart_search_lib.aChartSearch()
    achart_input.notes_total = int(input("Total notes:"))
    ans = []
    difficulty_dict = {1:"EZ",2:"HD",3:"IN",4:"AT",5:"Legacy"}
    count = 0
    print("Please choose the difficulty of the chart(enter number) EZ-1 HD-2 IN-3 AT-4 Legacy-5 :", end="")
    difficulty_num = input()
    if difficulty_num != "1" and difficulty_num != "2" and difficulty_num != "3" and difficulty_num != "4" and difficulty_num != "5":
        print("Error: Invalid input!")
        chart_search_lib.exit_program()
    else:
        achart_input.difficulty = difficulty_dict[int(difficulty_num)]
        for achart_dir in charts_list:
            achart_search = chart_search_lib.aChartSearch(achart_dir)
            try: #获取谱面难度，若获取到的难度不在预设列表中，则抛出错误
                achart_search.difficulty = chart_search_lib.get_achart_difficulty(achart_dir)
            except Exception as e:
                print(f"Warning: {e} Skipping this chart.")
                continue
            if not achart_input.difficulty == achart_search.difficulty:
                count += 1
                continue
            else:
                try: #使用JSON解析统计音符总数,若文件无法打开或JSON中没有"judgeLineList"键，则抛出错误
                    achart_search.json_search_bytotal()
                except Exception as e:
                    if isinstance(e, FileNotFoundError):
                        print(f"Warning: An FileNotFoundError occurred while processing '{achart_dir}', maybe it's not a valid chart file. Skipping this chart.")
                    elif isinstance(e, OSError):
                        print(f"Warning: An OS error occurred while processing '{achart_dir}'. Skipping this chart.")
                    elif isinstance(e, json.JSONDecodeError):
                        print(f"Warning: A JSONDecodeError occurred while processing '{achart_dir}'. Maybe it's not a valid chart file. Skipping this chart.")
                    elif isinstance(e, KeyError):
                        print(f"Warning: A KeyError occurred while processing '{achart_dir}'. The file does not contain 'judgeLineList'. Maybe it's not a valid chart file. Skipping this chart.")
                    continue
                if achart_input.notes_total == achart_search.notes_total:
                    ans.append(achart_dir)
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{len(charts_list)} charts...")
else:
    print("Error: Invalid mode selected!")
    chart_search_lib.exit_program()
print(ans)
chart_search_lib.exit_program()
