import stack
    

#def precedence(operator):
 #   if operator == "*" or operator == "/": return 1
  #  if operator == "+" or operator == "-": return 0

#operators = ["*","/","+","-","(",")"]
precedences = {"*":1,"/":1,"+":0,"-":0,"(":2}

def infix2postfix(expression):
    operators_stack = stack.Stack(10)
    expression_list = expression.split()
    postfix = ""
    print(expression_list)
    for i in expression_list:

        if i == "(":
            operators_stack.push(i)
        elif i == ")":
            while operators_stack.top() != "(":
                postfix += operators_stack.pop()
            operators_stack.pop()

        elif i in precedences:
            #print("operator")
            if operators_stack.is_empty():
                operators_stack.push(i)
                #print(stack.stack)
            elif precedences[i] <= precedences[operators_stack.top()]:
                #print(stack.pop())
                while not operators_stack.is_empty() and precedences[i] <= precedences[operators_stack.top()] and operators_stack.top() != "(":
                    postfix += operators_stack.pop()
                operators_stack.push(i)
            elif precedences[i] > precedences[operators_stack.top()]:
                operators_stack.push(i)

        else:
            postfix += i

        operators_stack.display()


    while not operators_stack.is_empty():
        postfix += operators_stack.pop()

    return postfix

print(infix2postfix("a * b + ( b - a ) / c"))