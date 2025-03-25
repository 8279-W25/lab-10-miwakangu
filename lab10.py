def get_morse_code_dict():
    """Returns the Morse code dictionary."""
    return {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }

def process_sentence(sentence, morse_dict):
    """Converts a sentence to lowercase and removes invalid characters."""
    processed_sentence = ""
    for char in sentence.lower():
        if char in morse_dict:
            processed_sentence += char
        elif char == ' ':
            processed_sentence += ' '  # Keep spaces for word separation
    return processed_sentence

def sentence_to_morse_list(processed_sentence, morse_dict):
    """Converts a processed sentence into a list of Morse code elements."""
    morse_list = []
    for word in processed_sentence.split():
        for i, char in enumerate(word):
            if char in morse_dict:
                morse_list.append(morse_dict[char])
                if i < len(word) - 1:
                    morse_list.append(' ')  # Space between characters
        if word:
            morse_list.append('   ')  # Space between words
    return morse_list

def display_morse_list(morse_list):
    """Prints the Morse code list in a readable format."""
    output = ""
    for item in morse_list:
        if item == ' ':
            output += " (char) "
        elif item == '   ':
            output += " (word) "
        else:
            output += item
    print(f"Morse Code Representation: {output}")

def main():
    """Main function to get user input and perform the conversion."""
    morse_dict = get_morse_code_dict()
    sentence = input("Enter a sentence: ")
    processed_sentence = process_sentence(sentence, morse_dict)
    morse_list = sentence_to_morse_list(processed_sentence, morse_dict)
    display_morse_list(morse_list)

if __name__ == "__main__":
    main()