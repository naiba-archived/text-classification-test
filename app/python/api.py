from http.server import HTTPServer, BaseHTTPRequestHandler
import classification
import segmentation


class API(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            sg = segmentation.Segmentation()
            sg.segment(filePath='../../data/舔狗日记.txt', label='舔狗')
            sg.segment(filePath='../../data/心灵鸡汤.txt', label='鸡汤')
            cf = classification.Classification()
            cf.train()
            cf.test()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'success')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'not found')


httpd = HTTPServer(('localhost', 8000), API)
httpd.serve_forever()
