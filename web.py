
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        html = """
        <html>
        <head>
            <title>TCP/IP Protocol Suite</title>
        </head>
        <body>
            <h1>TCP/IP Protocol Suite</h1>
            <h2>List of Protocols</h2>
            <ul>
                <li>HTTP - Hypertext Transfer Protocol</li>
                <li>HTTPS - Secure HTTP</li>
                <li>FTP - File Transfer Protocol</li>
                <li>TCP - Transmission Control Protocol</li>
                <li>UDP - User Datagram Protocol</li>
                <li>IP - Internet Protocol</li>
                <li>DNS - Domain Name System</li>
                <li>SMTP - Simple Mail Transfer Protocol</li>
                <li>POP3 - Post Office Protocol</li>
                <li>ICMP - Internet Control Message Protocol</li>
            </ul>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

server = HTTPServer(("localhost", 8000), MyServer)

print("Web server running at http://localhost:8000")

server.serve_forever
server.serve_forever()

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',680)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()