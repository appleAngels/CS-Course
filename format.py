f1 = open("/Users/yueqian/Desktop/code/CS-Course/input.txt","r")
# print(f1.read())

data = []
for line in f1.readlines():
  newLine = ''
  if(len(line) > 2):
    # print(line[-2])
    if((line[-1] == '\n' and (line[-2] == '.' or line[-2] == '?'))):
      data.append(line)
    else:
      # print(222)
      data.append(line.strip() + ' ')

f2 = open("/Users/yueqian/Desktop/code/CS-Course/output.txt", "w")
f2.write(''.join(data))
f2.close()
f1.close()