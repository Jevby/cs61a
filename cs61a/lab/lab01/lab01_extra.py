"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    star = 1
    if k <= n:
        while k > 0:
            star *= n
            k -= 1
            n -= 1
    else:
        print("error")

    return star             
    
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        now_num = n % 10
        next_num = n // 10 % 10
        if now_num == 8 and next_num == 8:
            return True
        else:
            n //= 10

    return False       

# Guessing Game

from random import randint

LOWER = 1
UPPER = 10

def guess_random():
    """Guess randomly and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)   # asks the user to choose a number
    num_guesses, correct = 0, False
    while not correct:
        guess = randint(LOWER, UPPER) # randomly guess
        correct = is_correct(guess)   # ask user if guess is correct
        num_guesses = num_guesses + 1
    return num_guesses

def guess_linear():
    """Guess in increasing order and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    guess = LOWER
    "*** YOUR CODE HERE ***"
    correct = is_correct(guess)
    if correct:
        return num_guesses
    if guess <= 10:
        while not correct:
            guess += 1
            correct = is_correct(guess)
            num_guesses += 1
    else:
        print("guesses error")
    return num_guesses 

def guess_binary():
    """Return the number of attempted guesses. Implement a faster search
    algorithm that asks the user whether a guess is less than or greater than
    the correct number.

    Hint: If you know the guess is greater than the correct number, then your
    algorithm doesn't need to try numbers that are greater than guess.
    """
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    lower, upper = LOWER, UPPER
    guess = (lower + upper) // 2
    "*** YOUR CODE HERE ***"
    while not is_correct(guess):
        if is_too_high(guess):
            upper = guess - 1
        else:
            lower = guess + 1
        guess = (lower + upper) // 2
        num_guesses += 1
    return num_guesses
    # correct = is_correct(guess)
    # high = is_too_high(guess)
    # middle = (lower + upper) // 2   #1~10 middle is 5
    # while not correct:
    #     if not high:
    #         guess = (lower + guess) // 2
    #         high = is_too_high(guess)
    #         correct = False
    #         num_guesses += 1
    #     else:
    #         guess = (upper + guess) // 2
    #         high = is_too_high(guess)
    #         correct = is_correct(guess)
    #         num_guesses += 1
    
    # return num_guesses

# Receive user input. You do not need to understand the code below this line.

def prompt_for_number(lower, upper):
    """Prompt the user for a number between lower and upper. Return None."""
    is_valid_number = False
    while not is_valid_number:
        # You don't need to understand the following two lines.
        number = input('Pick an integer between {0} and {1} (inclusive) for me to guess: '.format(lower, upper))
        number = int(number)
        if lower <= number <= upper:
            is_valid_number = True

def is_correct(guess):
    """Ask the user if a guess is correct and return whether they respond y."""
    return is_yes('Is {0} your number? [y/n] '.format(guess))

def is_too_high(guess):
    """Ask the user if a guess is too high and return whether they say yes."""
    return is_yes('Is {0} too high? [y/n] '.format(guess))

def is_yes(prompt):
    """Ask the user a yes or no question and return whether they say yes."""
    while True: # This while statement will loop until a "return" is reached.
        yes_no = input(prompt).strip()
        if yes_no == 'y':
            return True
        elif yes_no == 'n':
            return False
        print('Please type y or n and press return/enter')