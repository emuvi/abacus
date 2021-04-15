import os
import subprocess

def backup():
    doing = []
    for _, dirs, _ in os.walk("/mnt/hda/Abacus"):
        for folder in dirs:
            command = "rclone -v sync \"/mnt/hda/Abacus/" + folder + "\" \"server:/mnt/HD01/Abacus/" + folder + "\""
            doing.append(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE))
        break
    return doing

if (__name__ == '__main__'):
    doing = []
    doing.extend(backup())
    for process in doing:
        process.wait()
