from multiprocessing.sharedctypes import Value
from pydoc import doc
import random 

def calculate_distance(*args, **kwargs):
    """
    multiply: for multiplication
    add : For addition
    subtract : For subtraction
    divide : For division
    """
    if kwargs["operation"] == "add":
        print(sum(args))
    elif kwargs["operation"] == "multiply":
        print(sum(args) * 10)

value = input("Perform your calculation ")

print(eval())

