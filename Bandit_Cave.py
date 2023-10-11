#Author: Aliczander Haas
#Date Written: TBA
#Final Project
import tkinter
#Import the required Libraries
from tkinter import *
from tkinter import ttk
from random import randint
#Create an instance of Tkinter frame
bCave= Tk()

# Declares murder as false, if it is later made true, it disallows or allows certain endings
Murderer1 = False
Murderer2 = False
Genocide = False

# Makes a new Window
def enter_Cave():
    caveR1 = tkinter.Toplevel()
    caveR1.geometry("750x250")
    caveR1.title = ('The Bandit Cave - Room 1')
    # Create Button(s)
    Label(caveR1, text="The caves entrance is dark \nTorches mounted shoddily on the walls illuminate the mess broken carts and shields forming a makeshift barricade\n Towards the back of the cave sits a man in a chair seemingly writing something down, he doesn't seem to notice you.").pack(pady=20)
    Button(caveR1, text=("Sneak Past him.\n(High Success)"), width = 20, command = Sneak).pack(pady=0)
    Button(caveR1, text=("Announce yourself.\n(Medium Success)"), width = 20, command = Alert).pack(pady=0)
    Button(caveR1, text=("Attack him.\n(Combat)"), width = 20, command = CombatBlind).pack(pady=0)

# Makes a new Window
def Sneak():
    sneakint = randint(1,10)
    Sneak = tkinter.Toplevel()
    Sneak.geometry("750x250")
    Sneak.title = ('The Bandit Cave - Room 1')
    # Create a Button(s) and responses based on randint roll
    if sneakint >= 2:
        Label(Sneak, text="You sneak past the man, without any problems. \nYou take a look at his book, its just scribbles. \nThe desk is covered in even more scribbles, can this guy even see? ").pack(pady=20)
        Button(Sneak, text="Move to the next room.", width=20, command=CaveR2).pack(pady=0)
    else:
        Label(Sneak, text="The man notices you! \nHe is however, blind, and hits you with a broom before you move on.").pack(pady=20)
        Button(Sneak, text="Move to the next room, slightly saddly.", width=20, command=CaveR2).pack(pady=0)

# Makes a new Window
def Alert():
    alertint = randint(1, 10)
    Alert = tkinter.Toplevel()
    Alert.geometry("750x250")
    Alert.title = ('The Bandit Cave - Room 1')
    # Create Button(s) and responses based on randint roll
    if alertint >= 5:
        Label(Alert, text="You tell him your looking to join their Band of Brigands and he shakes his head.  \n'Get 'yerself movin' then! Boss's been lookin' fer more 'cruits! Down the hall to the left!'").pack(pady=20)
        Button(Alert, text="Get 'yerself movin'!", width=20, command=CaveR2).pack(pady=0)
    else:
        Label(Alert, text="You tell him that you're a strapping lad looking for bounty, booty, and brigandry! \nHe doesn't buy it. \n 'Yous a merkanary, ain't cha'? Boss's over through that there hall.' \nHe points behind him to a blank wall, you assume he meant to point deeper into the cave.").pack(pady=20)
        Button(Alert, text="Move forward, dejectedly.", width=20, command=CaveR2).pack(pady=0)

# Makes a new Window
def CombatBlind():
    playerCombatint = randint(1, 10)
    CombatBlind = tkinter.Toplevel()
    CombatBlind.geometry("750x250")
    CombatBlind.title = ('The Bandit Cave - Room 1')
    # Create Button(s) and responses based on randint roll
    if playerCombatint <=3:
        Label (CombatBlind, text="You go to swing your sword and miss horribly! The man looks over at you, dissapointed. \n'Boss's down that'a way hero' He points to the wall behind him, presumably meaning to point deeper. \n You notice his eyes are glassed over, he must be blind.").pack(pady=20)
        Button(CombatBlind, text="Go deeper. \nAttemped murder, look at you.", width=20, command=CaveR2).pack(pady=0)
    elif playerCombatint >=4 and playerCombatint<=9:
        Label(CombatBlind, text="You go to swing your sword and he moves at the last moment you end up cutting into his arm pretty badly. \n'DAMN! That hurts! I'm just a guard, Boss's 'ver there, you inbred ninnyhammer!' \n He points deeper into the cave.").pack(pady=20)
        Button(CombatBlind, text="Move forward!", width=20, command=CaveR2).pack(pady=0)
        Button(CombatBlind, text="Finnish him off!", width=20, command=Finisher).pack(pady=0)
    else:
        Label(CombatBlind, text="You swing your sword and in one cleave, the man's head is cleanly seperated from his body. \n As his head rolls you notice his eyes are glassed over, nice job killing a blind guy. \n Douche.").pack(pady=20)
        # Makes Murderer True, disallowing the pacafist ending
        Murderer1 = True
        Button(CombatBlind, text="Progress Deeper. \nMurderer.", width=20, command=CaveR2).pack(pady=0)

# Makes a new Window
def Finisher():
    Finisher = tkinter.Toplevel()
    Finisher.geometry("750x250")
    Finisher.title = ('The Bandit Cave - Room 1')
    # Create Button(s)
    Label(Finisher,text="You quickly go to stab him and he falls over his desk, dead.").pack(pady=20)
    # Makes Murderer True, disallowing the pacafist ending
    Murderer1 = True
    Button(Finisher, text="Progress Deeper. \nMurderer.", width=20, command=CaveR2).pack(pady=0)

# Makes a new Window
def CaveR2():
    CaveR2= tkinter.Toplevel()
    CaveR2.geometry("750x250")
    CaveR2.title = ('The Bandit Cave - Room 2')
    # Create Button(s)
    Label(CaveR2, text="The next room seems to be the main chamber. In the middle sit three men around a large fire. They haven't seen you. \nOne of them stand out as wearing what looks like a suit of cobbled together plate armour from scrap metal, he must be the leader.\nThree logs have been placed to try and keep the cobbled roof from caving in, it wouldn't take much to break one of them \nYou could also try casting a spell, although you were'nt very good in spellcasting back in school.").pack(pady=20)
    Button(CaveR2, text = "Forget Planing! \nCHARGE! \n(Combat)", width=20,).pack(pady=0)
    Button(CaveR2, text="Shoot an arrow to \ndislodge one of the logs. \n(High Success)", width=20, ).pack(pady=0)
    Button(CaveR2, text="Magic Maaaaaaan! \n(????? Success)", width=20, ).pack(pady=0)
    Button(CaveR2, text="Reason with them? \n (Low Success)", width=20,).pack(pady=0)



# Makes a new Window and warns players
label=Label(bCave, text="The mouth of a cave looms before you, Enter the Bandit Cave? \n WARNING! \n BANDIT CAVE CONTAINS FOUL LANGUAGE AND DEPICTS VIOLENCE! \n ALTHOUGH NOT GRAPHIC PLAY AT YOUR OWN DISCRETION! \nWARNING!")
label.pack()
# Set the geometry of Tkinter frame (I will not be puting this above all of them)
bCave.geometry("750x250")
# Create Button(s)
Button(bCave, text="Yes!", width= 20, command = enter_Cave ).pack(pady=20) # Oh yeah its bandit caving time!
Button(bCave, text="Turn Back.", width= 20, command = bCave.destroy).pack(pady=20) # Makes you leave, like a coward.

# makes loops the windows so they don't automatically close
bCave.mainloop()