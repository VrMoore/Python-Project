task_list = []

class taskBuddy() :

    def __init__(self) :
        pass

    def taskAdd(self,task : str) :
        task_list.append(task)

    def taskDelete(self,task : str) :
        if len(task_list) == 0 :
            print("No task to delete")
        else :
            task_list.pop(task)

    def taskUpdate(self,task : str) :
        pass

    def display(self) :
        for i in range(len(task_list)) :
            print(f"{i}. {task_list[i]}")

    def taskExit(self) :
        print("Thanks for using TaskBuddy")

class handler(taskBuddy) :
    def __init__(self, name : str) :
        self.name = name

    def check_user_input(self,input:int, task : str = None) :
        if input == 1 :
            return self.display()
        elif input == 2 :
            return self.taskAdd(task)
        elif input == 3 :
            return self.taskDelete(task)
        elif input == 4 :
            return self.taskUpdate()
        elif input == 5 :
            return self.taskExit()
        else :
            return "Invalid Input"

    def display(self) :
        print(self.name)
        print(task_list)

if __name__ == "__main__" :
    print('Welcome to TaskBuddy!!\n')

    print("I'll help you to manage your task.")
    print("You can add, delete or update your task\n")

    user_task_name = input('Your To Do List name : ')
    
    print("\n1. Display Task")
    print("2. Add New To Do List")
    print("3. Delete To Do List") 
    print("4. Update Task Progress")
    print("5. Exit\n")


    if len(user_task_name) != 0 : 
        user_input = input("Want to Use TaskBuddy? (y/n) : ")
        while user_input == "y" :
            user_input_num = int(input("Enter your choice : "))
            task = handler(user_task_name)
            task.check_user_input(user_input_num)

        else :
            print('Thanks')
    else :
        print('No Name Given.')


    
        