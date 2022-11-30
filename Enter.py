import args as args

from tello_connect import Tello
import sys
from datetime import datetime
import time
import argparse
# this file is for opening the Cv(videos) and also be able to identify the aruco code

def parse_args(args):
    parser = argparse.ArgumentParser(' Tello flight Commander', epilog = 'One-Off Coder http//www.oneoffcoder.com')

    parser.add_argument('f-', '--file', help ='command file', required = True)

    return parser.parse_args(args)

    def start(file_name):

            start_time  = str(datetime.now())

            with open(file_name, 'r') as f:
                commands = f.readlines()

            tello = Tello()
            for command in commands:
                if command != '' and command != '\n':
                    command = command.rstrip()

                    if command.find('delay') != -1:
                        sec = float(command.partition('delay')[2])
                        print(f'delayed {sec}')
                        time.sleep(sec)
                        pass
                    else:
                        tello.send_command(command)

            with open(f'log/{start_time}.txt', 'w') as out:
                log = tello.get_log()

                for Stat in log:
                    Stat.print_stats()
                    s = Stat.return_stats()
                    out.write(s)

    if __name__ == '__main__':
        args = parse_args(sys.argsv[-1])
        file_name = agrs.file
        start(file_name)
