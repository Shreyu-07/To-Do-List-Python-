print("☺Welcome to the todolist:☺ \n")
print('-----------------------------------------------------------------------------------------')
lists = []
try:
    noList = int(input("Enter the number of list"))
    number = 0
    while True:
        while number < noList:
            data = input("Enter the task: ")
            number+=1
            lists.append(data)
        print('Your tasks are: ')
        for i,j in enumerate(lists):
            print(f"{i}) {j} .")
        listOfIndex = list(range(len(lists)))
        print('--------------------------------------------------------------------------------------- \n')
        print("What do u want to do : \n 1) remove the task \n 2)Clear the task \n")
        taskOPtion = int(input("Enter the option (1 or 2 ): "))
        print(f'You have enterd: {taskOPtion}')
        match taskOPtion:
            case 1:
                tasknumrem = int(input("Enter the task number to remove : "))
                if tasknumrem in listOfIndex:
                    lists.pop(tasknumrem)
                    for i, j in enumerate(lists):
                        print(f"{i}) {j} .")
                else:
                    print("The task not found...!!!")
                    continue
            case 2:
                print('All task cleard....!!')
                lists.clear()
                for i,j in enumerate(lists):
                    print(f"{i}) {j} .")
        
        usePermition = input('Do you want to continue :> (Y/N)').strip().lower()
        if usePermition !='y':
            print("Thank you have a good day....♥☻☺☺☻♥")
            break
except:
    print("☻☺ There was some users error.... ☺☻")

