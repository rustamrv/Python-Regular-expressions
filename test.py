import re
 
#pattern = r'[A-Z]{3}' # мое
pattern = r'\w+$'  
text = 'Subsribe to Python insider via RSS'
print(re.findall(pattern,text))

#pattern = r'\b[a-zA-Z]{2}' #мое
pattern = r'\b\w.'
text = 'Subsribe to Python insider via RSS'
print(re.findall(pattern,text))

#pattern = r'@[a-z].{0,9}'
pattern = r'@\w+.\w+'
pattern1 = r'@\w+.(\w+)'
text = 'my.test@mail.ru, my@gmail.com, admin_test@list.ru, support.python@python.biz'
result = re.findall(pattern,text)
print(result)

result1 = re.findall(pattern1,text)
print(result1)

pattern = r'\d{2}-\d{2}-\d{4}'
pattern1 = r'\d{2}-\d{2}-(\d{4})'
text = 'Amit 35-3557 25-04-2017, XYZ 56-4633 23-01-2014, ABC 68-8064 28-02-2016'
result = re.findall(pattern,text)
print(result)

res = re.findall(pattern1,text)
print(res)

pattern = r'[8-9]{1}[0-9]{9}'
text = ['8123456-1230', '9123456789', '912345x1234']
for value in text:
    if re.match(pattern, value) and len(value) == 10:
        print("yes")
        print(re.findall(pattern,value))
    else:
        print("no")
