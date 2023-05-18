import hashlib
import secrets
import string

from database.links import hashExists

def generateHash(string):
    return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()

def generateVerificationCode(length = 6):
    return ''.join(secrets.choice(string.digits) for i in range(length))

def hashedVerificationCode(code):
    return generateHash(code)

def checkVerificationCode(userCode, code):
    return True if generateHash(userCode) == code else False

def generateLinkHash(length=4):
    CHARACTERS = string.ascii_letters + string.digits
    while True:
        hash = ''.join(secrets.choice(CHARACTERS) for i in range(length))
        exists = hashExists(hash)
        if exists:
            continue
        else:
            return hash