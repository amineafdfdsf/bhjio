while True:
    import random

    # the baisic infermichen
    emojis = {"R": "🪨", "S": "✂️", "P": "📃"}
    ch = ("R", "P", "S")
    com = 0
    user = 0
    # whil loop
    while com < 3 and user < 3:
        US = (input("enter votre choice (P/R/S) :")).upper()
        coputer_choice = random.choice(ch)

        # invalid nomber
        while US not in ch:
            print("invalid number !")
            US = (input("enter votre choice (P/R/S) :")).upper()
        computer = emojis[coputer_choice]
        amine = emojis[US]
        if US == coputer_choice:
            print(f"P:{amine} <==> C:{computer}")
            print("dessiner")
        elif (
                (US == "R" and coputer_choice == "S") or
                (US == "S" and coputer_choice == "P") or
                (US == "P" and coputer_choice == "R")):
            user += 1
            print(f"P:{amine} <==> C:{computer}")
            print("Vous gagnez ce tour !")
        else:
            com += 1
            print(f"P:{amine} <==> C:{computer}")
            print("L'ordinateur gagne ce tour !")
    # score
    if user == 3:
        print(f"Le gagnant c'est toi SCORE : 3 \n              {com} <===> {user} ")
    else:
        print(f"Le gagnant c'est L'ordinateur SCORE : 3 \n              {com} <===> {user} ")

    continue_playe = input("do you whant to contuine play y/n :").lower()
    if continue_playe == "n":
        print("ok pay pay")
        break