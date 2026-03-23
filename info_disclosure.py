def test(url, form, session):
    try:
        res = session.get(url)
        if "Exception" in res.text or "Traceback" in res.text:
            return {"vulnerability": "Information Disclosure", "url": url, "evidence": "Stack trace or error found"}
    except:
        pass
    return None
