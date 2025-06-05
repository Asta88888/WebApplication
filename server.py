from http.server import HTTPServer, SimpleHTTPRequestHandler


hostName = "localhost"
serverPort = 8080


class MyServer(SimpleHTTPRequestHandler):
    """Специальный класс, который отвечает за обработку входящих запросов от клиента"""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        if self.path in ["/", "/contact.html"]:
            try:
                with open("contact.html", "r", encoding="utf-8") as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html_content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "contact.html not found")
        else:
            super().do_GET()


    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started: http://{hostName}:{serverPort}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
