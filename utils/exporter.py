import json
from datetime import datetime

def export_json(payload, filename="output/payloads.json"):
    with open(filename, 'w') as f:
        json.dump({
            "payload": payload,
            "timestamp": datetime.now().isoformat()
        }, f, indent=4)
