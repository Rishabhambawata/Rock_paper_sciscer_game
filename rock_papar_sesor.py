import random
while True:
    user=input("enter number (rock,papar,sesor)\n")
    user=user.lower()
    action=["rock","papar","sesor"]
    com_act=random.choice(action)

    if user=="rock" or user=="papar" or user=="sesor":
        print(f"you Choose {user} and computer Chosse {com_act}")
        if user==com_act:
            print("tied")
        elif user=="rock":
            if com_act=="sesor":
                print("rock smash uou win")
            else:
                print("you loss")
        elif user=="sesor":
            if com_act=="papar":
                print("paper cut you win")
            else:
                print("you loss")
        elif user =="papar":
            if com_act=="rock":
                print("papar grabs YOU WIN")
            else:
                print("you lose")
    else:
        print("Pls enter valid value😑")
    agani=input("Play again ?y|n  \n")
    if agani.lower()=="n":
        print("Thanks for Playing")
        break

     








