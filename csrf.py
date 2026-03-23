def test(url, form, session):
    if not form['inputs']:
        return None
    has_token = any("csrf" in i['name'].lower() for i in form['inputs'])
    if not has_token:
        return {"vulnerability": "CSRF", "url": url, "evidence": "Missing CSRF token in form"}
    return None
