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
    sys.exit(0)

main()

 