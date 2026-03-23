def test(url, form, session):
    admin_urls = ["/admin", "/administrator", "/admin/login", "/cpanel"]
    for endpoint in admin_urls:
        full_url = url + endpoint
        try:
            res = session.get(full_url)
            if res.status_code == 200 and "login" in res.text.lower():
                return {"vulnerability": "Exposed Admin Panel", "url": full_url, "evidence": "Accessible admin page"}
        except:
            pass
    return None
