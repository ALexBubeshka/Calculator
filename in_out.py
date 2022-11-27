def parse_math_expression(exp):
    PRECENDENCE = {
        ')': 3,
        '(': 3,
        '*': 1,
        '/': 1,
        '+': 0,
        '-': 0,
    }
    output = []
    operators = []
    for ch in exp:
        if ch == ')':
            opr = operators.pop(0)
            while opr != '(':
                output.append(opr)
                opr = operators.pop(0)
        elif ch.isdigit():
            output.append(ch)
        else:
            top_op = None
            if len(operators) and operators[0]:
                top_op = operators[0]
            if top_op in ['*', '/'] and PRECENDENCE[top_op] > PRECENDENCE[ch]:
                output.append(top_op)
                operators.pop(0)
            operators.insert(0, ch)
    while len(operators):
        output.append(operators.pop(0))
    return output


def eval_parsed_expression(exp):
    OPRS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    tmp = []
    while len(exp) > 1:
        k = exp.pop(0)
        while not k in ['*', '-', '+', '/']:
            tmp.insert(0, k)
            k = exp.pop(0)
        o = k
        b = tmp.pop(0)
        a = tmp.pop(0)
        r = OPRS[o](float(a), float(b))
        exp.insert(0, r)
    return exp[0]


def simple_num(user_input):
    user_input = user_input.replace(" ", "")
    exp_list = parse_math_expression(user_input)
    print(eval_parsed_expression(exp_list))


def complex_num(user_input):
    user_input = user_input.replace(" ", "")
    complex_n = eval(user_input)
    print(complex_n)


user_input = input("Введите арифметическое выражение: ")
simple_num(user_input)
# complex_num(user_input)