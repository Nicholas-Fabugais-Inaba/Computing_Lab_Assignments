#!/usr/bin/env python
# coding: utf-8

# # Computing 8 Assignment
# 
# 

# ---
# ## Background
# 
# Object oriented programming languages are often used when designing and developing complex systems such as video games. Objects are used to represent various aspects of the game such as players, enemies, items, maps, etc. **Role-playing** video games are a common genre of video games where users control the actions of a player or character. These games often involve some form of combat in addition to the player having attributes such as health, levels, damage, etc. In this assignment, you will be implementing a **Player** class for a video game. Our player class will keep track of the following features:
# 
# -	The player’s name
# -	The player’s health
# -	The player’s current level
# -	The player’s current “score”
# -	The score required to reach the next level
# -	The player’s set of attacks
# 
# In addition to the **Player** class, you will be implementing a function that will use the **Player** class. Please thoroughly read the requirements section to understand how to implement the methods and function!

# ---
# ## NOTE THAT YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Test plan
#  - Exception handling
# 

# ---
# ## Program Requirements (12 Marks)
# ---
# ### Requirements - Player Class
# 
# The requirements for the **Player** class are given below. Please ensure that your methods have the EXACT naming as specified! Failure to do so will result in lost marks. 
# 
# ***Note: you must include a try and except statement in at least one function in your code.***
# 
# 1.	Create an **\_\_init\_\_**(*name*) method that takes the following arguments:
# 
#     -	***name***: A *string* representing the name of the player. The variable is assigned to an instance variable. If *name* is an empty string, the instance variable is set to the string **"Default"**.
#     
#     The method also initializes the following instance variables:
#     
#          **a.**	An *int* representing the player’s health. The player’s health is initially set to **100**.  
#          **b.**	An *int* representing the player’s level. The player’s initial level is **0**.  
#          **c.**	An *int* representing the player’s current score. The player’s initial score is **0**.  
#          **d.**	An *int* representing the score required to reach the next level. The initial value is **50**.  
#          **e.**	A *list of lists* representing the current set of attacks. Each sub-list has a length of **2**. The first element is a *string* that represents the name of the attack and the second element is an *int* representing the strength of the attack. A player has **3** different attacks. The player’s initial attacks are provided below:
# 
# 
# <center>[["Fast attack",5],["Slow attack",15],["Default Special Attack",20]]</center>
# 
# 2.	Create the following **accessor** methods:
# 
#     **a.**	**get_name**: Returns the player’s name.  
#     **b.**	**get_health**: Returns the player’s health.  
#     **c.**	**get_level**: Returns the player’s level.  
#     **d.**	**get_score**: Returns the player’s current score  
#     **e.**	**get_next_lvl_score**: Returns the score required to reach the next level.   
#     **f.**	**get_attacks**: Returns the player’s attack set.  
# 
# 
# 3.	Create the **mutator** method **raise_health**(*val*).  
# 
#     -	***val***: An *int*.  
#     -	**Method description**: The method does not return anything, but increases the player’s health by ***val***. If the ***val*** is negative, the method does nothing. The player's health cannot exceed 100 so if the sum of their current health and ***val*** exceeds 100, then set health to 100. 
# 
# 
# 4.	Create the **mutator** method **replace_attack**(*i*, *name*, *strength*).
#     -	***i***: An *int* representing an index (either 0, 1, or 2).
#     -	***name***: A *string* representing the name of an attack.
#     -	***strength***: An *int* representing the strength of the attack associated with ***name***.
#     -	**Method description**: The method replaces the list at index **i** in the attack list instance variable with a *list* of length 2 where the first element is ***name*** and the second element is ***strength***.
# 
# 
# 5.	Create the **mutator** method **take_damage**(*quantity*). 
#     -   ***quantity***: An *int*.
#     -   **Method description**: The method deducts ***quantity*** from the instance variable that stores the players health. The player’s health is set to 0 if ***quantity*** is greater than or equal to the player’s current health.
# 
# 
# 6.	Create the **mutator** method **perform_attack**(*i*, *player_2*).
#     -   ***i***: An *int* representing an index. Assume that the value must be either 0,1, or 2.
#     -   ***player_2***: A *Player* object.
#     -   **Method description**: The method simulates a user attack on ***player_2*** using the attack at index ***i*** from the attack instance variable list of lists. The method performs the following actions:
# 
#         - *player_2*’s health is calculated and stored in a variable.
#         - The object calling the method uses the attack associated with index *i* from the current set of attacks to inflict damage on *player_2* (i.e *player_2* will take damage equal to attack i’s strength).
#         - The difference between *player_2*’s current health and *player_2*’s health before the attack is calculated and stored in the variable *damage_given*.
#         - The value of *damage_given* is added to the player’s current score if the sum of *damage_given* and current score will result in a value less than the instance variable containing the score required to reach the next level.
#         - If the sum of *damage_given* and player score results in a value equal to or higher than the score required to reach the next level, then the following actions are performed
#             - a. The player’s level is increased by **1**. 
#             - b. The player’s current score is set to **0**.
#             - c. The score required to reach the next level is increased by **20**.
#             - d. Each of the player's attack strengths are increased by **5**.

