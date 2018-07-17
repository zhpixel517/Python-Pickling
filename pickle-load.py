import pickle

# The following program loads the data back into the program

f = open('pickle-data', 'rb')
new_answer = pickle.load(f)
f.close()
print("It works! You said: " + new_answer)

