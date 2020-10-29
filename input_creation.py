import subprocess
import uuid
from multiprocessing import Process
from ftplib import FTP
PORT = 4242

example = \
"""
@startuml

    node {a}
    node {b}
    node {c}

    {a} --> {b}
    {b} --> {c}
    {c} -> {a}

@enduml
"""


def create_inputs():
    for x in range(100):

        filename = str(uuid.uuid4())
        a = str(uuid.uuid4())[:5]
        b = str(uuid.uuid4())[:5]
        c = str(uuid.uuid4())[:5]
        with open(f'speed_test/input/{filename}.txt', 'w') as fp:
            fp.write(example.format(a=a, b=b, c=c))


if __name__ == '__main__':
    create_inputs()

