def test(url, form, session):
    try:
        res = session.get(url)
        cookies = res.headers.get("Set-Cookie", "")
        if "secure" not in cookies.lower() or "httponly" not in cookies.lower():
            return {"vulnerability": "Insecure Cookie Flags", "url": url, "evidence": cookies}
    except:
        pass
    return None