# ---
# ### Requirements - Battle Simulation
# 
# In addition to the **Player** class, you are required to implement a function to simulate a battle. The function definition is given below:
# 
# 1.	Create the function **simulate_battle**(*player_1*, *player_2*, *player_1_moves*, *player_2_moves*).
#     - ***player_1***: A *Player* object.
#     - ***player_2***: A *Player* object.
#     - ***player_1_moves***: A *list* of integers where each element is between 0 and 2 (inclusive).
#     - ***player_2_moves***: A *list* of integers where each element is between 0 and 2 (inclusive).
#     - ***Method Description***: The function performs the following algorithm:
#         - For each element i in *player_1_moves*, *player_1* attacks *player_2* using the *perform_attack* method with attack i. If *player_2*'s health becomes 0 at any point, *player_1* wins the battle.
#         - Then, for each element i in *player_2_moves*, *player_2* attacks *player_1* using the *perform_attack* method with attack i. If *player_1*'s health becomes 0 at any point, *player_2* wins the battle.
#         
#         Note: *All* Player 1 attacks should occur first before *all* Player 2 attacks 
#     - ***Return***: A *string* representing the name of the player object that won the battle. If there is no winner, an empty string is provided.

# ---
# ## Implementation
# Please define the Player class in the cell below.

# In[10]:


class Player:                           #creates a class called player, where different methods, such as accessors and
                                        #mutators will be created
    def __init__(self, name):           #Note: each method has self as a parameter that allows a variable to set, get, and
        try:                            #modify itself
            if len(name) != 0:          #the try and except statement checks if an empty string is used in the method and if
                self.name = name        #not, the name used in the method will be assigned to a Player object.
            else:                       #for an empty string, the name for the Player object will just become "Default"
                raise ValueError        #the rest of the Player object's attributes are then initialized
        except ValueError:
            self.name = "Default"
        self.health = 100
        self.level = 0
        self.score = 0 
        self.next_lvl_score = 50
        self.attacks = [["Fast attack",5],["Slow attack",15],["Default Special Attack",20]]
    
    def get_name(self):                 #each get method represents an accessor type of method that will be able to access
        return self.name                #data attributes connected to a specific Player object
        
    def get_health(self):
        return self.health
        
    def get_level(self): 
        return self.level
        
    def get_score(self): 
        return self.score
        
    def get_next_lvl_score(self): 
        return self.next_lvl_score
        
    def get_attacks(self): 
        return self.attacks

    def raise_health(self, val):        #with the variable 'val' being used in the method, if it is a negative number,
        if val < 0:                     #it will not raise the health of a Player object's health, and if the variable when
            pass                        #added to the Player object's health is over 100, because the max health someone can
        elif (val + self.health) > 100: #have is 100, their health will instead be set to 100. If the number is not negative
            self.health = 100           #or a number that will make the Player object's health exceed 100, 'val' will
        else:                           #just be added to the Player object's health
            self.health += val
        
    def replace_attack(self, i, name, strength):  #using an integer from 0-2, and the name and strength of an attack,
        self.attacks[i] = [name, strength]        #the attack at the index position of the integer will be switched out
                                                  #with a new name and strength of an attack as used in the method
    def take_damage(self, quantity):    #from a quantity inputted into the method, if the quantity is able to make a Player
        if quantity >= self.health:     #object's health negative, it will instead be set to 0 as that is the minimum health
            self.health = 0             #a Player object can have. Otherwise, the quantity will be used as a number deducted
        else:                           #from a Player object's health
            self.health -= quantity
    
    def perform_attack(self, i, player_2):                        #using an integer from 0-2 and the Player object that will
        player_2_health = player_2.get_health()                   #be attacked, the Player object's health being attacked
        player_2.take_damage(self.attacks[i][1])                  #will be retrieved from the accessor and set to a variable,
        damage_given = player_2_health - player_2.health          #the Player object being attacked will then utilize the
        if (damage_given + self.score) < self.next_lvl_score:     #take_damage() method, then the damage taken will be set 
            self.score += damage_given                            #to the variable "damage_given". If "damage_given" and 
        elif (damage_given + self.score) >= self.next_lvl_score:  #the Player object's score that dealt the damage is less
            self.level += 1                                       #than the score needed to achieve the next level, the
            self.score = 0                                        #"damage_given" will just be added to the Player object's
            self.next_lvl_score += 20                             #score that performed the attack. Else if the "damage_given" 
            for i in range(len(self.attacks)):                    #plus the Player object's score that performed the attack
                self.attacks[i][1] += 5                           #is greater than or equal to get to the next level,
                                                                  #increase their level by 1, set their score to 0, increase
                                                                  #the score to get to the next level by 20 and increase the
                                                                  #strength of each attack by 5


