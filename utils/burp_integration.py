import requests

def send_to_burp(payload, api_url="http://127.0.0.1:8080"):
    try:
        requests.post(f"{api_url}/burp/repeater", json={"payload": payload})
        return True
    except:
        return False
