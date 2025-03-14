from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

messages = ["Initial message"]

class CustomHandler(SimpleHTTPRequestHandler):        
    def do_GET(self):
        """Serve the main HTML page or return the current message."""
        global messages
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.generate_html().encode("utf-8"))
        elif self.path == "/message":
            message = "\n".join([m for m in sorted(messages, key=lambda x: len(x))])
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": message}).encode("utf-8"))
        else:
            self.send_error(404, "File not found")

    def do_POST(self):
        """Update the message when a POST request is received."""
        global messages
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            if "message" in data:
                message = data["message"]
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": message}).encode("utf-8"))
                messages.append(message)
            else:
                self.send_error(400, "Bad Request: 'message' field is required")
        except json.JSONDecodeError:
            self.send_error(400, "Bad Request: Invalid JSON")

    def generate_html(self):
        """Generates a simple HTML page with JavaScript to fetch and update the message."""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Live Message</title>
            <script>
                async function fetchMessage() {{
                    let response = await fetch('/message');
                    let data = await response.json();
                    document.getElementById('message').innerText = data.message;
                }}
                setInterval(fetchMessage, 1000); // Refresh message every second
                fetchMessage(); // Initial fetch
            </script>
        </head>
        <body>
            <h1>Live Message</h1>
            <p id="message">""</p>
        </body>
        </html>
        """

# Start server
host = "localhost"
port = 8000

server = HTTPServer((host, port), CustomHandler)
print(f"Serving at http://{host}:{port}")
server.serve_forever()
