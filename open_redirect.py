from urllib.parse import urlencode

def test(url, form, session):
    redir_payload = "https://evil.com"
    for input_tag in form['inputs']:
        if "url" in input_tag['name'].lower():
            data = {i['name']: redir_payload if i['name'] == input_tag['name'] else "test" for i in form['inputs']}
            action_url = url + form['action'] if form['action'] else url
            try:
                response = session.get(action_url, params=data)
                if "evil.com" in response.url:
                    return {"vulnerability": "Open Redirect", "url": action_url, "evidence": response.url}
            except:
                pass
    return None
