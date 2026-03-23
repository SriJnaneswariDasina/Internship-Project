def test(url, form, session):
    payload = "' OR '1'='1"
    data = {i['name']: payload for i in form['inputs'] if i['type'] != 'submit'}

    try:
        action_url = url + form['action'] if form['action'] else url
        if form['method'].lower() == "post":
            res = session.post(action_url, data=data)
        else:
            res = session.get(action_url, params=data)
        errors = ["sql syntax", "mysql_fetch", "ORA-01756", "syntax error"]
        for error in errors:
            if error in res.text.lower():
                return {"vulnerability": "SQL Injection", "url": action_url, "evidence": error}
    except:
        pass
    return None
