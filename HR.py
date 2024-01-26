
Size = 0

Names = []
Ages = []
Salaries = []


###############################################################################################################################################
def Add () :
    print("")

def Hussein () :
    global Size


    while (True) :
        print("\n----------------------------------------------------------- Main Window -----------------------------------------------------------\n")
        print("\nPlease, Choose a number :- [1 or 2 or 3 or 4 or 5 or 6]")
        print("\t1) Add a record")
        print("\t2) Edit a record")
        print("\t3) Delet a record")
        print("\t4) Search a record")
        print("\t5) Show All Employees")
        print("\t6) Exit Program")

        Choose = input("\nYour choice : ")
        while (True) :
            try :
                G = 1 / int(Choose)
                break
            except :
                print("\nSorry!! Type Error. Please, Try again")
                Choose = input("\nPlease, Enter Your choice again : ")


        if (Choose == '1') :
            Add()
            
        elif (Choose == '2') :
            print("\n______________________________ Edit ______________________________\n")
            if (Size == 0) :
                print ("\nThere are no employees to display yet. Please add employees first to view\n")
                
        
            else :
                Search = input("\nEnter a name to search : ")
                for n in range (Size) :        
                    if (Search == Names [n]) :
                        print("\nFounded (Employee number",n+1,")\n\nPlease, Choose a number to edit :- [1 or 2 or 3]")
                        print("\t1) Edit The Name")
                        print("\t2) Edit The Age")
                        print("\t3) Edit The Salary")
                        Choose = int(input("Your choice : "))

                        if (Choose == 1) :
                            print("\nThe old name is",Names[n],"\tThe new name is : ")
                            Names[n] = input()
                            print("\nDone, Sir\n")
                            print ("\nEmployee number",n+1,"\n\nThe Name is",Names[n])
                            print ("The Age is",Ages[n])
                            print ("The Salary is",Salaries[n])
                
                        elif (Choose == 2) :
                            print("\nThe old age is",Ages[n],"\tThe new age is : ")
                            Ages[n] = int (input())
                            print("\nDone, Sir\n")
                            print ("\nEmployee number",n+1,"\n\nThe Name is",Names[n])
                            print ("The Age is",Ages[n])
                            print ("The Salary is",Salaries[n])

                        elif (Choose == 3) :
                            print("\nThe old salary is",Salaries[n],"\tThe new salary is : ")
                            Salaries[n] = int (input())
                            print("\nDone, Sir\n")
                            print ("\nEmployee number",n+1,"\n\nThe Name is",Names[n])
                            print ("The Age is",Ages[n])
                            print ("The Salary is",Salaries[n])

                        else :
                            print("\n\nNot at range [1,2,3] . Please, Try again\n")

                        break
                else :
                    print("\nNot Found")


        elif (Choose == '3') :
            print("\n______________________________ Delet ______________________________\n")
            if (Size == 0) :
                print ("\nThere are no employees to display yet. Please add employees first to view\n")
                
        
            else :
                Search = input("\nEnter a name to search : ")
                for n in range (Size) :
                    if (Search == Names [n]) :
                        del(Names[n])
                        del(Ages[n])
                        del(Salaries[n])
                        Size -= 1
                        print("\nDone, Sir\n")
                        break
                else :
                    print("\nNot Found")


        elif (Choose == '4') :
            print("\n______________________________ Search ______________________________\n")
            if (Size == 0) :
                print ("\nThere are no employees to display yet. Please add employees first to view\n")
                
            else :
                Search = input("Enter a name to search : ")
                for n in range (Size) :
                    if (Search == Names[n]) :
                        print ("\nFounded (Employee number",n+1,")\n\nThe Name is",Names[n])
                        print ("The Age is",Ages[n])
                        print ("The Salary is",Salaries[n])
                        break
                else :
                    print("\nNot Found")
        
    
        elif (Choose == '5') :
            print("\n______________________________ All Employees ______________________________\n")
            if (Size == 0) :
                print ("\nThere are no employees to display yet. Please add employees first to view\n")
        
            else :
                for n in range (Size) :
                    print ("\n(Employee number",n+1,")\n\nThe Name is",Names[n])
                    print ("The Age is",Ages[n])
                    print ("The Salary is",Salaries[n])
                    print("\n---------------------------------\n")
            

        elif (Choose == '6') :
            print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
            exit()

    
        else :
            print("\n\nNot at range [1,2,3,4,5] . Please, Try again\n")
            continue
    

        print("\nPlease, Choose a number :- [1 or 2]")
        print("\t1) Main Window")
        print("\t2) Exit Program")

        Choose = input("\nYour choice : ")
        while (True) :
            try :
                G = 1 / int(Choose)
                break
            except :
                print("\nSorry!! Type Error. Please, Try again")
                Choose = input("\nPlease, Enter Your choice again : ")

        if (Choose == '1') :
            continue

        elif (Choose == '2') :
            print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
            exit()
    
        else :
            while (True) :
                print("\n\nNot at range [1,2] . Please, Try again\n")
                print("\t1) Main Window")
                print("\t2) Exit Program")
                Choose = input("\nYour choice : ")

                while (True) :
                    try :
                        G = 1 / int(Choose)
                        break
                    except :
                        print("\nSorry!! Type Error. Please, Try again")
                        Choose = input("\nPlease, Enter Your choice again : ")

                if (Choose == '1') :
                    break

                elif (Choose == '2') :
                    print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
                    exit()


