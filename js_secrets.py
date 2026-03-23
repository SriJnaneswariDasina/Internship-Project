import re

def test(url, form, session):
    try:
        res = session.get(url)
        secrets = re.findall(r"(apikey|secret|token)[\"'\s:=]+[a-zA-Z0-9-_]{10,}", res.text, re.IGNORECASE)
        if secrets:
            return {"vulnerability": "Exposed JavaScript Secrets", "url": url, "evidence": secrets[0]}
    except:
        pass
    return None
