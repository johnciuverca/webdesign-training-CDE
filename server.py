from http.server import SimpleHTTPRequestHandler, HTTPServer
import os


class ImageHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Processing request: {self.path}")
        if self.path == '/nature.jpg':
            self.path = 'nature.jpg'
        return super().do_GET()

if __name__ == '__main__':
    PORT = 8000
    print(f"Serving on http://localhost:{PORT}")
    httpd = HTTPServer(('localhost', PORT), ImageHandler)
    httpd.serve_forever()
