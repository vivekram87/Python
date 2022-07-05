import os
import sys

def check_reboot():
    # Return true if the computer is pending a reboot
    return os.path.exists("run/reboot-required")
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything is ok!")
    check_no_network()
    sys.exit(0)
    
def check_no_network():
    '''Return True if it fails to resolve Google.com, else False'''
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

main()

 
