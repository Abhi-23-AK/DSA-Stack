stack = []

# push
stack.append(10)

# pop
stack.pop()

# peek
top = stack[-1] if stack else None

# isEmpty
is_empty = len(stack) == 0
