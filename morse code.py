#First, let's grab a morse code dictionary.
#I chose to make all of the letters uppercase,
#and will print out a decoded answer in title case.
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

#let's make a Translator class for this

class Translator:
    #we init with self, and our dictionary
    def __init__(self, morse_code_dict):
        self.dict = morse_code_dict
    def encode(self,text):
        #empty list to hold the morse in
        morse = []
        #iterate through the letters in text
        for char in text:
            #make them all uppercase
            upper_char = char.upper()
            #append the upper characters if they are in the dictionary
            #to our morse list
            if upper_char in self.dict:
                morse.append(self.dict[upper_char])
            #and add a space between multiple words (if applicable)
            elif char == ' ':
                morse.append(' ')
                #then return our morse list, joined with a space between
                #the letters for clear printing later
        return ' '.join(morse)



    def decode(self,code):
        #here we must iterate through the list and switch
        #our values and keys using the items() function
        self.reverse_dict = {v:k for k,v in self.dict.items()}
        #here we split the codes with another space for clarity
        words = code.split('   ')
        #and hold the decoded word in an empty list
        decoded_words = []
        #iterate over the split code (words)
        for morse_word in words:
            #then split the morse_word with a space
            morse_letters = morse_word.split(' ')
            #and hold our decoded letters
            decoded_letters = []
            #now to iterate over our morse letters
            for morse_letter in morse_letters:
                #find it in the reverse dictionary
                if morse_letter in self.reverse_dict:
                    #and append the morse letter to our decoded_letters list
                    decoded_letters.append(self.reverse_dict[morse_letter])
                    #we pass if the letter is blank
                elif morse_letter == " ":
                    pass
                else: #and we return a ? if it isn't a letter
                    decoded_letters.append('?')
            #then append the word list with the decoded letters
            decoded_words.append(''.join(decoded_letters))
            #and return the word
        return ' '.join(decoded_words)


translator = Translator(morse_code_dict)
text = 'Oregon Trail'
encoded = translator.encode(text)
print(f"Original text: {text}")
print(f"Morse Code: {encoded}")

code = '--- .-. . --. --- -.   - .-. .- .. .-..'
decoded = translator.decode(code)
print(f"Original Code: {code}")
print(f"Decoded Word: {decoded.title()}")
