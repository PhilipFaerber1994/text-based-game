def goUpstairs():
    print("To go upstair put 'GO UP' into the console. -->[GO UP]")
    inputGoUp = input()
    if inputGoUp == "GO UP":
        print("You are on the next floor")
    else:
        print("invalid input. "
        "YOU LOST!!!")
    

def walk():
    steps = 0
    for x in range(0, 26):
        print ("Put 'WALK' into the console to step 5 steps forward . -->[WALK]")
        y = input()
        if y == "WALK":
            print ("walk...")            
            steps += 5
            if steps == 25:
                goUpstairs()
                break

def wait():
    steps = 0
    print ("You choose. Put in 'WAIT' or 'GO'. But watchout. If you go to early the teacher will see you. -->[WAIT/GO]")
    for x in range(0, 26):
        y = input()
        if y == "WAIT":
            print ("wait...")
            print ("You choose. Put in 'WAIT' or 'GO'. But watchout. If you go to early the teacher will see you. -->[WAIT/GO]")
            steps += 5
            if steps == 15:
                print("Now run")
                run()
                break
        if y == "GO":
            print("Teacher: 'Wait. What you are doing here. You are supposed to be in the lesson. No we have to go to the principal."
            "YOU LOST!!!")

def run():
    print("Put in 'RUN'. -->[RUN]")
    y = input()
    if y == "RUN":
        print("Great. Now you are on the next floor. It is the floor where the principals room is. "
        "During the lesson he is not in his room. This is you chance to get into it and make an announcement to get Mr. Evil out of the classroom.")

def makeAnnouncement():
    print("Go to the principals room")
    #steps = 0
    print ("Put 'WALK' into the console to step 5 steps forward. -->[WALK]")
    for steps in range(0, 26, 5):
        y = input()
        if y == "WALK":
            print ("walk...")
            print ("Put 'WALK' into the console to step 5 steps forward . -->[WALK]")            
            if steps == 15:
                print("Great, you made it to the principals room. Now it is you chance to get to the classroom safely."
                "You: 'Mr. Evil, please find yourself immediately in the office of Mr. Smith'")
                break

def goToClassroom():
    print("Now you have to hury up. Mr. Evil is out of the classroom. It is your chance to get in without beeing caught."
    "Put in the way you want to get in the room, but remember what I told you in the beginning"
    "-->[ELEVATOR/STAIRS]")
    y = input()
    if y == "ELEVATOR":
        print("Mr. EVIL: 'Who do we have here. I think you should join my visit at Mr. Smiths' office.\n"
        "YOU LOST!!!")
    elif y == "STAIRS":
        print("Friend in the classroom: 'Thank god, you made. Mr. Evil is in bad mood. He would have killed you, if he has seen you.'"
        "CONGRATS. YOU WON!!!")



def main():
    print("\n\n----------------WHAT A NIGHT----------------\n\n"
    "What a night. You are a student who was on a party last night." 
    "Unfortunatelly you had a few drinks to much and now you are "
    "very messed up. That is the reason you are to late for the lesson."
    "Of all things it is the lesson of Mr. Evil. The most mean teacher of the school."
    "The only way to get in the classroom without beeing caught by him is too get into the room"
    "of principal Noise to make an announcement to Mr. Evil to get him out of the classroom."
    "Be careful: The elivator is quick to change the floors, but the teachers are lazy and do not like to walk."
    "So you can either take the risk to take to elivator and get caught or you take the safe stairs.")

    print("\n=====================================================================================")

    walk()

    print("\n=====================================================================================")

    print("You are now on the second floor. Watch out! A teacher is coming straight forward to you. "
    "You have to wait until he is in the bathroom to go to the elevator. "
    "--> 1 WALK = 5 steps and the teacher needs 15 steps to get in the batchroom."
    "--> The whole floor needs 25 steps.")

    wait()

    print("\n=====================================================================================")

    makeAnnouncement()
    goToClassroom()

main()