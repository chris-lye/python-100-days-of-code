import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("day26-NATO-alphabet/nato_phonetic_alphabet.csv")
nato_alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    user_word = input("Enter a word: \n")
    if user_word == "exit":
        break
    letter_list = [letter for letter in user_word] # extraneous 
    output = [nato_alpha_dict[letter.upper()] for letter in letter_list ]
    print(output)