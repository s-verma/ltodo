# ltodo
A 'Lazy' todo list manager. (Todo list manager for tasks which are to be done after certain date and time.)

INTRODUCTION:

The "Lazy todo" in short ltodo is a very simple todo list management program intended for lazy people who doesn't want to their tasks right now but want to be reminded for the tasks after certain fixed time.

RATIONALE & FAQs:

Why build a simple tool for doing todo list management when there are so many programs out there?

The reason I built this is to manage my tasks according to my own specific requirements. I am quite lazy for many low priority tasks and hence keep pushing them and many times forget them. So I needed a program which can remind me to do certain task only after certain fixed time.

Do you think people in the world are lazy enough to use your program?

Sorry but I didn't name it to say that people are lazy. The word lazy in the "Lazy todo" program is to signify that this program is specially suited for those taks which we keep for low priority (hence we are lazy towards those tasks) and hence want to do after certain date and time as compared to urgent tasks which should be done before certain date and time. E.g. paying electricity bills must be before certain date as compared to let say study a novel or try a different flavour of ice cream.

INPUT and OUTPUT:

The program ltodo takes inputs from a file in the following format of each line per task:
X;Y;Z
i.e. three items X,Y and Z separated by ';' (semicolon)
e.g.

TASK; Task Description; 1/1/2018 00:00
where:
1. X is just a tag such as TODO, TASK, REMINDER etc.
2. Y is task description e.g. "Clean the room"
3. Z is date and time after which the utility must notify the user for the pending tasks. The format is day/month/year hour:minutes
where hour:minutes are 24 hour formats.

some examples are:
TASK; Clean the cupboard; 1/1/2018 12:30
REM; Try that new restaurant ; 12/1/2018 14:20
TODO; Buy some stuff; 26/1/2018 16:40

The outputs are all the tasks which are due at the present time.
e.g. if current time is 12/1/2018 15:00
then output will be 

TASK; Clean the cupboard; 1/1/2018 12:30

REM; Car servicing; 12/1/2018 14:20

as they fall before the current time.

USAGE: ltodo [todo_file]

todo_file is the file which program reads.
todo_file is optional, if not supplied program reads from ~/.todo.list

Future Work:

1. Adding support for the different time formats such as month/day/year or time in am/pm or different time zones can be included if I find the demand from the users in the issues.
