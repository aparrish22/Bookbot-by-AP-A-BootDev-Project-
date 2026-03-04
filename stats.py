def get_number_of_words(text):
    return len(text.split())

# takes text from the book as a string,
# and returns the number of times each character
# (excluding symbols and spaces) appears in the string
# convert any character to lowercase because we do not want duplicates
def get_character_counts(text):
    character_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

def sort_on(items):
    return items[1]

# take dictionary of characters and their counts and
# returns a sorted list of dictionaries
def get_sorted_character_counts(character_counts):
    sorted_character_counts = sorted(character_counts.items(), key=sort_on, reverse=True)
    return sorted_character_counts