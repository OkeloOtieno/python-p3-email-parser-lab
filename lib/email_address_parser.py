import re

class EmailAddressParser:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def __init__(self, email):
        self.email = email

    def parse(self):
        strings =  re.split(r',|\s', self.email)


        parsed_email = set()
        for string in strings:
            if self.regex.fullmatch(string):
                parsed_email.add(string)

        return sorted(list(parsed_email))