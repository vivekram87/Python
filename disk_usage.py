import shutil
import sys

def check_disk_usage(disk, min_gb, min_percent):
#Returns true if the disk is free, else false
    du = shutil.disk_usage(disk)
# to calculate % of free space
    percent_free = 100 * du.free/du.total
# to convert to GB
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_percent:
        return False
    return True

# check for 2 gb free or 10% free space

if not check_disk_usage(disk="/", min_gb=2, min_percent=10):                       
    print("Error, not enough disk space")
    sys.exit(1)
'''("/", 2 , 10)''' 

for x in range(0,100):
    print ("Everything is ok")
sys.exit(0)



