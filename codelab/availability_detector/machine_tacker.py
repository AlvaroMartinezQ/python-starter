# Main file for project
# This script uses all of the other scripts located in this directory
# to track the availability of any server of your choice

from os import stat
import time
import argparse

# Local
import ping_machine
import mailer

def track_machine():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--server", required=True, help="Server to track status")
    ap.add_argument("-e", "--email", required=True, help="Administrator email")
    args = ap.parse_args()

    server = args.server
    email = args.email

    print("Machine tracker is booting up... To exit press Crtl + c")

    last_ceck = False
    count_checks = 0

    while(True):
        start = time.time()
        status = ping_machine.ping_machine(server, 1)
        duration = time.time() - start # Time the ping command takes to perform
        print(f'Last ping lasted for {duration} ms')
        if status != 0:
            if count_checks == 5 and last_ceck is False:
                last_ceck = True
                mailer.send_email(email, 'Subject: Server failure!', f'Your server {server} is down!')
                count_checks += 1
            elif count_checks < 5:
                count_checks += 1
            else:
                count_checks = 0
        else:
            last_ceck = False
            count_checks = 0
        time.sleep(5) # Time in seconds


if __name__ == '__main__':
    track_machine()