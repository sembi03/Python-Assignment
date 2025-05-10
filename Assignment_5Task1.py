
my_dict = {'Alice':60,'Mike':70,'Hari':50,'Ram':70}

a = input('Enter the student name: ')

if a in my_dict == my_dict:
    print(a,"\'s mark is",my_dict[a])
else:
    print('Student not found')