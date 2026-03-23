def test(url, form, session):
    payload = "http://127.0.0.1"
    data = {i['name']: payload for i in form['inputs'] if i['type'] != 'submit'}
    try:
        action_url = url + form['action'] if form['action'] else url
        res = session.post(action_url, data=data) if form['method'].lower() == "post" else session.get(action_url, params=data)
        if "localhost" in res.text or "127.0.0.1" in res.text:
            return {"vulnerability": "SSRF", "url": action_url, "evidence": payload}
    except:
        pass
    return None
