import sys


def parse_arguments():
    args = sys.argv[1:]
    command = None
    options = {}

    i = 0
    while i < len(args):
        arg = args[i]

        if arg.startswith('--'):
            # Handle long options (--option)
            key, _, value = arg[2:].partition('=')
            options[key] = value if value else True
        else:
            # Assume it's the command
            command = arg
        i += 1

    return command, options
