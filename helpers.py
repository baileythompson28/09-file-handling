from time import sleep
import sys


def type_print(str, end="\n", delay=0.5):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.frush()
        sleep(delay)
    print(end, end="")
