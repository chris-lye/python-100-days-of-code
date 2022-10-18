#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []


with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as file:
    all_lines  = file.read()
    for name in names:
        name = name.strip()
        output = all_lines.replace("[name]", name)
        print(name)
        with open(f"./Output/ReadyToSend/letter_for{name}.txt", "w") as final_letter_file:
            final_letter_file.write(output)
        