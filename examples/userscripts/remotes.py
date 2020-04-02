import interfaces


class LocalRemote(interfaces.Remote):

    def download(self, source, target):
        print("Loading " + target + " locally from " + source)

    def upload(self, source, target):
        print("Storing " + source + " locally at " + target)


class FTPSRemote(interfaces.Remote):

    def download(self, source, target):
        print("Loading " + target + " via FTPS from " + source)

    def upload(self, source, target):
        print("Storing " + source + " via FTPS at " + target)