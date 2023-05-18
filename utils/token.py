from base64 import urlsafe_b64decode, urlsafe_b64encode
from json import dumps, loads

def tokenEncode(data):
    string = str(dumps(data))
    encode = string.encode('utf-8')
    result = urlsafe_b64encode(encode).rstrip(b'=')
    return result.decode('utf-8')

def tokenDecode(data):
    encode = data.encode('utf-8')
    padding = b'=' * (4 - (len(encode) % 4))
    string =  urlsafe_b64decode(encode + padding)
    return loads(string.decode('utf-8'))