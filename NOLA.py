import os
import platform
import requests

class Subscription:
    def __init__(self):
        self.bit = platform.architecture()[0]

    def install_requests(self):
        try:
            import requests
        except ImportError:
            os.system('pip2 install requests')
            import requests

    def run(self):
        self.install_requests()
        if self.bit == "64bit":
            from FILE import ____Main___
            ____Main___()

if __name__ == "__main__":
    subscription = ____Main___()
    ____Main___.run()
