
# Part 2: Application of Custom Data Structures for algorithms

# 1 (Reverse Sentence):
def reverse_words(sentence):
    stack=[]
    reverse_sentence=[]
    for char in sentence:
        if char!=' ':
            stack.append(char)
        else:
            word=''
            while stack:
                word=stack.pop()+word

            reverse_sentence.append(word)
            reverse_sentence.append(' ')

    word=''
    while stack: 
        word=stack.pop()+word
    reverse_sentence.append(word)    
    
    return ''.join(reverse_sentence[::-1])


# 2 (Postfix Calculator):
def postfix_calculator():
    stack=[]
    while True:
        user_Input=input("Enter a number,operator(? for stack,^ for top element,! for exit)")
        if(user_Input=="?"):
           print(stack)
        elif (user_Input=="!"):
            print("Exiting...")
            exit()
        elif(user_Input=="^"):
            if stack:
               print("Stack: ",stack[-1])
            else:
               print("Stack is empty")
        else:
            if user_Input.isdigit() or (user_Input.startswith("-")) and (user_Input[1:].isdigit()):
               stack.append(int(user_Input))
            elif  user_Input in ["+","%","-","*","/"]:
                if len(stack) < 2:
                  print("Error: Not enough operands")
                  continue
                operand2 = stack.pop()
                operand1 = stack.pop()
                if user_Input == "+":
                   result = operand1 + operand2
                elif user_Input == "-":
                   result = operand1 - operand2
                elif user_Input == "*":
                   result = operand1 * operand2
                elif user_Input == "/":
                    if operand2 == 0:
                      print("Error: Division by zero")
                      stack.append(operand1)
                      stack.append(operand2)
                      continue
                    else:
                       result = operand1 / operand2
                elif user_Input=="%":
                   result=operand1%operand2
                stack.append(result)
      
print(reverse_words(" I am from University of Engineering and Technology Lahore"))
postfix_calculator()

