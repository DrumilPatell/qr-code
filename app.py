from flask import Flask, render_template, request, send_file, Response
import qrcode
import io
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    
    if not url:
        return "Please provide a URL", 400
    
    # Generate QR code
    img = qrcode.make(url)
    
    # Save to bytes buffer
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap for search engines"""
    today = datetime.now().strftime('%Y-%m-%d')
    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://qr-code-sand-iota.vercel.app/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>'''
    return Response(sitemap_xml, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    """Generate robots.txt to guide search engine crawlers"""
    robots_txt = '''User-agent: *
Allow: /
Sitemap: https://qr-code-sand-iota.vercel.app/sitemap.xml'''
    return Response(robots_txt, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
