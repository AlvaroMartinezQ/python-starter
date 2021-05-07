# Script has to ping a domain/machine

import os, platform

import ping_logger

def ping_machine(host, times):
    os_name = platform.system()

    if os_name == "Windows":
        # Sends 5 packages. Received value is an integer if all went good 0 is returned
        status = os.system(f'ping -n {times} { host }')
        ping_logger.store_logs(status, host, times)
    elif os_name == "Linux":
        status = os.system(f'ping -c {times} { host }')
    else:
        print("SO not supported")
        return -1

if __name__ == '__main__':
    ping_machine("www.urjc.es", 5)
