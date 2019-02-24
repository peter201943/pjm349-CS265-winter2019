
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



'''SECTION ONE HALF: OPERATORS'''

#Adds two operands from the stack, uses next operand if error.
def stackAdd(x,y,z):
    try:
        stack_sum = str(int(y) + int(x))
    except:
        try:
            stack_sum = str(int(z) + int(x))
        except:
            stack_sum = str(int(y) + int(z))
    return stack_sum

#Subtracts two operands from the stack, uses next operand if error.
def stackSub(x,y,z):
    try:
        stack_difference = str(int(y) - int(x))
    except:
        try:
            stack_difference = str(int(z) - int(x))
        except:
            stack_difference = str(int(z) - int(y))
    return stack_difference

#Multiplies two operands from the stack, uses next operand if error.
def stackMul(x,y,z):
    try:
        stack_product = str(int(y) * int(x))
    except:
        try:
            stack_product = str(int(z) * int(x))
        except:
            stack_product = str(int(y) * int(z))
    return stack_product

#Divides two operands from the stack, uses next operand if error.
def stackDiv(x,y,z):
    try:
        stack_quotient = str(int(y) / int(x))
    except:
        try:
            stack_quotient = str(int(z) / int(x))
        except:
            stack_quotient = str(int(z) / int(y))
    return stack_quotient

#Modulates two operands from the stack, uses next operand if error.
def stackMod(x,y,z):
    try:
        stack_modulus = str(int(y) % int(x))
    except:
        try:
            stack_modulus = str(int(z) % int(x))
        except:
            stack_modulus = str(int(z) % int(y))
    return stack_modulus




'''SECTION ONE: CALCULATOR FUNCTIONS'''

#Converts an infix notation string to a postfix notation string by inspecting each token of the equation.
#A whitespace is added after each postfix appenditure to ensure ease of legibility.
def infix2postfix(infix):
    flag = False
    postfix = ""
    stack = []
    stack.append("(")
    infix += ")"
    for token in infix:
        
        #To resolve whitespace issue. Ensures numbers do not split apart.
        if flag == True:
            if token.isdigit():
                postfix += token
                token = " "
            else:
                flag = False
                postfix += " "

        #Ignores Whitespaces.
        if token == " ":
            pass
        
        #Ignores Newlines. (You have no idea how infuriating this was to debug).
        elif token == "\n":
            pass
        
        #Opening Parenthesis added "as-is".
        elif token == "(":
            stack.append(token)
            
        #Closing parenthesis looks for an opening parenthesis and binds the tokens within.
        elif token == ")":
            done = False
            while not done:
                element = stack.pop()
                if element == "(":
                    break
                elif element != "(":
                    postfix += element + " "
                    
        #Integers are simply appended to the postfix.
        elif token.isdigit():
            postfix += token
            flag = True
            
        #Lowest level operators ignore all hierarchy.
        elif token == "+" or "-":
            done = False
            while not done:
                element = stack.pop()
                if element == "(":
                    stack.append(element)
                    break
                else:
                    postfix += " " + element + " "
            stack.append(token)
            
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
                    postfix += " " + element + " "
            stack.append(token)

        #The unlikely event an unfriendly character is encountered.
        else:
            print("A Critical Error has Occurred on line 104. Reason: Unidentifiable Token. Token: " + token)
                
    #In the event the stack is not empty, notify the user.
    if len(stack) > 0:
        stack_string = ""
        for element in stack:
            stack_string += element + " "
        print("A Critical Error has Occurred on line 111. Reason: End of Expression Parsing, but Stack is not Empty. Stack: " + stack_string + " Postfix: " + postfix)
        return postfix
    else:
        return postfix