# Please define the battle simulation function in the cell below.

# In[11]:


def simulate_battle(player_1, player_2, player_1_moves, player_2_moves):
    for i in range(len(player_1_moves)):                    #using 2 different Player object's and their attacks, run
        player_1.perform_attack(i, player_2)                #through each attack by player_1 and if at any point player_2's
        if player_2.health == 0:                            #health equals 0, return the winner of the battle and after
            return (player_1.get_name())                    #running through all of player_1's attacks, run through all of
    for j in range(len(player_2_moves)):                    #player_2's attacks unless player_1's health is equal to 0 as
        player_2.perform_attack(i, player_1)                #then player_2 will be returned as the winner
        if player_1.health == 0:                            #and if there is no winner after all the attacks are run through
            return (player_2.get_name())                    #return the winner as an empty string
    return ""
    


# ---
# ## Sample Output
# Use the following cell to test out your code!

# In[19]:


print("----TESTING PLAYER CREATION----")
colin = Player("Colin")
bosco = Player("Bosco")
colin_name = colin.get_name()
bosco_name = bosco.get_name()
print("Two players created with names:",colin_name,"and",bosco_name)

print("\n")
print("----TESTING ATTACK MODIFICATION----")
print(colin_name+"'s Attacks:",colin.get_attacks())
i = 2
new_attack = "1P13 Exam"
strength = 50
print("Changing",colin_name,"attack",i,"to",new_attack)
colin.replace_attack(i,new_attack,strength)
print(colin_name+"'s Attacks:",colin.get_attacks())

print("\n")
print("----TESTING PLAYER ATTACK----")
print(bosco_name+"'s current score:",bosco.get_score())
print(bosco_name+"'s score required to reach next level:",bosco.get_next_lvl_score())
print(colin_name+"'s health:",colin.get_health())
i=1
print(bosco_name,"will perform an attack on",colin_name,"with move",bosco.attacks[i])
print("...")
bosco.perform_attack(i,colin)
print(bosco_name+"'s current score:",bosco.get_score())
print(bosco_name+"'s score required to reach next level:",bosco.get_next_lvl_score())
print(colin_name+"'s health:",colin.get_health())

print("\n")
print("----TESTING BATTLE----")
b_moves = [0,1,2]
c_moves = [0,2,1,2]
print(bosco_name+"'s moves:",b_moves)
print(colin_name+"'s moves:",c_moves)
print(bosco_name,"will be the first to attack...")
winner = simulate_battle(bosco,colin,b_moves,c_moves)
print("Battle has finished, winner is",winner)
print(bosco_name+"'s health:",bosco.get_health())
print(colin_name+"'s health:",colin.get_health())


