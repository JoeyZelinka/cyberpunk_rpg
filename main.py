
from ingame_roller import success_roll
import time
from Decker import Decker
from Street_Samurai import Street_Samurai


print("Welcome to Not Cyberpunk 2077! Let's get started... ")
time.sleep(1)
character_class = input("Would you like to be a Decker(hacker) or a Street Samurai? ")
if character_class == ("D") or character_class == ("d"):
    print("You're a Decker.")
    print("Time to roll stats")
    character = Decker() 
    time.sleep(2)
    print("")
    print("You have your first job offer!")
    
    job = input("Would you like to know more? Y/N ")
    if job == ("Y") or job == ("y"):
        print("""The job is simple. Hack a Dominion box in the Gibson mainframe computer system of the Satoshi Nakamoto Corporation. 
Then copy their garbage file and upload it to the IP address 127.0.0.1 port 21""")
    if job == ("N") or job == ("n"):
        print("That's why you're broke. BROKE ASS!")
    
    yorn = input("Do you accept the job? Y/N ")
    if yorn == ("Y") or job == ("y"):
        print("Excellent. Contact us once the upload is complete you will receive your payment.")
    if yorn == ("N") or job == ("n"):
        print("That's why you're broke. BROKE ASS!")
    time.sleep(2)
    print(".")
    print("..")
    print("...")
    time.sleep(2)
    print("Well, time for you to jack in.")
    time.sleep(2)
    print("You are connected to the Gibson's main interface...")
    while True:
        how_hack = input("""Choose one:
            1. Brute Force the password
            2. Conduct DDoS attack
            """)
        if how_hack == ("1"):
            time.sleep(1)
            if(character.logic + character.hacking) > success_roll():
                print("You're in!")
                time.sleep(2)
                print("You copy the garbage.txt file and get off the mainframe")
                time.sleep(2)
                print("Commencing upload to 127.0.0.1 port 21")
                time.sleep(2)
                print("Upload complete. You receive 50,000 credits")
                time.sleep(2)
                print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                break
            else:
                print("Your brute force attack failed. Try again.")
            
        elif how_hack == ("2"):
            time.sleep(1)
            if(character.logic + character.hacking) > success_roll():
                print("You're in!")
                time.sleep(2)
                print("You copy the garbage.txt file and get off the mainframe")
                time.sleep(2)
                print("Commencing upload to 127.0.0.1 port 21")
                time.sleep(2)
                print("Upload complete. You receive 50,000 credits")
                time.sleep(2)
                print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                break
            else:
                print("Your DDoS attack failed. Try again.")
         
