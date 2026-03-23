def test(url, form, session):
    try:
        res = session.get(url, cookies={"auth": "admin"})
        if "admin" in res.text.lower() and "login" not in res.text.lower():
            return {"vulnerability": "Broken Authentication", "url": url, "evidence": "Authenticated content visible"}
    except:
        pass
    return None
