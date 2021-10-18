


def questions() :
    
    #loan
    
    print("\nHow much do you spend money on loan")
    cost=int(input(">> "))
    
    if cost>income :
        print("your dont earn more than",income)
    i=cost
    
    
    #food
    
    print("How much do you spend money on food")
    cost=int(input(">> "))
    
    if cost>income :
        print("your dont earn more than",income)
        
    b=i+cost
    
    #junk food
    
    print("How much do you spend money on junk food")
    cost=int(input(">> "))
    
    if cost>income :
        print("your dont earn more than",income)
    i=b+cost
    
    #stream platform 
    
    print("How much do you spend money on onine streaming platform like netflix ")
    cost=int(input(">> "))
    
    if cost>income :
        print("your dont earn more than",income)
    b=i+cost
    
    #ask about house
    
    print("Do you live on rented house or you own you own house")
    print("select between rented or own")
    choise=input(">> ")
    
    #if own house
    
    if choise in ["own","Own"] :
        print("so do you have loan for hous and enter monthly pay")
        cost=int(input(">> "))
        i=b+cost
        
        #if rented 
        
    elif choise in ["rent","Rent","rented","Rented"] :
        print("so how much is your monthly rent")
        cost=int(input(">> "))
        i=b+cost
    else :
        print("invalid input")
        pass
        
    #taxes
    print("how much do you spend on taxes")
    cost=int(input(">> "))
    b=i+cost
    final=b 
    
    #insurance
    
    print("Do you pay to any insurance company")
    print("type yes or no ")
    choise=str(input(">> "))
    if choise in ["yes","Yes","Y","y","yea","Yea","yup","Yup"] :
        print("how much do you spend")
        cost=int(input(">> "))
        i=b+cost
        
        final=i #summing all value in         final var
    if choise in ["no","No","N","n","Nope","nope"] :
        print("ok u dont spend any")
    else :
        print("invalid")
        
    print("you spend total",final,"rs")

#totals saves and save value in #saved_amount

    saved_amount=income-final
    print("you saved total",income-final,"rs")
    
    #comapring his past and present #savings
    
    #if he saves more
    if saved_amount>general_sav :
        print("congo ypu saved more than you saved generally")
    #if he saves less
    
    elif general_sav>saved_amount :
        print("\nsorry you have been spending more ,you have been saving more before ,please try again")
        k=0.  #start loop
       
        #asking for yes to satrt prog again
        
        print("\nDo you want to try again enter yes or no")
        choise=input(">> ")
        if choise in ["yes","yes","yea","Yea"] :
            while(k==0) :
                questions()
        elif choise in ["no","No","Nope","nope"] :
            print("bye!!!!")
            pass
#vaiables
i=0
k=0 
#program

#name taking save in name var 

print("Enter the name of subject for whome are we creating a budget plan : ")
name=input(">> ")

#taling income detail in var income

print("\nhey",name ,"Enter your income in integer for month only")
income=int(input(">> "))

# knowing his saving in var #genera_sav
while(k==0) :
    print("\nplease tell me how much do you save at end of month ,for general")
    general_sav=int(input(">> "))
    
    #if you contion is invalid
    
    if general_sav>income :
        print("your saving is more than your income please try again")
        continue
        
        #if you conditon is 
    elif income>general_sav :
        k=1 #breaking loop while

print("\n----your details has been taken-------------")


questions()

#thank his to use program

print("\nthank you",name,"for trying our program")
