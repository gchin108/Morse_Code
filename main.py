code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",

    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
    "\"": ".-..-.", "$": "...-..-", "@": ".--.-.", " ": "/"
}


def encode(input_text):
    morse_code = []
    for texts in input_text:
        if texts in code:
            morse_code.append(code[texts])
    # prints code separated by space
    print(' '.join(morse_code, ))


def decode(morse_code):
    def get_key_from_value(dictionary, target_value):
        for key, value in dictionary.items():
            if value == target_value:
                return key
        return None

    # turn code into a list, separated by space
    lst = morse_code.split(' ')
    words = []
    for n in lst:
        words.append(get_key_from_value(dictionary=code, target_value=n))
    result = ''.join(words)
    print(result.title())


def methods():
    method = input("\nEncode or Decode? Type 'quit' to exit\n").lower()
    if method == 'encode':
        text = input('Enter the words\n').upper()
        encode(text)
        methods()
    elif method == 'decode':
        mc = input("\nEnter morse code, please separate each code by a space\n")
        try:
            decode(mc)
        except TypeError:
            print("Invalid Entry")
            methods()
        else:
            methods()
    elif method == 'quit':
        print('Good Bye!')
        exit()
    else:
        print("Invalid Entry.")
        methods()


print("Hello, this is a Morse Code Translator")
methods()
