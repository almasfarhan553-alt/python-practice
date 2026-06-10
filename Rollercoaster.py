#i Can make a Program about the if user can ride rollercoster or not 
# it can decided by this program and 
# how much $ can you pay based on age
# so, please check this program and enjoy this.  


print("WELCOME TO ROLLERCAOSTER")
height= int(input("please Enter Your Height In CM = "))
bill=0
if height >=120 :
    print("You Can Ride The Rollercaoster")

#Here, i can give Age condition to the user:

    age=int(input("please Enter Your Age: "))
    if age < 12:
        print("Child Ticket is Only $5")
        bill=5
    elif age >=12 and  age <18:
     print("Youth Ticket is only $7")
     bill =7
    else: 
       print("Adult Ticket is only $12")
       bill =12
   
#in Here i can give another condition to the user,
#it is "can take a photo condition"
    
    print("IT IS THE LAST QUESTION,\nAFTER THIS QUESTION YOUR RIDE PASS IS READY.")
    photo=(input("If You Want To Take A Photo,\n If You Take Photo Say 'yes' not take say 'no' :- "))
    if photo =="yes":
       bill+=3
       print(f"Your Final Bill is {bill}, \n Enjoy Your Ride,\n      Good Byee....") 

    elif  photo =="no":
       bill+=0
       print(f"Your Final Bill is {bill}, \n Enjoy Your Ride,\n      Good Byee....")
else : 
    print("You Are Not Aligable To Ride") 

