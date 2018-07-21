from twisted.internet import protocol, reactor

class Knock(protocol.Protocol):

    def dataReceived(self, data):

        print('Client:', data)

        if data.startswith("Knock knock".encode("utf8")):
            response = "Who's there?".encode("utf8")

        else:
            response = (data + " who?").encode("utf8")

        print('Server:'.encode("utf8"), response)
        self.transport.write(response.encode("utf8"))

class KnockFactory(protocol.Factory):

    def buildProtocol(self, addr):

        return Knock()

reactor.listenTCP(8800, KnockFactory())
reactor.run()
