
#Peter J. Mangelsdorf
#pjm349@drexel.edu
#Dr. William Mongan
#CS 265
#24 February 2019

'''Name:
        Infix to Postfix Converter and Calculator
   Description:
        The Second Assignment for CS 265. Exists as an execise in stack and string operations.
        Reads from either a cli specified file location or stdin (Linux).
        For each line of input, convert the equation to posfix format.
        For each postfix equation, calculate the answer.
        Returns both the postfix equation and the answer as a single line.'''



'''SECTION ZERO: PROGRAM DEPENDENCIES'''

#Needed for cli usage and counting arguments.
import sys



'''SECTION ONE: CALCULATOR FUNCTIONS'''

#Converts an infix notation string to a postfix notation string by inspecting each token of the equation.
def infix2postfix(infix):
    postfix = ""
    stack = []
    stack.append("(")
    postfix.append(")")
    for line in infix:
        for token in line:
            
            #Ignores Whitespaces.
            if token == " ":
                pass
            
            #Opening Parenthesis added "as-is".
            elif token == "(":
                stack.append(token)
                
            #Closing parenthesis looks for an opening parenthesis and bind the tokens within.
            elif token == ")":
                done = False
                while not done:
                    element = stack.pop()
                    if element == "(":
                        break
                    elif element != "(":
                        postfix.append(element)
                        
            #Integers are simply appended to the postfix.
            elif isinstance(token, int):
                postfix.append(token)
                
            #Lowest level operators ignore all hierarchy.
            elif token == "+" or "-":
                done = False
                while not done:
                    element = stack.pop()
                    if element == "(":
                        stack.append(element)
                        break
                    else:
                        postfix.append(element)
                        
            #Higher level operators are dependent on the presence of lowest level operators.
            elif token == "*" or "/" or "%":
                done = False
                while not done:
                    element = stack.pop()
                    if element == "(":
                        stack.append(element)
                        break
                    elif element == "-" or "+":
                        stack.append(element)
                        break
                    else:
                        postfix.append(element)

            #The unlikely event an unfriendly character is encountered.
            else:
                print("A Critical Error has Occurred on line 86. Reason: Unidentifiable Token. Token: " + str(token))
                
    #In the event the stack is not empty, notify the user.
    if len(stack) > 0:
        stack_string = ""
        for element in stack:
            stack_string.append(element)
        print("A Critical Error has Occurred on line 93. Reason: End of Expression Parsing, but Stack is not Empty. Stack: " + stack_string + " Postfix: " + postfix)
        return
    else:
        return postfix

#Evaluates a postfix notation string to an integer.
def evalPostfix(postfix):
    answer = 0
    stack = []
    x = ""
    y = ""
    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        elif token == "*":
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) * int(y)))
        elif token == "/":
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) / int(y)))
        elif token == "%":
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) % int(y)))
        elif token == "+":
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) + int(y)))
        elif token == "-":
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) - int(y)))
        elif token == "(" or ")":
            print("A Critical Error has Occurred on line 128. Reason: Unacceptable Token: ( or ).")
            break
    if len(stack) > 1:
        stack_string = ""
        for element in stack:
            stack_string.append(element)
        print("A Critical Error has Occurred on line 134. Reason: End of Expression Evaluation, but Stack has more than 1 argument. Stack: " + stack_string + " Postfix: " + postfix)
        return
    else:
        answer = int(stack[0])
        return answer



'''SECTION TWO: FILE FUNCTIONS'''

#Opens a file given a file location and returns a string of that file.
def getSysInput(location):
    with open(location) as file:
        lines = file.readlines()
    return lines

#Opens the stdin file and returns a string of it.
def getStdInput():
    file = sys.stdin
    lines = file.readlines()
    return lines



'''SECTION THREE: DATA FUNCTIONS'''

#Converts a dictionary to a plain string of keys and values.
def getStringOutput(dictionary):
    dict_string = ""
    for key in dictionary:
        dict_string.append(key + " = " + str(dictionary[key]) + "\n")
    return dict_string

#Takes infix strings, passes them to conversion, passes them to eval, and returns a dictionary.
def getAnswersDict(strings):
    answers={}
    new_eq = ""
    new_answer = 0
    for line in strings:
        new_eq = infix2postfix(line)
        new_answer = evalPostfix(new_eq)
        answers[new_eq] = new_answer
    return answers



'''SECTION FOUR: PROGRAM FUNCTIONS'''

#Manages the program. Handles calling the functions and returns the final answer.
#Accepts two methods of input: CLI arguments or stdin.
def main():
    infix_strings = ""
    if len(sys.argv) >= 2:
        infix_strings = getSysInput(sys.argv[1])
    else:
        infix_strings = getStdInput()
    print(getStringOutput(getAnswersDict(infix_strings)))
    return

#For modularity, this is the only procedural script.
if __name__ == '__main__':
    main()