#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

class WOLHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress all HTTP request logging

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = '''
            <html>
            <head>
                <title>Wake PC</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script>
                function wakePC(person) {
                    fetch('/wake/' + person, {method: 'POST'})
                        .then(() => {
                            document.getElementById('status').innerHTML = 'Wake command sent to ' + person + '\\'s PC!';
                            setTimeout(() => {
                                document.getElementById('status').innerHTML = '';
                            }, 3000);
                        });
                }
                </script>
            </head>
            <body style="text-align:center; background-color:#2d2d2d; padding-top:100px; font-family:Arial;">
                <h1 style="color:white">Wake PCs</h1>
                <button onclick="wakePC('user1')" style="font-size:24px; padding:20px 40px; cursor:pointer; display:block; margin:100px auto;">
                    User 1
                </button>
                <button onclick="wakePC('user2')" style="font-size:24px; padding:20px 40px; cursor:pointer; display:block; margin:100px auto;">
                    User 2
                </button>
                <p id="status" style="color:green; font-size:18px; margin-top:20px; min-height:30px;"></p>
            </body>
            </html>
            '''
            self.wfile.write(html.encode())

    def do_POST(self):
        if self.path == '/wake/user1':
            subprocess.run(['etherwake', os.environ['USER1_MAC']])
            self.send_response(200)
            self.end_headers()
        elif self.path == '/wake/user2':
            subprocess.run(['etherwake', os.environ['USER2_MAC']])
            self.send_response(200)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), WOLHandler)
    print('Server running on port 8080...')
    server.serve_forever()
