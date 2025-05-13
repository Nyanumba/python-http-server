from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
portno = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>My Server</title></head>
            <body>
                <h1>My Python Server</h1>
                <p>Request: {self.path}</p>
                <p>Simple HTTP server built by python for practice.</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(html, "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            <head><title>404 Not Found</title></head>
            <body>
                <h1>404 - Not Found</h1>
                <p>Page not found.</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(html, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostname, portno), MyServer)
    print(f"Server started http://{hostname}:{portno}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print("Server stopped.")