import json
from flask import send_file
from xhtml2pdf import pisa
import io

from flask import session, redirect, url_for, flash
app.secret_key = 'vulnscan-secret-key'  # Use strong secret key in production

from flask import Flask, render_template, request
from scanner import crawler, scanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        pages = crawler.crawl(url)
        results = scanner.run_all_checks(pages)
        return render_template("results.html", results=results, target=url)
    return render_template("index.html")

@app.route('/export/html')
def export_html():
    with open("scan_logs.json", "r") as f:
        data = json.load(f)
    return render_template("results.html", results=data, target="Previous Scan")

@app.route('/export/pdf')
def export_pdf():
    with open("scan_logs.json", "r") as f:
        data = json.load(f)
    html = render_template("results.html", results=data, target="Previous Scan")
    pdf = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), dest=pdf)
    pdf.seek(0)
    return send_file(pdf, download_name="scan_report.pdf", as_attachment=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['user'] = 'admin'
            return redirect(url_for('index'))
        else:
            flash('Invalid Credentials', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    ...

from flask import jsonify

scan_results_cache = []

@app.route('/scan', methods=['POST'])
def scan_ajax():
    data = request.get_json()
    url = data['url']
    pages = crawler.crawl(url)
    results = scanner.run_all_checks(pages)
    scan_results_cache.clear()
    scan_results_cache.extend(results)
    return jsonify({"status": "done"})

@app.route('/results')
def results():
    if 'user' not in session:
        return redirect(url_for('login'))
    target = request.args.get('url', 'Target')
    return render_template('results.html', results=scan_results_cache, target=target)

if __name__ == '__main__':
    app.run(debug=True)
