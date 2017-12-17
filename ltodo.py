#!/usr/bin/python

import datetime
import os
import sys

now=datetime.datetime.now()
print "Current time: "+ str(now)+'\n'

class todo_t:
  year=2017
  month=8
  day=23
  hour=3
  minute=30

def compare_times(time1, time2):
  if time1.year>time2.year:
    return 1
  elif time1.year<time2.year:
    return -1
  else:
    if time1.month>time2.month:
      return 1
    elif time1.month<time2.month:
      return -1
    else:
      if time1.day>time2.day:
        return 1
      elif time1.day<time2.day:
        return -1
      else:
        if time1.hour>time2.hour:
          return 1
        elif time1.hour<time2.hour:
          return -1
        else:
          if time1.minute>time2.minute:
            return 1
          #elif time1.minute<=time2.minute:
           # return -1
          else:
           # if time1.second>time2.second:
            #  return 1
            #elif time1.second<time2.second:
             # return -1
            #else:
            return -1

task_time=todo_t()

#Take the todo file.
if len(sys.argv)<2:
  if os.path.exists(os.path.expanduser('~/.todo.list')):
    todo_list=os.path.expanduser('~/.todo.list')
  else:
    print("ERROR: Couldn't find todo list file.\n")
    print("Usage: " + sys.argv[0] + " [todo_list_file]")
    print("OR")
    print("Place your todo list file as ~/.todo.list")
    sys.exit(1)
else:
  if os.path.exists(os.path.expanduser(sys.argv[1])):
    todo_list=os.path.expanduser(sys.argv[1])
  else:
    print("ERROR: Supplied file "+sys.argv[1]+" doesn't exists.")
    sys.exit(1)

todo_file=open(todo_list,"r")
for line in todo_file:
  if line.strip()!="":
    task_info=line.split(";")
    task_time_str=str(task_info[2]).strip().split("/")
    #Prepare time object for todo time.
    timeyear=task_time_str[2].split(" ")
    timeInput=timeyear[-1].split(":")
    task_time.day=int(task_time_str[0])
    task_time.month=int(task_time_str[1])
    task_time.year=int(timeyear[0])
    task_time.hour=int(timeInput[0])
    task_time.minute=int(timeInput[1])
    #task_time.second=int(timeInput[2])

    if compare_times(task_time,now)==-1:
      print line
