def test(url, form, session):
    payload = "test; echo cmd_injection_test"
    data = {i['name']: payload for i in form['inputs'] if i['type'] != 'submit'}

    try:
        action_url = url + form['action'] if form['action'] else url
        res = session.post(action_url, data=data) if form['method'].lower() == "post" else session.get(action_url, params=data)
        if "cmd_injection_test" in res.text:
            return {"vulnerability": "Command Injection", "url": action_url, "evidence": payload}
    except:
        pass
    return None
