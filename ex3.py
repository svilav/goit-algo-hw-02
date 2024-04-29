def check_brackets(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if brackets[top] != char:
                return "Несиметрично"

    if stack:
        return "Несиметрично"

    return "Симетрично"


expressions = [
    "( ){[ ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in expressions:
    print(f"{expr}: {check_brackets(expr)}")
