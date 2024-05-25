import hashlib
import hmac
import secrets
import string

def generateSalt(length = 16):
    CHARACTERS = string.ascii_letters + string.digits
    return "".join(secrets.choice(CHARACTERS) for _ in range(length))

def _hashInternal(text, salt):
    N = 2**12
    R = 8
    P = 1
    return hashlib.scrypt(text.encode(), salt=salt.encode(), n=N, r=R, p=P).hex()

def createHash(text):
    salt = generateSalt()
    h = _hashInternal(text, salt)
    return f"{salt}${h}"
  
def checkHash(plainText, hash):
    salt, hashVal = hash.split("$",1)
    return hmac.compare_digest(_hashInternal(plainText, salt), hashVal)