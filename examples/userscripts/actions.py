import interfaces


class LocalAction(interfaces.Action):

    def execute(self, command):
        print("Executing command: " + command)


class DockerAction(interfaces.Action):

    def execute(self, container, command):
        print("Executing in container: " + container + ", command: " + command)