# The expected output from the previous cell is given below:
# 
# <code>
# ----TESTING PLAYER CREATION----
# Two players created with names: Colin and Bosco
# </code>
# <code>
# ----TESTING ATTACK MODIFICATION----
# Colin's Attacks: [['Fast attack', 5], ['Slow Attack', 15], ['Default Special Attack', 20]]
# Changing Colin attack 2 to 1P13 Exam
# Colin's Attacks: [['Fast attack', 5], ['Slow Attack', 15], ['1P13 Exam', 50]]
# </code>
# <code>
# ----TESTING PLAYER ATTACK----
# Bosco's current score: 0
# Bosco's score required to reach next level: 50
# Colin's health: 100
# Bosco will perform an attack on Colin with move ['Slow Attack', 15]
# ...
# Bosco's current score: 15
# Bosco's score required to reach next level: 50
# Colin's health: 85
# </code>
# <code>
# ----TESTING BATTLE----
# Bosco's moves: [0, 1, 2]
# Colin's moves: [0, 2, 1, 2]
# Bosco will be the first to attack...
# Battle has finished, winner is Colin
# Bosco's health: 0
# Colin's health: 45
# </code>

# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on variable names, commenting and exception handling.<br>
# The mark breakdown is as follows:<br>
# > 2 marks for using appropriate variable names that indicate what is being stored in that variable<br>
# 2 marks for leaving comments on major parts of your code such as where you read the file or calculate a summation<br>
# 2 marks for exception handling. Your functions should produce the required outputs even when receiving unexpected inputs

# ---
# ## Test Plan (6 Marks)
# Develop a test plan for your program. Your test plan should have at least **three** test cases: one normal case, one boundary case, and one abnormal case. You can test any function/method but you must test **at least two different** functions/methods. Please use the following format for your test cases:
# 
# **Function:**   
# **Input:**  
# **Output:**  
# **Expected Output:**  
# **Pass/Fail:**  
# 
# An example test case is shown below:  
# ```
# Function: replace_attack(self, i, name, strength)
# Input: p = Player("")
#        p.replace_attack(0,"weak",2)
#        print(p.get_attacks() == [["weak",2],["Slow Attack",15],["Default Special Attack",20]])
#        
# Output: True
# Expected Output: True
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# ```
# Function: replace_attack(self, i, name, strength)
# Input: p = Player("Jim")
#        p.replace_attack(0,"Strong Attack",25)
#        print(p.get_attacks() == [['Strong Attack', 25], ['Slow attack', 15], ['Default Special Attack', 20]])
# 
# Output: True
# Expected Output: True
# Pass/Fail: Pass
# 
# Function: raise_health(self, val)
# Input: hr = Player("Toby")
#        hr.raise_health(131)
#        print(p.get_health())
# 
# Output: 100
# Expected Output: 100
# Pass/Fail: Pass
# 
# Function: get_name(self)
# Input: weird = Player("")
#        print(weird.get_name())
# 
# Output: Default
# Expected Output: Default
# Pass/Fail: Pass
# 
# ```

# ---
# ## Reflective Questions
# 
# 1. In the Program Requirements, the ***raise_health()*** mutator was specified to have 1 argument, but when you defined it, the mutator was defined to accept 2 parameters. What is the purpose of the first parameter? What happens if we omit this parameter?
# 
# 
# 2. Suppose we had a method ***rename_player(self,name)*** that renames your player object with *name*. Would this method be an accessor or mutator?
# 
# 
# 3. Is it possible to test that ***raise_health()*** works correctly using a single python statement (i.e. using a single line of code)?
# 
# Please answer all questions in the cell below!

# ```
# 1. The purpose of the first parameter is to provide the ability to reference an instance of a class' object, essentially referencing itself. Without the self parameter to refer to itself that provides the ability to set, get, and modify attributes, you would not be able to do anything with a class' object's attributes.
# 2. This would be a mutator as you would be modifying an attribute rather than retrieving it like an accessor method would do.
# 3. No, this is not possible as the raise_health() method does not return anything, which means you would not know if anything would change. You would then need to use the get_health() method to then see if the health had changed or not as that would provide a way to test the method.
# 
# 
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 8 dropbox on avenue with the naming convention: macID_CL8.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely recieve zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
