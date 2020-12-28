"""
    Copyright (C) 2020  Basaac, piz2a

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import functions


bracket_error = SyntaxError('Unmatching parenthesis')


def check_iterable(obj):
    try:
        if type(obj) == str:
            raise TypeError
        iter(obj)
    except TypeError:
        return False
    return True


def pdqobsiois(obj):  # Put double quotes on both sides if obj is string
    return f'"{obj}"' if type(obj) == str else f'{obj}'


def split_code(code, split=';'):  # Splits code (default ";")
    is_string = False
    brackets = []
    result = []
    temp = ''
    for char in code:
        if char == '"':
            is_string = not is_string
        elif char in '({[':
            brackets.append('({['.index(char))
        elif char in ')}]':
            if len(brackets) == 0:
                raise bracket_error
            if ')}]'.index(char) == brackets[-1]:
                brackets.pop()
            else:
                raise bracket_error
        if char in split and not is_string and brackets == []:  # 이때 split
            result.append(temp)
            result.append(char)
            temp = ''
        else:
            temp += char
    result.append(temp)
    if result == ['']:
        return []
    return result


def set_variables(lang, command):
    # 변수의 값을 지정하는지 확인
    split = split_code(command, '=')
    # print(split)
    if len(split) != 3:
        return 1

    if split[0] not in lang.variable_names:
        return 1
    lang.variables[split[0]] = pdqobsiois(evaluate(split[2], lang))

    return 0


def evaluate(string, lang):
    # print(string)

    # 함수인지 판단
    if len(string) >= 3 and \
            string[1] == '(' and string[-1] == ')':
        if string[0] not in functions.functions:
            raise NameError("Invalid function")
        args = [evaluate(arg, lang) for arg in split_code(string[2:-1], ',')]
        if not check_iterable(args):
            args = (args,)
        # print(f'args: {args}')
        # print("function return value:", repr(functions.functions[string[0]](*args)))
        return functions.functions[string[0]](*args)

    # declare variables using exec()
    for key in lang.variables:
        value = lang.variables[key]
        exec(f'{key}={value}')

    # check operators
    operators = '+-*/%^|&><'
    items = split_code(string, operators)
    if len(items) == 1:  # 연산자가 없다면
        return eval(string)
    new_items = items[:]
    for index, item in enumerate(items):
        if item not in operators:
            new_items[index] = '' if item == '' else pdqobsiois(evaluate(item, lang))
    return eval(''.join(new_items))
