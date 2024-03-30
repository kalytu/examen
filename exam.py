import random

def load_words():
    
    return ["полуниця", "авто", "клей", "телефон", "папір", "шкарпетки", "собака"]

def choose_word(word_list):
    return random.choice(word_list)

def main():
    print("вітайємо у грі слова!")
    words = load_words()
    current_word = choose_word(words)
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        display_word = ""
        for letter in current_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("слово:", display_word)
        print("кількість спроб:", attempts)
        
        guess = input("введіть літеру: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("ви вгадали літру!")
            elif guess in current_word:
                print("вітаю!ви вгадали літру")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in current_word):
                    print("вітаю! ви перемогли! слово було '{}'.".format(current_word))
                    break
            else:
                print("нажаль, такої літри не було у слові")
                attempts -= 1
        else:
            print("будь ласка, введіть тільки одну літеру")
    
    if attempts == 0:
        print("нажаль, ви програли. слово було '{}'.".format(current_word))

if __name__ == "__main__":
    main()