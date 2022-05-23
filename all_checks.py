import os
import sys

def check_reboot():
    # Return true if the computer is pending a reboot
    return os.path.exist("run/reboot-required")
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

main()

 