#Evaluates a postfix notation string to an integer.
def evalPostfix(postfix):
    stack = []
    x = ""
    y = ""
    while (len(postfix) != 0):
        token = postfix.pop()
        '''
        #A completely hacked together solution to an irritating problem, which would require massive overhaul.
        if token.isdigit():
            pass
        else:
            next_token = postfix.pop()
            if next_token.isdigit():
                postfix.append(next_token)
                
            next_next_token = postfix.pop()
            if next_next_token.isdigit():
                postfix.append(next_next_token)
                
            #Eliminates redundant operators.
            if (not token.isdigit()) and (next_token == token):
                pass
            
            #Eliminates redundant operators.
            if (not token.isdigit()) and (next_next_token == token):
                pass'''
            
        #Skipping the whitespaces.
        if token == " ":
            pass
    
        #Integers added "as-is" to stack.
        elif token.isdigit():
            stack.append(token)
            
            #Operators have special rules. They keep popping until an actual value is found.
            #I should probably make these things a class... Sorta did that.
        elif token == "*":
            z = 0
            x = postfix.pop()
            if x == " ":
                x = postfix.pop()
            y = postfix.pop()
            if y == " ":
                y = postfix.pop()
            try:
                z = postfix.pop()
                if z == " ":
                    z = postfix.pop()
                postfix.append(z)
            except:
                z = 0
            stack.append(stackMul(x,y,z))
        
        elif token == "/":
            z = 0
            x = postfix.pop()
            if x == " ":
                x = postfix.pop()
            y = postfix.pop()
            if y == " ":
                y = postfix.pop()
            try:
                z = postfix.pop()
                if z == " ":
                    z = postfix.pop()
                postfix.append(z)
            except:
                z = 0
            stack.append(stackDiv(x,y,z))
        
        elif token == "%":
            z = 0
            x = postfix.pop()
            if x == " ":
                x = postfix.pop()
            y = postfix.pop()
            if y == " ":
                y = postfix.pop()
            try:
                z = postfix.pop()
                if z == " ":
                    z = postfix.pop()
                postfix.append(z)
            except:
                z = 0
            stack.append(stackMod(x,y,z))
        
        elif token == "+":
            z = 0
            x = postfix.pop()
            if x == " ":
                x = postfix.pop()
            y = postfix.pop()
            if y == " ":
                y = postfix.pop()
            try:
                z = postfix.pop()
                if z == " ":
                    z = postfix.pop()
                postfix.append(z)
            except:
                z = 0
            stack.append(stackAdd(x,y,z))
        
        elif token == "-":
            z = 0
            x = postfix.pop()
            if x == " ":
                x = postfix.pop()
            y = postfix.pop()
            if y == " ":
                y = postfix.pop()
            try:
                z = postfix.pop()
                if z == " ":
                    z = postfix.pop()
                postfix.append(z)
            except:
                z = 0
            stack.append(stackSub(x,y,z))
            
            #I genuinely have no idea why "5" == ")". Anyhow, commented here for posterity's sake.
        '''#Parentheses (if any) should be acknowledged.
        elif token == "(" or ")":
            print("TOKEN: " + token)
            print("A Critical Error has Occurred on line 146. Reason: Unacceptable Token: ( or ).")
            break'''
        
    if len(stack) > 1:
        stack_string = ""
        for element in stack:
            stack_string += element + " "
        print("A Critical Error has Occurred on line 190. Reason: End of Expression Evaluation, but Stack has more than 1 argument. Stack: " + stack_string + " Postfix: " + str(postfix))
    elif len(stack) < 1:
        print("A Critical Error has Occurred on line 192. Reason: End of Expression Evaluation, but Stack is Empty. Postfix: " + str(postfix))
    else:
        return int(stack[0])



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

#An evil made necessary by my own stupidity.
#I misinterpretted the instructions and thought postfix was supposed to be a string, not a stack.
#Hence, this function is invoked.
def string2stack(string):
    stack = []
    for token in string:
        stack.append(token)
    return stack

#Converts a dictionary to a plain string of keys and values.
def getStringOutput(dictionary):
    dict_string = ""
    for key in dictionary:
        dict_string += (key + " = " + str(dictionary[key]) + "\n")
    return dict_string

#Takes infix strings, passes them to conversion, passes them to eval, and returns a dictionary.
def getAnswersDict(strings):
    answers={}
    new_eq = ""
    new_answer = 0
    new_stack = []
    for line in strings:
        new_eq = infix2postfix(line)
        new_stack = string2stack(new_eq)
        new_answer = evalPostfix(new_stack)
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

#For modularity, this is the only procedural script.
if __name__ == '__main__':
    main()