###############################################################################################################################################


def Add () :
    global Size
    
    print("\n______________________________ Add ______________________________\n")
    X = input("\nPlease, Enter the number of employees that you want add : ")
    while (True) :
        try :
            G = 1 / int(X)
            X = int(X)
            break
        except :
            print("\nSorry!! Type Error. Please, Try again")
            X = input("\nPlease, Enter the number of employees that you want add : ")
        
    for m in range (X) :
        Size+=1
        print ("\nPlease, Enter the name of the employee number",Size,": ",end="")
        Names.append(input())
        for z in range (Size-1) :
            if (Names[z] == Names[Size-1]) :
                Size -= 1
                print("\nThis Employee already added\nEmployee Number",z+1)
                print("\nPlease, Choose a number :- [1 or 2]")
                print("\t1) Main Window")
                print("\t2) Exit Program")

                Choose = input("\nYour choice : ")
                while (True) :
                    try :
                        G = 1 / int(Choose)
                        break
                    except :
                        print("\nSorry!! Type Error. Please, Try again")
                        Choose = input("\nPlease, Enter Your choice again : ")

                if (Choose == '1') :
                    Hussein()

                elif (Choose == '2') :
                    print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
                    exit()
    
                else :
                    while (True) :
                        print("\n\nNot at range [1,2] . Please, Try again\n")
                        print("\t1) Main Window")
                        print("\t2) Exit Program")
                        Choose = input("\nYour choice : ")

                        while (True) :
                            try :
                                G = 1 / int(Choose)
                                break
                            except :
                                print("\nSorry!! Type Error. Please, Try again")
                                Choose = input("\nPlease, Enter Your choice again : ")

                        if (Choose == '1') :
                            Hussein()

                        elif (Choose == '2') :
                            print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
                            exit()
        print("Please, Enter the age of the employee number",Size,": ",end="")
        Ages.append(input())
        while (True) :
            try :
                G = 1 / int(Ages[Size-1])
                break
            except :
                print("\nSorry!! Type Error. Please, Try again")
                print("\nPlease, Enter the age of the employee number",Size,": ",end="")
                Ages[Size-1]=input()
        print("Please, Enter the salary of the employee number",Size,": ",end="")
        Salaries.append(input())
        while (True) :
            try :
                G = 1 / int(Salaries[Size-1])
                break
            except :
                print("\nSorry!! Type Error. Please, Try again")
                print("\nPlease, Enter the salary of the employee number",Size,": ",end="")
                Salaries[Size-1]=input()
        print("------------------------------------------------------------------------")


###############################################################################################################################################


