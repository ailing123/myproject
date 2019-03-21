#!/usr/bin/env python
# coding: utf-8

# In[56]:


# 3/21

def player():
    print("You are in a land full of dragons. In front of you, you see two caves.\nIn one cave, the dragon is friendly and will share his treasure with you.\nThe other dragon is greedy and hungry, and will eat you on sight.")
    playerchoice=input("Which cave would you go into? (1 or 2)")
    
    if playerchoice=='1':
        print("")
        print("You approach a cave...")
        print("It is dark and spooky....")
        print("A large dragon jumps out infront of you! He opens his jaw and ....")
        print("Gobbles you dwon in one bite!")
        playagainornot=input("Do you want play again? (Y or N)")
    
    elif playerchoice=='2':
        print("")
        print("You approach a cave...")
        print("Surprise!")
        print("You meet a friendly dragon")
        playagainornot=input("Do you want play again? (Y or N)")

    if playagainornot=='Y':
        print("")
        player()
    
        

player()

    


# In[ ]:




