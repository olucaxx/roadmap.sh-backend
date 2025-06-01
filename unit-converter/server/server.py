from http.server import HTTPServer, SimpleHTTPRequestHandler
import os, json

PORT = 8080
os.chdir("../client")

class Handler(SimpleHTTPRequestHandler):
    def _send_json_response(self, data: dict, status_code: int):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json') 
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    
    def _send_error(self, message: str, status_code:int):
        self.send_response(status_code)
        self.end_headers()
        
    
    def do_GET(self):
        return super().do_GET()
    
    
    def do_POST(self):
        content_length: int = int(self.headers['Content-Length'])
        post_data: bytes = self.rfile.read(content_length)
        
        answers: dict = json.loads(post_data.decode())
        print(answers)
        
        self._send_error("teste", 400)
        

server = HTTPServer(('localhost', PORT), Handler)
print(f"http://localhost:{PORT}")
server.serve_forever()