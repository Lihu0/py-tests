import fileinput

# dosen't work with vscode extion for python
for line in fileinput.input('words.txt'):
    print(f'> {line}', end='')