import pickle
input_file = open('phonebook.dat', 'rb')
pb = pickle.load(input_file)
print(pb)
input_file.close()

