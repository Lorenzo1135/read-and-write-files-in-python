# # remember to fork this and push to github


# f = open('employees.txt', 'r')
# f.write("you thought i was feeling you?")
# print(f.read())
# #read gives us everything.readline reads first line

with open("test.txt" , 'r') as f:
  for line in f:
    print(line,end='')
  # # f.read()
  # print(f)