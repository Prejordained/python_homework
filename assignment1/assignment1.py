#Task 1
def hello ():
    return "Hello!"

print (hello())

#Task 2
def greet(name):
    return f"Hello, {name}!"

print (greet("Jordan"))

#Task 3
def calc(a, b, operation = "multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
         return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc (13, 0, "divide"))

#Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    
print(data_type_conversion(16, "float"))

#Task 5

def grade(*args):
    try:
        average =  sum(args)/len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
print(grade(95, 80, 65))

#Task 6

def repeat(str, count):
    result = ""
    for i in range(count):
        result = result + str
    return result

print(repeat("bye", 3))

#Task 7
def student_scores(result, **kwargs):
    if result == "mean":
        total = sum(kwargs.values())
        count = len(kwargs.values())
        return total/count
    elif result == "best":
        best_student = "" 
        best_score = 0
        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = name
        return best_student
    
print(student_scores("mean", David=79, Amber=91, Sarah=85))
print(student_scores("best", David=79, Amber=91, Sarah=85))

#Task 8

def titleize(string):
    little_words = ["a", "an", "on", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)
    

print(titleize("only thing we have to fear is fear itself"))

#Task 9

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result = result + letter
        else:
            result = result + "_"
    return result

print(hangman("pringle", "in"))

#Task 10

def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while word[i] not in vowels:
                i += 1
            result.append(word[i:] + word[:i] + "ay")
    return " ".join(result)

print(pig_latin("you arer the only exception"))