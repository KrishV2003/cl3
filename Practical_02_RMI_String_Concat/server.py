import Pyro4

# Expose class for remote access
@Pyro4.expose
class StringConcatenator(object):

    # Remote method
    def concatenate(self, str1, str2):

        result = str1 + " " + str2

        return result


# Create Pyro daemon
daemon = Pyro4.Daemon()

# Register remote object
uri = daemon.register(StringConcatenator())

# Print server URI
print("Server URI :", uri)

# Start server loop
print("Server is running...")

daemon.requestLoop()