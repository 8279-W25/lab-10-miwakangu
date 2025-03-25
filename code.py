import time
import board
import adafruit_circuitplayground.express as cp

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

def display_morse_on_cpx(morse_list, unit_time, color):
    """Displays the Morse code on the CPX LEDs."""
    if not cp.pixels.n:
        print("Circuit Playground Express not detected.")
        return

    cp.pixels.fill((0, 0, 0))  # Turn off all LEDs initially
    cp.pixels.brightness = 0.5  # Set brightness

    dot_duration = unit_time
    dash_duration = 3 * unit_time
    char_space_duration = 3 * unit_time
    word_space_duration = 7 * unit_time

    if color == "red":
        led_color = (255, 0, 0)
    elif color == "green":
        led_color = (0, 255, 0)
    elif color == "blue":
        led_color = (0, 0, 255)
    elif color == "yellow":
        led_color = (255, 255, 0)
    elif color == "purple":
        led_color = (255, 0, 255)
    elif color == "cyan":
        led_color = (0, 255, 255)
    else:
        led_color = (255, 255, 255) # Default to white

    for item in morse_list:
        if item == '.':
            cp.pixels.fill(led_color)
            time.sleep(dot_duration)
            cp.pixels.fill((0, 0, 0))
            time.sleep(dot_duration)
        elif item == '-':
            cp.pixels.fill(led_color)
            time.sleep(dash_duration)
            cp.pixels.fill((0, 0, 0))
            time.sleep(dot_duration)
        elif item == ' ':
            time.sleep(char_space_duration)
        elif item == '   ':
            time.sleep(word_space_duration)
        time.sleep(0.01) # Small delay to prevent blocking

def main_cpx():
    """Main function for the CPX to get input and display Morse code."""
    morse_dict = get_morse_code_dict()

    while True:
        try:
            unit_str = input("Enter the length of a unit (0 to 1 seconds): ")
            unit_time = float(unit_str)
            if 0 <= unit_time <= 1:
                break
            else:
                print("Unit time must be between 0 and 1 second.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        color = input("Enter LED color (red, green, blue, yellow, purple, cyan, or other for white): ").lower()
        if color in ["red", "green", "blue", "yellow", "purple", "cyan", "other"]:
            break
        else:
            print("Invalid color. Please enter a valid color name.")

    sentence = input("Enter a sentence for Morse code: ")
    processed_sentence = process_sentence(sentence, morse_dict)
    morse_list = sentence_to_morse_list(processed_sentence, morse_dict)
    print("Generating Morse code...")
    display_morse_on_cpx(morse_list, unit_time, color)
    print("Morse code displayed on CPX.")

if __name__ == "__main__":
    main_cpx()