PlACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as data:
    invited_names = data.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PlACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


