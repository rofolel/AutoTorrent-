#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging
import logging.handlers
import os
import time
BYEL = "\033[1;33m"
EOC  = "\033[0m"
MAX_LEN = 20
clevel = {"DEBUG"    :  ("\033[0;35m","\033[1;35m"),
          "INFO"     :  ("\033[0;36m","\033[1;36m"),
          "WARNING"  :  ("\033[0;31m","\033[1;31m"),
          "CRITICAL" :  ("\033[0;31m","\033[1;31m"),
          "ERROR"    :  ("\033[0;31m","\033[1;31m"),
          }
active_loggers = list()

def get_log(name,level = logging.DEBUG):
    global active_loggers
    mylog = logging.getLogger(name)
    active_loggers.append(mylog)
    mylog.setLevel(level)
    if len(mylog.handlers) != 0:
        return mylog 
    
    #handler = logging.handlers.RotatingFileHandler("debug.log")
    #mylog.addHandler(handler)
    
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = myFormatter()
    ch.setFormatter(formatter)
    
    mylog.addHandler(ch)
    
    return mylog

def set_log(level):
    global active_loggers
    print (active_loggers)
    for ll in active_loggers:
        ll.setLevel(level)

class myFormatter(logging.Formatter):
    
    def __init__(self):
        logging.Formatter.__init__(self)
        
    def formatTime(self):
        return time.strftime("%H:%M.%S")
    
    def getCFL(self,level):
        return clevel[level]
    
    def format(self,record):
        
        header = self.getCFL(record.levelname)[0] + "[" + self.getCFL(record.levelname)[1] + "%-08s"%record.levelname + self.getCFL(record.levelname)[0] + "  " + self.formatTime() + "][%-24s]: " % record.name + EOC 
        return header + BYEL + record.msg + EOC
    
