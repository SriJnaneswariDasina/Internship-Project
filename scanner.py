import requests
from bs4 import BeautifulSoup
from scanner.vulnerabilities import (
    xss, sqli, csrf, cmd_injection, open_redirect, file_inclusion,
    dir_traversal, ssrf, html_injection, clickjacking, info_disclosure,
    auth_bypass, cookie_flags, admin_exposure, js_secrets
)

all_modules = [
    xss, sqli, csrf, cmd_injection, open_redirect, file_inclusion,
    dir_traversal, ssrf, html_injection, clickjacking, info_disclosure,
    auth_bypass, cookie_flags, admin_exposure, js_secrets
]

def get_forms(url):
    try:
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        return soup.find_all("form")
    except:
        return []

def form_details(form):
    details = {"action": form.get("action"), "method": form.get("method", "get"), "inputs": []}
    for input_tag in form.find_all("input"):
        details["inputs"].append({"name": input_tag.get("name"), "type": input_tag.get("type", "text")})
    return details

def run_all_checks(urls):
    results = []
    for url in urls:
        forms = get_forms(url)
        for form in forms:
            f_details = form_details(form)
            session = requests.Session()
            for module in all_modules:
                result = module.test(url, f_details, session)
                if result:
                    results.append(result)
                    log_result(result)
                    
    return results

import json
import os

def log_result(result, filename="scan_logs.json"):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    with open(filename, 'r+') as f:
        data = json.load(f)
        data.append(result)
        f.seek(0)
        json.dump(data, f, indent=4)

