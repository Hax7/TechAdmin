import os

def get_username(target):
    wmic_output = os.popen("wmic /node:'{0}' computersystem get username".format(target)).read()
    print(wmic_output)

def get_softwares(target):
    wmic_output = os.popen("wmic /node:'{0}'  product get name,version".format(target)).read()
    print(wmic_output)

def get_tasklist(target):
    tasklist_output = os.popen("tasklist /s {0}".format(target)).read()
    print(tasklist_output)

def killTask(target):
    pid = str(raw_input("Enter PID: "))
    taskkill_output = os.popen("taskkill /s {0} /PID {1}".format(target,pid)).read()
    print(taskkill_output)
    
    
choise = {'1': get_username,
          '2': get_softwares,
          '3': get_tasklist,
          '4': killTask}

while(True):
    
    print('''Please chose your option then enter your target computer:
    1: Get logged in username
    2: Get a list of installed softwares
    3: Get a list of running tasks
    4: Kill task using PID
    5: Exit''')
    
    command_type = str(raw_input("option: "))
    if command_type == "5":
            exit()
            
    target = str(raw_input("Target: "))
    choise[command_type](target)
