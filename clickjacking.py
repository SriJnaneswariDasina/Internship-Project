def test(url, form, session):
    try:
        res = session.get(url)
        if "x-frame-options" not in res.headers:
            return {"vulnerability": "Clickjacking", "url": url, "evidence": "Missing X-Frame-Options header"}
    except:
        pass
    return None
