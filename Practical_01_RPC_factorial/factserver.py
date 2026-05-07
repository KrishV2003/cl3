from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Class for factorial operations
class FactorialServer:

    def calculate_factorial(self, n):

        if n < 0:
            raise ValueError("Input must be non-negative")

        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

# Restrict path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(
        ("localhost", 8000),
        requestHandler=RequestHandler) as server:

    server.register_introspection_functions()

    # Register factorial class
    server.register_instance(FactorialServer())

    print("Server is running...")

    # Keep server running forever
    server.serve_forever()