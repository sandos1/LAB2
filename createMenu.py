"""
precondition: need a list
postcondition: creating a menu 
description:return a numb and menu item
"""


def createMenu(optionList):
    
    tmp = " "
    ct = 0
    for opt in optionList:
        tmp += str(ct)+"." + opt +"\n"
        ct +=1
    return tmp
