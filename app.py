from flask import Flask, render_template, request, send_file, Response
import qrcode
import io

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

@app.route('/robots.txt')
def robots():
    """Generate robots.txt to guide search engine crawlers"""
    robots_txt = '''User-agent: *
Allow: /
Sitemap: https://qr-code-sand-iota.vercel.app/sitemap.xml'''
    return Response(robots_txt, content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
