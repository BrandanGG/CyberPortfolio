from flask import Flask, render_template, send_from_directory, g, has_request_context
import os, base64

app = Flask(__name__)

# Security headers
@app.after_request
def after_request(response):
    nonce = getattr(g, 'nonce', base64.b64encode(os.urandom(16)).decode('utf-8'))
    # Security headers for enhanced protection
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = (
        f"default-src 'self'; "
        f"style-src 'self' 'unsafe-inline'; "
        f"script-src 'self' 'nonce-{nonce}' https://cdn.jsdelivr.net; "
        f"connect-src 'self' https://cdn.jsdelivr.net;"
    )
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

@app.route('/')
def index():
    nonce = base64.b64encode(os.urandom(16)).decode('utf-8')
    g.nonce = nonce
    return render_template('index.html', nonce=nonce)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
