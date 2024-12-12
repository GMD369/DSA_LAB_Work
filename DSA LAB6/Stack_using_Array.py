# Implement Stack using Array:

stack=[None,None,None,None,None,None,None]
top=-1
size=7

# PUSH function:
def push(value):
    global top,size
    if top>=size-1:
        print("Stack is full")
    else:
        top+=1
        stack[top]=value
        
# POP function
def Pop():
    global top
    if top==-1:
        print("Stack is empty")
    else:
        value=stack[top]
        stack[top]=None
        top-=1
        return value

# TOP or PEEK function:
def Top():
    if top==-1:
        print("Stack is empty")
    else:
        return stack[top]

push(10)
push(4)
push(23)
push(34)
push(33)
push(35)
pop1=Pop()
print(pop1)
print(Top()) 

print(stack)
