"""A tiny HTTP server. Standard library only: nothing to install.

Every file in routes/ that defines PATH and handle() becomes an endpoint.
Add your own file. Do not edit this one.
"""
class Handler(BaseHTTPRequestHandler):
    routes = load_routes()

    def do_GET(self):
        routes = self.routes
        if self.path == "/":
            self.reply(200, {"endpoints": sorted(routes) + ["/"]})
        elif self.path in routes:
            self.reply(200, routes[self.path]())
        else:
            self.reply(404, {"error": "no such path", "try": sorted(routes)})

    def reply(self, code, body):
        payload = json.dumps(body, indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt, *args):
        print("  %s" % (fmt % args))