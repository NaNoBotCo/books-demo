#!/usr/bin/env python3
"""Serve this folder for the demo.

Static files only, on localhost, with caching turned off so an edit shows up on
the next reload rather than the next browser restart.
"""
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4321


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):   # one line per request is enough
        sys.stderr.write("%s\n" % (fmt % args))


with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"http://localhost:{PORT}")
    httpd.serve_forever()
