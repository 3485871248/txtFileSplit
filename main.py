import json
import os
import math

settingsDict = {}
HELPTEXT = ["帮助：", "将文件拖入此程序并回车开始分割", "打开本目录下的conifg.json文件调整设置"]

print("警告，第一次使用请先关闭程序，调整本目录下的'config.json'，后使用此程序")

if os.path.isfile("./config.json"):  # 读取与输出配置文件
    readConfig = open("./config.json", "r")

    settingsDict = json.load(readConfig)
    readConfig.close()
else:
    writeConfig = open("./config.json", "w")
    settingsDict = {'rows/oneFile': '100', 'startLine': '0', 'encoding': 'utf-8'}

    writeConfig.write(json.dumps(settingsDict))
    writeConfig.close()


def split(filepath):  # 分割函数
    readfile = open(filepath, "r", encoding=settingsDict['encoding'])
    lines = readfile.readlines()
    readfile.close()
    linenum = int(settingsDict['startLine'])

    if os.path.isfile('./out'):
        os.makedirs('./out')

    for o in range(math.ceil(len(lines) / int(settingsDict['rows/oneFile']))):
        outtext = ""
        for p in range(int(settingsDict['rows/oneFile'])):
            outtext += lines[linenum]
            linenum += 1
        write = open("./out/" + str(o) + ".txt", "w", encoding=settingsDict['encoding'])
        write.write(outtext)
        write.close()


while True:
    command = input("")

    if command == "help":  # 帮助
        for i in HELPTEXT:
            print(i)

    else:
        if os.path.isfile(command):  # 分割
            split(command)
            input("完成")
            exit()
        else:
            print("文件路径错误")
