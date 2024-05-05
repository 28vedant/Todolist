tasks=[]

def addTask():
    task = input("Please  enter the task you want to add: ")
    tasks.append(task)
    print (f"Your task {task}has been added!")


def listTask():
    if not tasks:
        print("No tasks have been added yet.")
    else:
        print("Current Tasks")
        for index,task in enumerate(tasks):
            print(f"{index}: {task}")

def deleteTask():
    listTask()
    try:
        tasktodelete=int(input("\nWhich Task do you want to Delete?\n"))
        if tasktodelete >=0 and tasktodelete <len(tasks):
            tasks.pop(tasktodelete)
            print (f"Task {tasktodelete}has been deleted")

        else:
            print (f"Task {tasktodelete}has been deleted")
    except:
        print("invalid value")
if __name__=="__main__":

    print("Welcome to the To Do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("---------------------------------")
        print("1. Add a task.")
        print("2. Delete a task.")
        print("3. List all tasks.")
        print("4.Quit")

        choices = input("Enter your choice (1/2/3/4): ")
        if(choices == '1'):
            addTask()
        elif(choices=='2'):
            deleteTask()
        elif(choices=='3'):
            listTask()
        elif(choices=='4'):
            break
        else:
            print("Invalid option! Please enter 1, 2 , 3 or 4.")
