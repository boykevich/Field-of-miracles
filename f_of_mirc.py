import random as rn


def field_of_miracles() -> str:
    words = \
        (
            "apple",
            "banana",
            "book",
            "hill",
            "beat",
            "goal",
            "night",
            "whisper",
            "lion",
            "monkey"
        )
    correct_word = rn.choice(words)
    hidden = (['*' for _ in range(len(correct_word))])
    counter = 0
    attempts = int(input("Enter amount of attempts to guess: \n"))

    while counter < attempts:
        is_changed = False
        counter += 1
        guess = str(input("Guess the letter or word: "))

        if len(guess) > 1:
            return "You guessed, congratulation!" if guess == correct_word else "Your word is wrong"

        for i in range(len(hidden)):
            if correct_word[i] == guess:
                hidden[i] = guess
                is_changed = True

        if is_changed:
            counter -= 1
            print(f"{''.join(hidden)}\n")
        else:
            print("There is no such letter\n")

        if ''.join(hidden) == correct_word:
            return "You guessed, congratulation!"

    return f"Your attemps have ended, it's a pity you didn't guess the word.\nThe correct word was: {correct_word}"


print(field_of_miracles())
