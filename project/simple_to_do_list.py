task_list = []

class taskBuddy() :
    def __init__(self) :
        pass

    def display(self) :
        print('\n-----Today task-----')
        if len(task_list) != 0 : 
            for i in range(len(task_list)) :
                print(f"{i+1}. {task_list[i]}")
        else :
            print('You have no task.\n')

    def addTask(self,new) -> list :
        task_list.append(new)
        print('Task Added')

    def deleteTask(self,discard) :
        if len(task_list) != 0 :
            del task_list[discard-1]
            print('Task Deleted')
        else :
            print('Nothing to delete')

if __name__ == "__main__" :
    print("\nWelcome to TaskBuddy")
    print("TaskBuddy will help you to manage your tasks\n")

    print("1. Display")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit Task")

    while True :

        user_input_choice = int(input('\nWhich choice do you choose? : '))

        if user_input_choice == 1 :
            run_task = taskBuddy()
            run_task.display()

        elif user_input_choice == 2 :
            task = input('What task do you want to add? : ')
            run_task = taskBuddy()
            run_task.addTask(task)

        elif user_input_choice == 3 :
            task = int(input('What task do you want to delete? : '))
            run_task = taskBuddy()
            run_task.deleteTask(task)

        elif user_input_choice == 4 :
            print('Exit Task')
            break

        else :
            print('Invalid choice')
            break
    else :
        print('Goodbye')