while (True) :
    print("\n----------------------------------------------------------- Main Window -----------------------------------------------------------\n")
    print("\nPlease, Choose a number :- [1 or 2 or 3 or 4 or 5 or 6]")
    print("\t1) Add a record")
    print("\t2) Edit a record")
    print("\t3) Delet a record")
    print("\t4) Search a record")
    print("\t5) Show All Employees")
    print("\t6) Exit Program")

    Choose = input("\nYour choice : ")
    while (True) :
        try :
            G = 1 / int(Choose)
            break
        except :
            print("\nSorry!! Type Error. Please, Try again")
            Choose = input("\nPlease, Enter Your choice again : ")


    if (Choose == '1') :
        Add()


    elif (Choose == '2') :
        print("\n______________________________ Edit ______________________________\n")
        if (Size == 0) :
            print ("\nThere are no employees to display yet. Please add employees first to view\n")
                
        
        else :
            Search = input("\nEnter a name to search : ")
            for n in range (Size) :        
                if (Search == Names [n]) :
                    print("\nFounded (Employee number",n+1,")\n\nPlease, Choose a number to edit :- [1 or 2 or 3]")
                    print("\t1) Edit The Name")
                    print("\t2) Edit The Age")
                    print("\t3) Edit The Salary")
                    Choose = int(input("Your choice : "))

                    if (Choose == 1) :
                        print("\nThe old name is",Names[n],"\tThe new name is : ")
                        Names[n] = input()
                        print("\nDone, Sir\n")
                        print ("\nEmployee number",n+1,"\n\nThe Name is",Names[n])
                        print ("The Age is",Ages[n])
                        print ("The Salary is",Salaries[n])
                
                    elif (Choose == 2) :
                        print("\nThe old age is",Ages[n],"\tThe new age is : ")
                        Ages[n] = int (input())
                        print("\nDone, Sir\n")
                        print ("\nEmployee number",n+1,"\n\nThe Name is",Names[n])
                        print ("The Age is",Ages[n])
                        print ("The Salary is",Salaries[n])

                    elif (Choose == 3) :
                        print("\nThe old salary is",Salaries[n],"\tThe new salary is : ")
                        Salaries[n] = int (input())
                        print("\nDone, Sir\n")
                        print ("\nEmployee number",n+1,"\n\nThe Name is",Names[n])
                        print ("The Age is",Ages[n])
                        print ("The Salary is",Salaries[n])

                    else :
                        print("\n\nNot at range [1,2,3] . Please, Try again\n")

                    break
            else :
                print("\nNot Found")


    elif (Choose == '3') :
        print("\n______________________________ Delet ______________________________\n")
        if (Size == 0) :
            print ("\nThere are no employees to display yet. Please add employees first to view\n")
                
        
        else :
            Search = input("\nEnter a name to search : ")
            for n in range (Size) :
                if (Search == Names [n]) :
                    del(Names[n])
                    del(Ages[n])
                    del(Salaries[n])
                    Size -= 1
                    print("\nDone, Sir\n")
                    break
            else :
                print("\nNot Found")


    elif (Choose == '4') :
        print("\n______________________________ Search ______________________________\n")
        if (Size == 0) :
            print ("\nThere are no employees to display yet. Please add employees first to view\n")
                
        else :
            Search = input("Enter a name to search : ")
            for n in range (Size) :
                if (Search == Names[n]) :
                    print ("\nFounded (Employee number",n+1,")\n\nThe Name is",Names[n])
                    print ("The Age is",Ages[n])
                    print ("The Salary is",Salaries[n])
                    break
            else :
                print("\nNot Found")
        
    
    elif (Choose == '5') :
        print("\n______________________________ All Employees ______________________________\n")
        if (Size == 0) :
            print ("\nThere are no employees to display yet. Please add employees first to view\n")
        
        else :
            for n in range (Size) :
                print ("\n(Employee number",n+1,")\n\nThe Name is",Names[n])
                print ("The Age is",Ages[n])
                print ("The Salary is",Salaries[n])
                print("\n---------------------------------\n")
            

    elif (Choose == '6') :
        print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
        exit()

    
    else :
        print("\n\nNot at range [1,2,3,4,5] . Please, Try again\n")
        continue
    

    print("\nPlease, Choose a number :- [1 or 2]")
    print("\t1) Main Window")
    print("\t2) Exit Program")

    Choose = input("\nYour choice : ")
    while (True) :
        try :
            G = 1 / int(Choose)
            break
        except :
            print("\nSorry!! Type Error. Please, Try again")
            Choose = input("\nPlease, Enter Your choice again : ")

    if (Choose == '1') :
        continue

    elif (Choose == '2') :
        print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
        exit()
    
    else :
        while (True) :
            print("\n\nNot at range [1,2] . Please, Try again\n")
            print("\t1) Main Window")
            print("\t2) Exit Program")
            Choose = input("\nYour choice : ")

            while (True) :
                try :
                    G = 1 / int(Choose)
                    break
                except :
                    print("\nSorry!! Type Error. Please, Try again")
                    Choose = input("\nPlease, Enter Your choice again : ")

            if (Choose == '1') :
                break

            elif (Choose == '2') :
               print("\n----------------------------------------------------------- Thak you for using my program -----------------------------------------------------------\n")
               exit()