import random
import operator

def user_guess():
    guess_from = None
    guess_to = None

    while guess_from is None:
        try:
            guess_from = int(input('Enter the first number: '))
        except ValueError:
            print('Please, enter a valid input')

    while guess_to is None:
        try:
            guess_to = int(input('Enter the second number: '))
        except ValueError:
            print('Please, enter a valid input')
    
    return guess_from, guess_to 


def run_quiz():
    user_input1, user_input2 = user_guess()

    total_question = 10

    while total_question > 0:
        random_num1 = random.randint(user_input1, user_input2)
        random_num2 = random.randint(user_input1, user_input2)


        Operator = {
            '*': operator.mul,
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv
        }

        Operator_choice = random.choice(list(Operator.keys()))

        Operator_function = Operator[Operator_choice]

        user_answer = None
        correct_answer = Operator_function(random_num1, random_num2)


        while user_answer is None:
            try:
                user_answer = int(input(f"{random_num1} {Operator_choice} {random_num2}: "))
            except ValueError:
                print("Please, enter an appropriate value for the answer.")

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print('Incorrect🤦‍♂️')

        total_question -= 1


run_quiz()