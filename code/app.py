import http.server
import socketserver
import webbrowser

# This tells Python to run a server on port 8000
PORT = 8000

# This is the "Engine" that serves your HTML file
Handler = http.server.SimpleHTTPRequestHandler

print(f"Server starting at http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")

# This line opens your browser automatically to the right spot
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()