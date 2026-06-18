#!/usr/bin/env python3
"""Petit serveur statique pour prévisualiser le site À l'Aveugle."""
import functools
import http.server
import os
import socketserver

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 4173

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"À l'Aveugle servi sur http://127.0.0.1:{PORT}")
    httpd.serve_forever()
