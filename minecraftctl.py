#!/bin/python
# minecraftctl.py

# In this module: main entry point

import getopt
import signal
import sys

# Exit codes
EXIT_NO_ERROR = 0
EXIT_ERR_WRONG_ARGUMENT = 9
EXIT_UNKNOWN_ARGUMENT = 10
EXIT_TERMINATED_BY_USER = 99
EXIT_UNKNOWN_ERROR = 100

# Runtime variables
programm_arguments = "hv"
programm_argument_names = ["help", "version"]
version = "0.0.0"


def usage():
    print("usage: ./minecraftctl.py [OPTION]")
    print("Minecraft-Server control software.\n")

    print("  -h, --help")
    print("  -v, --version")

    print("\nReport Bugs to https://github.com/crapStone/minecraftctl/issues")


def exit_program(status):
    sys.exit(status)


def exit_with_message(prompt, status):
    print(prompt)
    exit_program(status)


def signal_handler(signum, frame):
    print(signum)
    if signum == signal.SIGINT:
        exit_with_message("Terminated by user", EXIT_TERMINATED_BY_USER)


def main():
    for signum in [signal.SIGINT]:
        try:
            signal.signal(signum, signal_handler)
        except OSError:
            print("Skipping {}".format(signum))

    try:
        opts, args = getopt.getopt(sys.argv[1:], programm_arguments, programm_argument_names)
    except getopt.GetoptError as e:
        print(str(e))
        usage()
        exit_program(EXIT_ERR_WRONG_ARGUMENT)

    for o, a in opts:
        if o in ("-v", "--" + programm_argument_names[programm_arguments.find("v")]):
            print(version)

        elif o in ("-h", "--" + programm_argument_names[programm_arguments.find("h")]):
            usage()
            exit_program(EXIT_NO_ERROR)

        else:
            exit_with_message("Unknown argument!", EXIT_UNKNOWN_ARGUMENT)

    # TODO start point here


if __name__ == "__main__":
    main()
