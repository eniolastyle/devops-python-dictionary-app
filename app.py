import json

def load_dictionary():
    try:
        with open("dictionary.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_dictionary(dictionary):
    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file, indent=4)

def display_definition(word, definitions):
    print(f"\nDefinitions for '{word}':")
    if definitions:
        for i, definition in enumerate(definitions, start=1):
            print(f"{i}. {definition}")
    else:
        print("No definitions found for the entered word.")

def search_word(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        similar_words = []
        for term in dictionary:
            if word in term.lower():
                similar_words.append(term)
        if similar_words:
            print(f"Word '{word}' not found. Did you mean:")
            for i, similar_word in enumerate(similar_words, start=1):
                print(f"{i}. {similar_word}")
        else:
            print(f"No definitions found for the entered word '{word}'.")

        return []

def add_word(dictionary):
    word = input("Enter the new word: ")
    definition = input("Enter the definition: ")
    dictionary[word.lower()] = [definition]
    print(f"'{word}' has been added to the dictionary.")

def display_all_words(dictionary):
    print("\nList of available words:")
    for word in sorted(dictionary.keys()):
        print(word)

def save_and_exit(dictionary):
    save_dictionary(dictionary)
    print("Dictionary has been saved. Exiting the app.")
    exit()

def dictionary_app():
    dictionary = load_dictionary()

    while True:
        print("\nCloud/DevOps Dictionary App")
        print("1. Search word")
        print("2. Add word")
        print("3. Display all words")
        print("4. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            word = input("Enter the word to search: ")
            definitions = search_word(word, dictionary)
            display_definition(word, definitions)
        elif choice == "2":
            add_word(dictionary)
        elif choice == "3":
            display_all_words(dictionary)
        elif choice == "4":
            save_and_exit(dictionary)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    dictionary_app()
