import re

pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
roman_num = input()
result = re.match(pattern, roman_num) != None

print(result)
