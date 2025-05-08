try:
    file1=open('sample.txt','r')
    read_file = file1.read()
    print(read_file)
    file1.close()

except FileNotFoundError:
    print("The file 'sample.txt' was not found")




