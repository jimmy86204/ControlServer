from http.server import BaseHTTPRequestHandler,HTTPServer
import subprocess
import json


PORT_NUMBER = 8001

# This class will handles any incoming request from
# the browser 
class myHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        cmd = "/var/lib/docker/volumes/jenkins_volume_jenkins_data/_data/workspace/hanshin-amc/main.sh"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        p_status = p.wait()
        (output, err) = p.communicate()

        # self.wfile.write(cmd + "\n")
        return
try:
        # Create a web server and define the handler to manage the
        # incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print('Started httpserver on port ' , PORT_NUMBER)

        # Wait forever for incoming http requests
        server.serve_forever()

except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()