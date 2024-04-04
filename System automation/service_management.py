import shutil
import psutil
import os
import paramiko

#ssh to the server and execute the command
def ssh_client():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    password = input("Enter the password: ")
    ssh.connect('192.168.124.11', username='debian', password=password)
    stdin, stdout, stderr = ssh.exec_command('df -h')
    print(stdout.read())
    ssh.close()

ssh_client()

#Check the disk usage, CPU usage and memory usage

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

def check_memory_usage():
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024
    return mem.available > THRESHOLD

if not check_disk_usage("/") or not check_cpu_usage() or not check_memory_usage():
    print("ERROR!")

