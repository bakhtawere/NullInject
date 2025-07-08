import base64
import urllib.parse

def encode(payload, method):
    if method == "base64":
        return base64.b64encode(payload.encode()).decode()
    elif method == "url":
        return urllib.parse.quote(payload)
    elif method == "hex":
        return ''.join(f'%{ord(c):02x}' for c in payload)
    return payload
