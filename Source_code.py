from datetime import datetime
from uuid import uuid1
class Task:
    list = []
    def __init__(self):
        self.task =''
        self.created_time = 'NA'
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False
        self.id = uuid1()

    def update_task(self, name):
        self.task = name
        self.created_time = datetime.now()
        self.list.append(self)
        print('\nTask created succesfully')
       
    def complete_task(self):
        j=1
        print('\n')
        for i in self.list:
            print(f'Task No- {j}')
            print(f'ID- {i.id}')
            print(f'Task- {i.task}')
            print(f'Created time- {i.created_time}')
            print(f'Updated time- {i.updated_time}')
            print(f'Completed- {i.task_done}')
            print(f'Completed time- {i.completed_time}')
            print("\n")
            j+=1
        print('\n')
        num = int (input('Enter task no: '))
        if (num-1) >=0 and (num-1)<len(self.list):
            self.list[num-1].task_done=True
            self.list[num-1].completed_time =datetime.now()
            print('\nTask Completed successfully\n')
        else:
            print("\nInvalid Task Number\n")
    
    def print_instance(self):
        for i in self.list:
            print(f'ID- {i.id}')
            print(f'Task- {i.task}')
            print(f'Created time- {i.created_time}')
            print(f'Updated time- {i.updated_time}')
            print(f'Completed- {i.task_done}')
            print(f'Completed time- {i.completed_time}')
            print("\n")
    
    def for_update_task(self):
        j=1
        print('\n')
        for i in self.list:
            print(f'Task No- {j}')
            print(f'ID- {i.id}')
            print(f'Task- {i.task}')
            print(f'Created time- {i.created_time}')
            print(f'Updated time- {i.updated_time}')
            print(f'Completed- {i.task_done}')
            print(f'Completed time- {i.completed_time}')
            print("\n")
            j+=1
        print('\n')
        num = int (input('Enter task no: '))
        if (num-1) >=0 and (num-1)<len(self.list):
            name = input('Enter new task: ')
            self.list[num-1].task=name
            self.list[num-1].updated_time =datetime.now()
            print('\nTask Updated successfully\n')
        else:
            print("\nInvalid Task Number\n")
    def sow_completed_task(self):
        count=0
        for i in self.list:
            if i.task_done ==True:
                count+=1
        if count==0:
            print("\nno completed task\n")
        else:
            for i in self.list:
                if i.task_done == True:
                    print("\n")
                    print(f'ID- {i.id}')
                    print(f'Task- {i.task}')
                    print(f'Created time- {i.created_time}')
                    print(f'Updated time- {i.updated_time}')
                    print(f'Completed- {i.task_done}')
                    print(f'Completed time- {i.completed_time}')
                    print("\n")
    def sow_incomplete_task(self):
        flag = True
        for i in self.list:
                if i.task_done == False:
                    print("\n")
                    flag=False
                    print(f'ID- {i.id}')
                    print(f'Task- {i.task}')
                    print(f'Created time- {i.created_time}')
                    print(f'Updated time- {i.updated_time}')
                    print(f'Completed- {i.task_done}')
                    print(f'Completed time- {i.completed_time}')
                    print("\n")
        if flag ==True:
            print("\nAll Task are completed\n")
        
        
while True:
    print('\n')
    print("1.Add New Task")
    print("2.Show All Task")
    print("3.Show Incomplete Task")
    print("4.Show Complete Task")
    print("5.Update Task")
    print("6.Mark A Task Completed")
    n = int (input ('Enter option: '))
    obj = Task()
    if n==1:
        name = input('Enter New Task: ')
        obj.update_task(name)
    elif n==2:
        print('\n')
        obj.print_instance()
    elif n==3:
        obj.sow_incomplete_task()
    elif n==4:
        obj.sow_completed_task()
    elif n==5:
        obj.for_update_task()
    elif n==6:
        obj.complete_task()


        
        


            



