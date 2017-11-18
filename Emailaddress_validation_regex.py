import re



input = "asdf@gh......om"

def valid_email(input):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.match(pattern,input):
        return 1
    else:
        return 0

print valid_email(input)
