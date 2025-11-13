import random

word_list = ["python", "java", "kotlin", "javascript"]
hangman_art = {
    0: (""),
    1: ("o"),
    2: ("o|"),
    3: ("o|/"),
    4: ("o|/\\"),
    5: ("o|/\n/"),
}


def disply_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print("".join(answer))


def main():
    answer = random.choice(word_list)
    hint = ["-"] * len(answer)
    wrong_guesses = 0
    gusssed_letters = set()
    is_running = True
    while is_running:
        disply_man(wrong_guesses)
        display_hint(hint)
        guess = input("Input a letter: ").lower()
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if guess in gusssed_letters:
            print("You've already guessed this letter.")
            gusssed_letters.add(guess)
            continue
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                else:
                    wrong_guesses += 1
        if ("_") not in hint:
            disply_man(wrong_guesses)
            display_answer(answer)
            print("You guessed the word!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            disply_man(wrong_guesses)
            display_answer(answer)
            print("You lost!")
            is_running = False


if __name__ == "__main__":
    main()
