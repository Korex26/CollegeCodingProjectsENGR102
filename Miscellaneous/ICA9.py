text = open('para.txt', 'r')
TEXT = open('para_C.txt', 'w')
line = text.readline()
while line != '':
    LINE = line.upper()
    TEXT.write(LINE)
    line = text.readline()
text.close()
TEXT.close()





