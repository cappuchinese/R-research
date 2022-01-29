#!/usr/bin python3

# imports
from random import randint as rdi
import math

# globals
formula_list = []


# Plus/minus questions
def plus_minus_questions():
    """
    create the plus and minus questions
    :return:
    """
    for i in range(6):
        number1 = rdi(10, 99999)
        number2 = rdi(10, 99999)
        if i < 3:
            answer = number1 + number2
            calculation = "{} + {} = {}".format(number1, number2, answer)
        else:
            answer = number1 - number2
            calculation = "{} - {} = {}".format(number1, number2, answer)
        formula_list.append(calculation)


# Multiplying/division questions
def multiplication_questions():
    """
    create the multiplication questions
    :return:
    """
    for i in range(2):
        number1 = rdi(10,999)
        number2 = rdi(10,999)
        answer = number1 * number2
        calculation = "{} * {} = {}".format(number1, number2, answer)
        formula_list.append(calculation)


def division_questions():
    """
    create the division questions
    :return:
    """
    for i in range(2):
        number1 = rdi(1,100)
        number2 = rdi(1,100)
        answer = number1 * number2
        calculation = "{} / {} = {}".format(answer, number2, number1)
        formula_list.append(calculation)


def squared_question():
    """
    create a squared question
    :return:
    """
    num = rdi(5, 20)
    answer = num ** 2
    calculation = "{} ^2 = {}".format(num, answer)
    formula_list.append(calculation)


def sqrt_questions():
    """
    create square root question
    :return:
    """
    num = rdi(1, 10)
    squared = num ** 2
    answer = math.sqrt(squared)
    calculation = "[root]{} = {}".format(squared, answer)
    formula_list.append(calculation)


def write_txt(filename, formula_list):
    """
    function writes txt file
    :param filename: input from console
    :param formula_list: the math questions
    :return:
    """
    fileopen = open(filename, "w")
    for item in formula_list:
        fileopen.write("{}\n".format(item))
    fileopen.close()


def main():
    """
    main function: create all the questions
    :return: .txt file with math questions
    """
    filename = input("Please put in a filename, no .txt required: ") + ".txt"
    plus_minus_questions()
    multiplication_questions()
    division_questions()
    squared_question()
    sqrt_questions()
    write_txt(filename, formula_list)


if __name__ == "__main__":
    exit(main())
