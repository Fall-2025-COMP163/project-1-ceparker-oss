"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Chase Parker]
Date: [31/10/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os
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
    elif character_class=="Rouge":
        strength=(level*5)
        health=100
        health_equation=100-(50+strength)
        magic= (strength+(health*booster))/4
        return strength,int(magic),health_equation
    elif character_class=="Clerics":
        strength=(level*5)
        health=100
        health_equation=100-(25+strength)
        magic= (strength+health*booster)/2
        return strength,int(magic),health_equation
    

    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

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
        "chr_name":name,
        "chr_class":character_class,
        "level":1,
        "strength":strength,
        "magic":magic,
        "health":health,
        "gold":100
    }
    return dictionary
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    

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
    with open(filename,'w') as file:
       file.write(f"Character Name: {character['chr_name']}\n")
       file.write(f"Class: {character['chr_class']}\n")
       file.write(f"Level: {character['level']}\n")
       file.write(f"Strength: {character['strength']}\n")
       file.write(f"Magic: {character['magic']}\n")
       file.write(f"Health: {character['health']}\n")
       file.write(f"Gold: {character['gold']}")
  
    if os.path.isfile(filename):
       return True
    else:
       return False
    

    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    
    
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

   
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    char = create_character("TestHero", "Warrior")
    print(char)
    #display_character(char)
    print(save_character(char, "my_character.txt"))
    #loaded = load_character("my_character.txt")