if character_class == ("S") or character_class == ("s"):
    print("You're a Street Samurai.")
    print("Time to roll stats")
    character = Street_Samurai()
    time.sleep(2)
    print("")
    print("You have your first job offer!")

    job = input("Would you like to know more? Y/N ")
    if job == ("Y") or job == ("y"):
        print("""HELP! The Hacker King Kevin Mitnick has been kidnapped by the Yakuza.
    We need you to rescue him from where the Yakuza are holding him and bring him back 2600's 
    Headquarters.""")
    if job == ("N") or job == ("n"):
        print("That's why you're broke. BROKE ASS!")

    yorn = input("Do you accept the job? Y/N ")
    if yorn == ("Y") or job == ("y"):
        print("Excellent. Bring The Hacker King back to us and you'll be handsomely rewarded!")
    if yorn == ("N") or yorn == ("n"):
        print("That's why you're broke. BROKE ASS!")

    time.sleep(2)
    print(".")
    print("..")
    print("...")
    time.sleep(2)
    print("""You grab your weapons and a raincoat because, let's be honest, this is a cyberpunk
game and why WOULDN'T it be raining?!""")
    time.sleep(4)
    print("Ok you've gotten to the building they're holding him in")
    time.sleep(2)
    while True: 
        choice = input("""Choose one:
        1. Scale a wall to climb through a window
        2. Try the back door
        3. DO NOT CHOOSE THIS OPTION!!!
        """)

        if choice == ("1"):
            time.sleep(1)
            if (character.agility + character.strength) > success_roll():
                print("You scale a wall and find an open window on the second floor and enter the building")
                time.sleep(2)
                print("You find yourself in a hallway. Only one door has a keypad lock on it")
                time.sleep(2)
                print("You think to yourself 'This must be the room'")
                print("You're in! You see The Hacker King tied to a chair.")
                time.sleep(2)
                print("You untie him and get the hell out of there")
                time.sleep(2)
                print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                time.sleep(3)
                print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                break
            
                # while True:
                #     open_door = input("Do you want to hack the keypad or kick the door in? Select hack or kick ")
                #     if open_door == ("h"):
                #                 if(character.hacking + character.logic) > success_roll():
                #                     print("You're in! You see The Hacker King tied to a chair.")
                #                     time.sleep(2)
                #                     print("You untie him and get the hell out of there")
                #                     time.sleep(2)
                #                     print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                #                     time.sleep(3)
                #                     print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                #                     break
                                    
                    # else:
                    #     print("You're unable to hack the keypad.")
            
                
                    # if open_door == ("k"):
                    #         if(character.agility + character.strength) > success_roll():
                    #             print("You kick the door in! You see The Hacker King tied to a chair.")
                    #             time.sleep(2)
                    #             print("You untie him and get the hell out of there.")
                    #             time.sleep(2)
                    #             print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                    #             time.sleep(3)
                    #             print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                    #             break
                        
                    #         else:
                    #             print("You're unable to kick the door in.")

            else: 
                print("You failed to enter the building through the window try again.")                    
                    
                        
                
        elif choice == ("2"):
            time.sleep(1)
            if (character.hacking + character.logic) > success_roll():
                print("It worked! You're in!")
                time.sleep(2)
                print("The first floor appears to be empty. You head up a stairwell to the second floor")
                time.sleep(2)
                print("You find yourself in a hallway. Only one door has a keypad lock on it")
                time.sleep(2)
                print("You think to yourself 'This must be the room'")
                print("You're in! You see The Hacker King tied to a chair.")
                time.sleep(2)
                print("You untie him and get the hell out of there")
                time.sleep(2)
                print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                time.sleep(3)
                print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                break
                # open_door = input("Do you want to hack the keypad or kick the door in? Select hack or kick ")
                # if open_door == ("h"):
                #     if(character.hacking + character.logic) > success_roll():
                #         print("You're in! You see The Hacker King tied to a chair.")
                #         time.sleep(2)
                #         print("You untie him and get the hell out of there")
                #         time.sleep(2)
                #         print("You untie him and get the hell out of there.")
                #         time.sleep(2)
                #         print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                #         time.sleep(3)
                #         print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                #     else:
                #         print("You're unable to hack the keypad.")
                # if open_door == ("k"):
                #     if(character.agility + character.strength) > success_roll():
                #         print("You kick the door in! You see The Hacker King tied to a chair.")
                #         time.sleep(2)
                #         print("You untie him and get the hell out of there.")
                #         time.sleep(2)
                #         print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                #         time.sleep(3)
                #         print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                #     else:
                #         print("You're unable to kick in the door.")
                
            
            else:
                print("You failed to enter the building through the back door try again.")
                
        elif choice == ("3"):
            time.sleep(2)
            print("""KOBAYASHI MARU PROTOCOL INITIATED! You walk right in the front door.
            50 Yakuza henchmen come pouring out of every door""")
            time.sleep(4)
            live_or_die = input("""Choose one
            1. Drop to your knees and surrender...
            2. Get Captain Kirk on that ass! 
            """)
            if live_or_die == ("1"):
                print("""YOU COWARD!!! They kill you and The Hacker King. Now, the Yakuza 
            control all the data in the world good job!""")
            
            
            if live_or_die == ("2"):
                print("You hit yourself with a stimulant injector and lay waste to all of them on some John Wick shit!")
                time.sleep(2)
                print("You head up a stairwell to the second floor")
                time.sleep(2)
                print("You find yourself in a hallway. Only one door has a keypad lock on it")
                time.sleep(2)
                print("You think to yourself 'This must be the room'")
                time.sleep(2)
                print("You're in! You see The Hacker King tied to a chair.")
                time.sleep(2)
                print("You untie him and get the hell out of there")
                time.sleep(2)
                print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                time.sleep(3)
                print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
            break
                # open_door = input("Do you want to hack the keypad or kick the door in? Select hack or kick ")
                # if open_door == ("h"):
                #     if(character.hacking + character.logic) > success_roll():
                #         print("You're in! You see The Hacker King tied to a chair.")
                #         time.sleep(2)
                #         print("You untie him and get the hell out of there")
                #         time.sleep(2)
                #         print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                #         time.sleep(3)
                #         print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                #     else:
                #         print("You're unable to hack the keypad.")
                # if open_door == ("k"):
                #     if(character.agility + character.strength) > success_roll():
                #         print("You kick the door in! You see The Hacker King tied to a chair.")
                #         time.sleep(2)
                #         print("You untie him and get the hell out of there.")
                #         time.sleep(2)
                #         print("You return The Hacker King Kevin Mitnick to 2600 and receive 50,000 credits")
                #         time.sleep(3)
                #         print("CONGRATULATIONS! YOU HAVE WON THE GAME! THANK YOU FOR PLAYING 'NOT CYBERPUNK 2077'!")
                #     else:
                #         print("You're unable to kick the door in.")


                


