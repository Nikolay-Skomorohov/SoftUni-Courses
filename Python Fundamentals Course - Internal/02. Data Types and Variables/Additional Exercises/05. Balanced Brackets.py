balanced = None
last_paran = None

n = int(input())

for i in range(n):
    line = input()
    if line == '(' and last_paran is None:
        last_paran = '('
    elif line == ')' and last_paran is None:
        balanced = False
        break
    elif line == '(' and last_paran is not None:
        if last_paran == '(':
            balanced = False
            break
        elif last_paran == ')':
            last_paran = ')'
            balanced = True
    elif line == ')':
        if last_paran == '(':
            balanced = True
        elif last_paran == ')':
            balanced = False
            break
if balanced is True:
    print('BALANCED')
else:
    print('UNBALANCED')
