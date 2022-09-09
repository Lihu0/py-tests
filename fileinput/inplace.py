import fileinput

# work only in pycharm
for line in fileinput.input('inplace.txt', inplace='True'):
    line += '1'