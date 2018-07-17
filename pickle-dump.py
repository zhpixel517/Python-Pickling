import pickle

# Pickling is a way to restore lost data from variables and such from files

answer = input("Enter something: ")

# Loads inputed data to a file called 'pickle-data'

f = open('pickle-data' , 'wb')
pickle.dump(answer , f)
f.close()
