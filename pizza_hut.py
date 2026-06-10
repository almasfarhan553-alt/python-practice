# I make a program for my "ALTa pizza hut"here the cutomer can 1stly select the which size of pizza want and
#and then customer select add extra peperoni and add some exttra cheese, cutomer only said yes or not,
# based the customer condition program can automatically calculate Total Bill.
#PLEASE SAW MY PROGRAM AND ENJOY.
#THANK YOU....


print("Welcome To AlTa Pizza Hut")
price =0
pizza =input("which size of pizza do you want,\nSmall\nMedium\nLarge\n say is 'small''medium''large':-\n")

#SMALL SIZE PIZZA.

if pizza =="small":
   sprice =15 
   print(f"you will select {pizza} size & price ${sprice}. ")
   
   
   add_peperoni_small_size=input("Add Pepproni For Small Pizza\n yes or not say:- ")
    
   if add_peperoni_small_size =="yes" :
       sprice +=2
       print(f"Your Bill is ${sprice}")
   else :
      print(f"Your Bill is ${sprice}")
   extra_cheese=input("Do you want Extra cheese? 'yes' Or 'not':- ")
   if extra_cheese == "yes" :
         sprice +=1
         print(f"your Total bill ${sprice} ")
   else :
         print(f"your Total Bill ${sprice}")     

#MEDIUM SIZE PIZZA.


elif  pizza =="medium" :
   mprice =20
   print(f"you will select {pizza} size & price ${mprice}. ")

   add_peperoni_medium_size=input("Add Pepproni For Small Pizza\n yes or not say:- ")

   if add_peperoni_medium_size =="yes" :
       mprice +=3
       print(f"Your Bill is ${mprice}")
   else :
      print(f"Your Bill is ${mprice}") 
   extra_cheese=input("Do you want Extra cheese? 'yes' Or 'not':- ")
   if extra_cheese == "yes" :
         mprice +=1
         print(f"your Total bill ${mprice} ")
   else :
         print(f"your Total Bill ${mprice}")     


#LARGE SIZE PIZZA.

elif pizza =="large" :
   lprice =25
   print(f"you will select {pizza} size & price ${lprice}.") 
   
   add_peperoni_Large_size=input("Add Pepproni For Small Pizza\n yes or not say:- ")
   
   if add_peperoni_Large_size =="yes" :
       lprice +=3
       print(f"Your Bill is ${lprice}")
   else :
      print(f"Your Bill is ${lprice}")    
   extra_cheese=input("Do you want Extra cheese? 'yes' Or 'not':- ")
   if extra_cheese == "yes" :
         lprice +=1
         print(f"your Total bill ${lprice} ")
   else :
         print(f"your Total Bill ${lprice}")  
   
else:
   print("Invalid Size!!!")  













