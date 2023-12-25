import sys, os
from colorama import init
from termcolor import colored


# Init colorama
init()


class KeyMaster:
    def __init__(self) -> None:
        self.version = "0.0.2"
        self.user_os = None
        self.root_dir = None # Root dir for keymaster

    def init_root_dir(self):
        if sys.platform.startswith('win'):
            print(colored("Developing", "green"))
            sys.exit(1)
        elif sys.platform.startswith('darwin'):
            print(colored("Developing", "green"))
            sys.exit(1)
        elif sys.platform.startswith('linux'):
            self.user_os = "linux"

            if not os.path.exists(f"{os.path.expanduser('~')}/.keymaster"):
                os.makedirs(f"{os.path.expanduser('~')}/.keymaster")
                self.root_dir = f"{os.path.expanduser('~')}/.keymaster"
                print(colored(f"✔ SSH key store initialized!\nKey store location is: {self.root_dir}", "green"))
            else:
                print(colored("✖ The key store is already initialized!", "red"))
        else:
            print("Unsupported platform")
            sys.exit(1)
