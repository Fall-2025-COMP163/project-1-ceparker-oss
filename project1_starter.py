"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Chase Parker]
Date: [31/10/25]

AI Usage: [Document any AI assistance used]
I used AI to solve the issues for load character and save character
Example: AI helped with file I/O error handling logic in save_character function
"""
# AI USAGE:
    #I used  Ai to help figure out the issue regarding save and load character
       #Save- ensuring that the filename was corresponding to an actual argument with a file that exist and told me i forgot to add \n
       #load- I didn't had load as a dictionary and AI told me to return it as a dictionary (Also was said in instructions)
       #load- told me to return numeric values in the dictionaries as integers to correspond with their numeric values in create_character
   #I used AI for line 60 so It didn't return nothing for incorrect values in the character_class and level parameters
    
#1 I imported os to check future files, whether it be if they exist or if there actually files
import os
#2 Calculate_stats is the first bump of functions, calculating stats based on user input. 
#Calculate_stats uses the parameter “character_class” to make choices based on your class(Mage,warrior,etc). 
# This will affect the amount of health you have, the strength you have, etc with you even being able to choose your level.
#If nothing inputted, it will retruns zero (0,0,0) for the stats instead
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    booster=2
    if character_class=="Warrior":
        strength=(level*10)
        health=100
        health_equation=100-(10+strength)
        magic= (strength+health)/5
        return strength,int(magic),health_equation
    elif character_class=="Mage":
        strength=(level*2)
        health=100
        health_equation=100-(25+strength)
        magic= ((strength+health)*booster)/2
        return strength,int(magic),health_equation
    elif character_class=="Rogue":
        strength=(level*5)
        health=100
        health_equation=100-(50+strength)
        magic= (strength+(health*booster))/4
        return strength,int(magic),health_equation
    elif character_class=="Cleric":
        strength=(level*5)
        health=100
        health_equation=100-(25+strength)
        magic= (strength+health*booster)/2
        return strength,int(magic),health_equation
    
    else:
        return (0,0,0)

    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
#3 This returns a tupule of aspects (strength,int(magic),health_equation) to be used in the future

#4 Create_character is used based severely 
# on Calculate_stats, returning a dictionary that 
# will present these stats to the user. 
# This also shows why those 3 values were returned in the last function, 
# as they were used for values in our new dictionary.
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    strength,magic,health=calculate_stats(character_class,1)
    dictionary= {
        'name':name,
        'class':character_class,
        'level':1,
        'strength':strength,
        'magic':magic,
        'health':health,
        'gold':100
    }
    return dictionary
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    
#5 Save character is used to literally “save” these stats for future reference, 
# with you first needing to bypass any potential errors, ensuring that the file exists. 
# After, it saves your information to the file using the parameter filename, 
# with it being opened up, and your stats will be written in it using the write(“w”) method. 
# After being written in, it will return True if the newly created file is actually a file.
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    if "/" in filename and not os.path.exists(filename):
        return False
    with open(filename,'w') as file:
        
       file.write(f"Character Name: {character['name']}\n")
       file.write(f"Class: {character['class']}\n")
       file.write(f"Level: {character['level']}\n")
       file.write(f"Strength: {character['strength']}\n")
       file.write(f"Magic: {character['magic']}\n")
       file.write(f"Health: {character['health']}\n")
       file.write(f"Gold: {character['gold']}")
    
    
    
    if os.path.isfile(filename):
       return True
   
    

    # TODO: Implement this function
    # Remember to handle file errors gracefully
    
#6 Since your status is saved in save_character, 
# load_character will return in as a dictionary based on what's saved in the file,
# re-opening the file with these stats to perfectly imported into a new dictionary for your saved file.
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.isfile(filename):
        return None
    with open(filename,'r') as file:
       chr_dict={}
       file_read=file.readlines()
       for i in file_read:
            t=i.split(":")
            key=t[0]
            val=t[1].strip()
            if key=="Character Name":
                chr_dict["name"]=val
            elif key=="Class":
                chr_dict["class"]=val
            elif key=="Level":
                chr_dict["level"]=int(val)
            elif key=="Strength":
                chr_dict["strength"]=int(val)
            elif key=="Magic":
                chr_dict["magic"]=int(val)
            elif key=="Health":
                chr_dict["health"]=int(val) 
            elif key=="Gold":
                chr_dict["gold"]=int(val)
       return chr_dict
    # TODO: Implement this function
    # Remember to handle file not found errors
    
#7 Display_Character is what will print based on in the create_character file,
#  making it look presentable. It does this by using that returned dictionary 
# and printing them one by one using indexing to present the full stats. 
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print((f"Class: {character['class']}"))
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
   
    # TODO: Implement this function
    pass
#8 This also uses the create_character function, 
# indexing the returned dictionary to level up your stats when called, 
# with every level updating your stats more and more. 
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    
    if character['level']>=1:
        character['level']+=1
        character['strength']=character['strength']*character['level']
        character['magic']=character['magic']*character['level']
        character['health']=character['health']*character['level']
        character['gold']=character['gold']*character['level']
        return character
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    name_input=input()
    class_input=input()
    char = create_character(name_input, class_input)
    display_character(char)
    level_up(char)
    display_character(char)
    save_character(char, "character.txt")
    loaded = load_character("character.txt")
    print(loaded)
    
    
