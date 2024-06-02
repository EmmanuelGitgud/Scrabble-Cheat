import json

FILE = 'sorted_words.json'

points = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

with open(FILE) as f:
    words_data = json.load(f)

def calculate_points(word):
    return sum(points.get(char, 0) for char in word.upper())

def sort_words_by_points(words):
    return sorted(words, key=lambda word: (calculate_points(word), word), reverse=True)

def match(word, letters):
    for i in word:
        if letters.__contains__(i) == False:
            return False
    return True

def list_words(letters):
    results = []
    for letter in letters:
        if letter in words_data:
            words_starting_with_letter = words_data[letter]
            for word in words_starting_with_letter:
                if match(word,letters):
                    results.append(word)
    results = (sort_words_by_points(results))
    print("\nResults:\n")
    for word in results:
        print(f"{word} : {calculate_points(word)} Points")

def handle_input(user_input):
    characters = []
    for i in user_input:
        characters.append(i)
    return characters

loop = True
while loop:
    user_input = input("\nEnter characters in any order: \n")
    loop = user_input
    list_words(handle_input(user_input))
