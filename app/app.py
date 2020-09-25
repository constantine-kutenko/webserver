#!/usr/bin/python3

import os
import sys
import logging
from io import BytesIO
from http.server import BaseHTTPRequestHandler, HTTPServer
from signal import signal, SIGINT

VERSION="0.0.1"

def handler(signal_received, frame) -> None:
    """ Handler for correct process termination """
    log.warning("SIGINT or CTRL-C detected. Exiting gracefully")
    sys.exit(0)


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    """ Base class that handles requests """

    def do_GET(self):
        """ Handle GET requests """
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('Get request received', "utf8"))


    def do_POST(self):
        """ Handle POST requests """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()

        response = BytesIO()
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        log.info(body.decode("utf-8"))


def main():
    local_addr = os.getenv('LISTEN_ADDR', '0.0.0.0')
    local_port = int(os.getenv('LISTEN_PORT', '5000'))
    log_level = os.getenv('LOG_LEVEL', 'info')

    if log_level == '' or log_level not in ('info', 'debug'):
        log_level = 'info'

    global log
    log = logging.getLogger('stdout')
    logging.basicConfig(format='%(asctime)s [ %(levelname)s ] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    log.setLevel(getattr(logging, log_level.upper()))

    signal(SIGINT, handler)

    log.info("Starting web server v%s" % VERSION)
    httpd = HTTPServer((local_addr, local_port), HTTPServer_RequestHandler)
    log.info("Log level: %s" % log_level.upper())
    log.info("Listening on %s:%s..." % (local_addr, local_port))
    httpd.serve_forever()


if __name__ == "__main__":
    main()
