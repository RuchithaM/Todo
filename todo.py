import os
import argparse
from datetime import date
def create_files(path):
     # create todo.txt and done.txt
    todo_file =os.path.join(path,'todo.txt')
    done_file = os.path.join(path,'done.txt')

    if not os.path.isfile(todo_file):
        with open(todo_file,'a') as file:
            pass

    if not os.path.isfile(done_file):
        with open(done_file,'a') as file:
            pass

def parse_arg():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    create_parser = subparser.add_parser('todo')
    create_parser.add_argument('--add',nargs='?',type=str,default=None,help="# Add a new todo")
    create_parser.add_argument('--ls', action='store_true',default=None,help='# Show remaining todos')
    create_parser.add_argument('--del',type=int,help="# Delete a todo")
    create_parser.add_argument('--done',type=int,help="# Complete a todo")
    create_parser.add_argument('--report', action='store_true',default=None,help=" # Statistics")
    args = parser.parse_args()
    #print(vars(args))
    return(vars(args)) #{'add': ['water'], 'ls': None, 'del': None, 'done': None}

def reverse_mapping():
    with open('todo.txt','r') as file:
        c=[]
        for i in file:
            c.append(i)
        m =c[::-1]
        d={}
        for i in range(len(c)):
            for j in range (len (m)):
                if c[i] == m[j]:
                    d[j+1]=m[i]
    return(d)

def add(argument):
    with open('todo.txt','a') as file:
        file.write(str(argument)+'\n')
    print('Added todo: "{}"'.format(argument))   
    
def check_for_todo_exist(argument):
    d=reverse_mapping()
    print(d)   #items
    if argument in d:
        string=d[argument]
        return(string)
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(argument))
        return(False)

def remove_string_from_file(file_name,string):
    #print(string,file_name)
    with open('todo.txt', "r") as f:
        lines = f.readlines()
    with open('todo.txt', "w") as f:
        for line in lines:
            if not line == string:
                f.write(line)
            

def dele(argument):
    s=check_for_todo_exist(argument)
    if s != False :
        remove_string_from_file('todo.txt',str(s))
    else:
        pass
def done(argument):
    s=check_for_todo_exist(argument)
    if s != False :
        remove_string_from_file('todo.txt',s)
        with open('done.txt','a') as file:
            print(s)
            file.write('x '+str(date.today())+" "+s)
        print("Marked todo #{} as done.".format(argument))

def ls():
    d=reverse_mapping()
    for item in d:
        print("[{}] {}".format(item,d[item])) 
    else:
            print("There are no pending todos!")        
def report():
    with open("todo.txt",'r') as f:
        pending=len(f.readlines())
    with open("done.txt",'r') as f:
        completed=len(f.readlines())  
    print(str(date.today())+" Pending : {} Completed : {}".format(pending,completed))

def resolve_arguments(args): 
    #which argument is not null
    for i, j in args.items():
        if j != None:
            return(i,j)
        
    
       
def fun_call(operation):
    #call the function based on which argument is not null
    #print(operation)
    for i in operation:
        if i == 'add':
            add(operation[1])
        elif i== 'del':
            dele(operation[1])
        elif i== 'done':
            done(int(operation[1]))
        elif i== 'ls':
            ls()
        elif i=='report':
            report()
        
        

if __name__ == '__main__':
    file_path = os.getcwd()
    create_files (file_path) 
    arguments=parse_arg()
    #print(arguments)
    operation=list(resolve_arguments(arguments))
    fun_call(operation)