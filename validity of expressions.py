import stack

def is_valid(expression):
    brackets_stack = stack.Stack(30)
    expression_list = expression.split()
    for i in expression_list:
        if i == "(":
            if brackets_stack.top() == "(":
                return False
            else:
                brackets_stack.push("(")
        elif i == ")":
            if brackets_stack.top() == "(":
                brackets_stack.push(")")
            else:
                return False
    return True

print(is_valid("( 3 * 3 )"))
print(is_valid("( 3 * 3 ( )"))
print(is_valid("( 3 * 3 ("))
print(is_valid(" 3 * 3 "))
print(is_valid(" 3 * 3 )"))
