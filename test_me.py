# Это будет кодирование 


# далее необходимо представить её в бинарном виде
def binary_representation(string):
    binary_string = ''
    for char in string:
        binary_string += format(ord(char), '08b')
    return binary_string

text = input() # входная строка
print(binary_representation(text))