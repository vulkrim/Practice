#!/usr/bin/python3

from completed import complete
import importlib

qaSheet = [importlib.import_module(i+'.answerKey') for i in complete]
answers = [importlib.import_module(i+'.answer') for i in complete]

if __name__ == '__main__':
    menuKey=0
    print('hello this is a practice Environmet currently ' +str(len(complete))+' questions have been completed you can view the details of the questions in the txt file labled questions. To view the completed questions press 1')
    menuKey = input()
    if menuKey == 1:
        dictMenu = [i for i in complete]
        for i in dictMenu:
            print(str(dictMenu.index(i)) +' ' +i)
        menuKey = input('which would you like to run')
