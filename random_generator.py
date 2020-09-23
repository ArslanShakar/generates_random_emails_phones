import random
from unique_id import get_unique_id

"""
Please install this library/module using Terminal: 
Command: pip install unique-id
"""


class RandomGenerator:
    total_phones_limit = 100000
    ph_country_code = '+92'
    ph_location_digit = '1'
    ph_digits_limit = 10

    total_emails_limit = 100000
    email_custom_text = 'a'

    email_domains = [
        'gmail.com',
        'front',
    ]

    symbols = [
        '_', '',
        # '!', '#', '$', '%', '&', "'", '*', '+', '-',
        # '/', '=', '?', '^', '{', '|', '}', '~',
    ]

    def __init__(self):
        self.generate_emails()
        self.generate_phones()

    def generate_emails(self):
        email_file = open("emails_321.txt", "w")
        excluded_chars = ":*^`\",.~;%+-'@=#!$%&()/\\|<>?{}[]_0123456789"
        count = 0

        for i in range(0, self.total_emails_limit):
            uni_str = get_unique_id(length=8, excluded_chars=excluded_chars)
            digits = self.get_random_num(length=3)

            for dom in self.email_domains:
                for sym in self.symbols:
                    if count > self.total_emails_limit:
                        return
                    count += 1

                    # "{custom_letter}{random alphabets}{allowed symbol}{digits}@{domain-name}"
                    email = "{}{}{}{}@{}".format(self.email_custom_text, uni_str, sym, digits, dom).capitalize()
                    email_file.write(email + '\n')

                    more_chars = get_unique_id(length=self.get_random_digit(), excluded_chars=excluded_chars)
                    if sym:
                        # Adt3_sd@
                        email = "{}{}{}{}{}@{}".format(self.email_custom_text, uni_str, digits, sym, more_chars, dom).capitalize()
                        email_file.write(email + '\n')
                    else:
                        # 1344dfg@
                        email = "{}{}{}{}@{}".format(self.email_custom_text, uni_str, digits, more_chars, dom).capitalize()
                        email_file.write(email + '\n')

                    print(email)

    def generate_phones(self):
        phones_file = open(f"phones_321.txt", "w")
        random_digits_limit = int(len(self.ph_country_code.strip('+')) + len(self.ph_location_digit))
        random_digits_limit = self.ph_digits_limit - random_digits_limit - 1
        random_digits = '0' * random_digits_limit
        start = int('{}{}'.format(self.ph_location_digit, random_digits))
        excluded_chars = ":*^`\",.~;%+-'@=#!$%&()/\\|<>?{}[]_asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM"
        phones = []

        for ph in range(0, self.total_phones_limit):
            # start += 1
            # phone = "{} {}{}".format(self.ph_country_code, self.ph_location_digit, start)

            r1 = get_unique_id(length=random_digits_limit, excluded_chars=excluded_chars)
            phone = "{} {}{}".format(self.ph_country_code, self.ph_location_digit, r1)

            # r1 = get_unique_id(length=random_digits_limit-3, excluded_chars=excluded_chars)
            # r2 = get_unique_id(length=3, excluded_chars=excluded_chars)
            # r2 = self.get_random_num(2)
            # r3 = self.get_random_digit(end=9)
            # phone = "{} {}{}{}{}".format(self.ph_country_code, self.ph_location_digit, r1, r2, r3)

            phones_file.write(phone + '\n')
            phones.append(phone)
            print(phone)

        # print(len(phones), len(set(phones)))

    def get_random_digit(self, start=0, end=5):
        return random.randrange(start, end)

    def get_random_num(self, length=3):
        _min = pow(10, length - 1)
        _max = pow(10, length) - 1
        return random.randint(_min, _max)


RandomGenerator()
