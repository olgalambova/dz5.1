
import string
my_user_name = input("Enter your username: " " ")
print(my_user_name[0].startswith('_'),
      my_user_name[0].isdigit(),
      my_user_name[1:].isalnum(),
      my_user_name[0].islower(),
      my_user_name[:].islower(),
      my_user_name[1:].isalpha())



















