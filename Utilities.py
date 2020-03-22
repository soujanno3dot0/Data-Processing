# -*- coding: utf-8 -*-
"""
Generic utility functions ...

"""




def addToList(message, lst_msg): # Message, Message List
    """
    addToList(): Appends the formatted messages to the Message List
    
    Args: 
        message(str): Message
        lst_msg(list) - list where message to be added
        
    """
    lst_msg.append(message)

   
    
    
import pandas as pd
    
def writeToCsv(msgList, packagePath, fileName):
    """
    writeToCsv:Exports Message List in to csv file. The function will create the file 
                if not already created
    
    Args: 
        msgList(list): Message List
        packagePath(str) - Path where file should be created
        fileName(str) - Name of the file
    
    """
    df = pd.DataFrame(msgList)
    filePath = packagePath + '\\' + fileName
    df.to_csv (filePath, index = False, header=True)




import os

def obtainValidFiles(packagePath, validFileList):
    """
    obtainValidFiles(): Retrieves valid .xml file list from the specified Folder path
    
    Args: 
        packagePath(str): vaid location path
        validFileList(list): valid File (Object) types
        
    Returns: array of file names (full path)
    
    """
    directory = packagePath
    
    fileArray = []
    for filename in os.listdir(directory):
        if filename.endswith(".xml") and filename.startswith(validFileList) :
            fileArray.append(directory+"/"+filename)
            continue
        else:
            continue
    return fileArray




import re

def findStringByRegex(pattern, text):
    """
    findStringByRegex() finds the text based on the regex pattern in the text
    
    Args:
        
    pattern(str): regular expression
    text(str): text that contains the pattern
            
    Returns(str): text pattern if found, '' otherwise
    
    """
    x = re.search(pattern, text)
    if(x):
        return x.group()
    else:
        return ''


def splitString(separator, text):
    """
    splitString() splits the text based on the separator passed as arg
    
    Args:
        
    separator(str): separator pattern
    text(str): text that contains the pattern
            
    Returns(list): split list
    
    """
    x = re.split(separator, text)
    if(x):
        return x
    else:
        return ''
