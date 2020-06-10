import string
import secrets

# Generates a random string of alphanumeric characters, with at least
# one upper-case letter, one lower-case letter, and three numbers.
# Use the 'digits' input parameter to request the length of the
# randomized string.  Note that, because of the uppercase/lowercase/3 numbers requirement,
# the requested string must be at least 5 characters.
# See this page for more:  https://docs.python.org/3/library/secrets.html
def generateCode(digits):
    if not type(digits) is int:
        raise TypeError("The 'digits' input parameter must be an integer -- the length of the requested string.")

    if digits < 5:
        raise Exception ("The 'digits' input parameter must be at least 5.") 

    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(digits))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def testGenerateCode():
    test16 = generateCode(16)
    print(test16)
    test5 = generateCode(5)
    print(test5)

    input("press a key")

def testGenerateTwenty5DigitCodes():
    for x in range(20):
        print(generateCode(5))

#testGenerateTwenty5DigitCodes()
