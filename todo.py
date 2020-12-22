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
    my_parser = argparse.ArgumentParser()
    my_group = my_parser.add_mutually_exclusive_group()
    my_group.add_argument('-add',nargs='*',type=str,default=None)
    my_group.add_argument('-ls', action='store_true',default=None)
    my_group.add_argument('-del',type=int)
    my_group.add_argument('-done',type=int)
    args = my_parser.parse_args()
    return(vars(args)) #{'add': ['water'], 'ls': None, 'del': None, 'done': None}



def add(argument):
    with open('todo.txt','a') as file:
        file.write(str(argument)+'\n')
    print('Added todo : "{}"'.format(argument))   
    
def dele(argument):
    
    pass

def done(argument):
    with open('done.txt','a') as file:
        time=date.today()
        file.write(str(time))
        file.write(' '+str(argument)+'\n') 


def ls():
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
                    v=j+1
                    print('[{}] {}'.format(j+1,m[i]))  
                    
        


def resolve_arguments(args): 
    #which argument is not null
    for i, j in args.items():
        if j != None:
            return(i,j)
        elif i=='ls':
            return(i)
    
       
def fun_call(operation):
    #call the function based on which argument is not null
    for i in operation:
        if i == 'add':
            add(operation[1][0])
        elif i== 'del':
            dele(int(operation[1]))
        elif i== 'done':
            done(int(operation[1]))
        elif i== 'ls':
            ls()
        
        

if __name__ == '__main__':
    file_path = os.getcwd()
    create_files (file_path) 
    arguments=parse_arg()
    operation=list(resolve_arguments(arguments))
    fun_call(operation)