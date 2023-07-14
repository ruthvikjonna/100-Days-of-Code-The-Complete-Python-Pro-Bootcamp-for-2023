import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

continue_asking = True
while continue_asking == True:
    word = input("\nEnter a word: ").upper()
    output = [data_dict[i] for i in word]
    print(output)
    keep_going = input("\nDo you wish to enter another word? Type 'yes' to continue or 'no' to exit: ").lower()
    if keep_going == "yes":
        continue_asking = True
    elif keep_going == "no":
        continue_asking = False