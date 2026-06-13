#In This Program i make a Game this, game name is "Escape Devil House" .


print("Welcome to Devil House ")
print("    Escape From Devil House😈: ")


#LEVEL 1 CHOOSE RED,GREEN,BLACK DOOR.


choice1=input('In Devil Home There Are Three Door,' \
              ' You Enter Which For Escape This House' \
              ' "red", "black", "green" : ').lower()
if choice1 == "red":
    print("GAME OVER!!" \
         " DEVIL CAN KILL YOU ")
elif choice1 == "black" :
    print("GAME OVER!!" \
          " DEVIL DOG CAN KILL YOU")
elif choice1 == "green" :
    print("You Enter Devil Garden")


#LEVEL 2 CHOOSE ONE GATE, STEEL OR IRON GATE.
    
    choice2=input('There Are Two(2) gate' \
          ' Choose one "steel" ,"iron" gate :').lower()
    if choice2 == "iron" :
        print("YOU SUCCESSFULLY " \
          " ESCAPE FROM DEVIL HOUSE" \
          "  !!!YOU WIN!!!")
    else:
        print("DEVIL GUARD KILL YOU, " \
          " GAME OVER..")
else :
    print("^^ERROR^^" \
          " CHOOSE RIGHT WORDS")
    