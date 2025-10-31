[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21274966&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge


What Is This?:
Welcome traveler! Welcome to the beginning of the character creation journey, as you've been assigned to create a character and its class (Warrior: High strength,low magic,and high health).
When you choose your class your stats are created using formulas. My inspiration for these formulas was to ensure that some stats for your class influenced others aspects with your level determining your strength and your health and magic being influenced to this factor as well. 

AI:
I used AI to help figure out the issue regarding saving and loading characters.
Save- ensuring that the filename corresponded to an actual argument with a file that exists and told me I forgot to add \n
Load- I didn't have load as a dictionary, and AI told me to return it as a dictionary (Also was said in instructions)
Load- told me to return numeric values in the dictionaries as integers to correspond with their numeric values in create_character
I used AI for line 60 to ensure my algorithm didn't return “nothing” for incorrect values in the character_class and level parameters. returning (0,0,0)

How To Run:
	It's simple: input your name and the class you want, and your stats will be presented.
​
What happens?:
Your character is created and then displayed using those respected functions.
After, you level up instantly with your new stats being presented
Finally, your character is then saved in “character.txt” and then loaded back to show how load works, printing your loaded stats.



How It Works (deeper look):

In this project, you are assigned to create your own fictional character. Though not as expansive as one would think, it's a start, as you're given options to select your name and your class out of four options: Warriors,Mages,Rogues,and Clerics. With each respective role given, you're given your statistics with said class (EX: Warrior: High strength,low magic,and high health). These stats are given based on created formulas to calculate these aspects, and when done, the function calculate_stats returns this as a tuple of your strength, magic, and health. create_character is what's run next, as you're told to create a dictionary resembling these stats, including your name,class,level,strength,magic,gold,and health. This is done using the calculate_stats function, as it uses the returned items from the function to create the values for this dictionary.
​
After these stats are created, files can be incorporated into the equation, starting with save_character. With save_character, this function will save your stats into a file for future purposes. This is done using the open() method, opening or creating a file to read,write,or append information. In this case, we must write(.write(),”w”) the created stats into the file filename (argument=”character.txt”). Load_character is after, returning a list based on your saved file using read(read(),readlines(),“r”).
​
Finally, for the display function, printing the returned list from create_character to print these results to the user interface. These stats can also be updated based on level_up, which upgrades your stats based on your level.
