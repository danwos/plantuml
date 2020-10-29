import subprocess
import uuid
from multiprocessing import Process
from ftplib import FTP
import os
import time



def use_jar():
    times = []
    start_overall = time.time()
    for index, filename in enumerate(os.listdir('speed_test/input')):
        start = time.time()
        print(f'{index}. {filename} :', end='')
        input_location = f'speed_test/input/{filename}'
        output_location = f'../output_jar/'
        subprocess.run(['java', '-jar', 'plantuml.jar', input_location, '-o', output_location])
        end = time.time()
        print(end-start)
        times.append(end-start)
    end_overall = time.time()
    print('Overall time: ', end='')
    print(end_overall - start_overall)
    times.sort()
    print('longest: ', times[-1])
    print('shortest: ', times[0])

if __name__ == '__main__':
    use_jar()
    print('ENDE')

