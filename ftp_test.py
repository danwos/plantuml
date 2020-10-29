import subprocess
import uuid
from multiprocessing import Process
from ftplib import FTP
import os
import time

PORT = 4242


def start_ftp():
    process = subprocess.run(['java', '-jar', 'plantuml.jar', f'-ftp:{PORT}'])
    print('FTP Server STOPPED')


def use_ftp():
    times = []
    ftp = FTP()
    print(ftp.connect('127.0.0.1', PORT))
    print(ftp.login())
    ftp.set_pasv(False)
    print(ftp.retrlines("LIST"))
    start_overall = time.time()

    for index, filename in enumerate(os.listdir('speed_test/input')):
        start = time.time()
        print(f'{index}. {filename} :', end='')
        with open(f'speed_test/input/{filename}', 'rb') as fup:
            ftp.storlines(f"STOR {filename}", fup)

        new_filename = filename.split(".")[0] + '.png'
        new_file = open(f'speed_test/output_ftp/{new_filename}', 'wb')
        ftp.retrbinary(f'RETR {new_filename}', new_file.write)
        end = time.time()
        print(end-start)
        times.append(end - start)
    end_overall = time.time()
    print('Overall time: ', end='')
    print(end_overall - start_overall)
    times.sort()
    print('longest: ', times[-1])
    print('shortest: ', times[0])


if __name__ == '__main__':
    p = Process(target=start_ftp)
    p.start()
    time.sleep(1.0)
    print(f'FTP Server running with PID {p.pid}')
    use_ftp()
    print('ENDE')

