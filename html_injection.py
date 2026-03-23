def test(url, form, session):
    payload = "<h1>HTML Injected</h1>"
    data = {i['name']: payload for i in form['inputs'] if i['type'] != 'submit'}
    try:
        action_url = url + form['action'] if form['action'] else url
        res = session.post(action_url, data=data) if form['method'].lower() == "post" else session.get(action_url, params=data)
        if payload in res.text:
            return {"vulnerability": "HTML Injection", "url": action_url, "evidence": payload}
    except:
        pass
    return None
