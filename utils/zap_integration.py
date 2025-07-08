from zapv2 import ZAPv2

def send_to_zap(payload, proxy="http://127.0.0.1:8080"):
    try:
        zap = ZAPv2(proxies={'http': proxy})
        zap.urlopen(payload)
        return True
    except:
        return False
