import re
a = "o\xe2\x80\xa6"
print(re.sub(r'[a-zA-Z0-9]*', "hello", a))
print(re.sub(r'\\*', "abc", a))
print(re.sub(r'([a-zA-Z0-9]*\\)+', "", a))