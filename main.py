import pandas as pd

morse = pd.read_csv('morse.csv')
morse_dict = morse.set_index('LETTER')['CODE'].to_dict()


def conv_text():
    text = input("Please enter text to covert: ").upper()

    for char in text:
        if char in morse_dict:
            text = text.replace(char, f"{morse_dict[char]} ")
    print(f"The morse code is: \n{text}")


def conv_morse():
    text = input("Please enter text to covert: ").split()

    words = [key for i in text for key, value in morse_dict.items() if value == i]
    converted = ''.join(words)
    print(f"The text is: \n{converted}")


def main():
    convert = input("What would you like to convert? Text (T) or Morse (M): ").upper()

    if convert == "T":
        conv_text()
    elif convert == "M":
        conv_morse()
    else:
        print("Please enter either T or M")
        main()


run = True

while run:
    main()
    another = input("Would you like to convert another? (Y or N) ").upper()
    if another == "Y":
        run = True
    else:
        run = False
        print("Thanks for using my Converter!")
