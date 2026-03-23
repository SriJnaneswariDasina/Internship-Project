def test(url, form, session):
    payload = "<script>alert(1)</script>"
    data = {i['name']: payload for i in form['inputs'] if i['type'] != 'submit'}

    try:
        action_url = url + form['action'] if form['action'] else url
        if form['method'].lower() == "post":
            res = session.post(action_url, data=data)
        else:
            res = session.get(action_url, params=data)
        if payload in res.text:
            return {"vulnerability": "XSS", "url": action_url, "evidence": payload}
    except:
        pass
    return None
