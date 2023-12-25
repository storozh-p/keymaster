from art import text2art
from utils import parse_arguments
from keymaster import KeyMaster


if __name__ == "__main__":
    command, options = parse_arguments()

    match command:
        case "init":
            KeyMaster().init_root_dir()

        case _:            
            help_str = f"""
{text2art("keymaster", font="big")}

keymaster v{KeyMaster().version}

NAME:
    keymaster - A simple and powerful SSH keys manager

USAGE:
    keymaster command

VERSION:
    v{KeyMaster().version}

COMMANDS:
    init - Initialize SSH keys store for the first time use
"""
            print(help_str)
