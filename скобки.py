def is_correct_bracket_seq(sequence):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in brackets.values():  # Если открывающая скобка
            stack.append(char)
        elif char in brackets.keys():  # Если закрывающая скобка
            if not stack or stack.pop() != brackets[char]:
                return False
        else:  # Если символ не скобка
            return False

    return not stack  # True если стек пуст, иначе False


bracket_sequence = input().strip()
print(is_correct_bracket_seq(bracket_sequence))
