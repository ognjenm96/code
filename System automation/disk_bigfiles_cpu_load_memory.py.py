# This script is used to check the disk usage, find big files, check CPU usage and check memory usage of a remote Linux server.
import psutil
import paramiko
from psutil._common import bytes2human

ip = input("Enter the IP address of the server: ")
username = input("Enter the username: ")
password = input("Enter the password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)

def check_disk_usage():
    stdin, stdout, stderr = ssh.exec_command('df -h')
    print("Disk usage:")
    print(stdout.read().decode())

def find_big_files():
    stdin, stdout, stderr = ssh.exec_command('find / -type f -size +50M -exec du -h {} \; | sort -rh')
    print("Big files on / :")
    print(stdout.read().decode())

def check_cpu_usage():
    stdin, stdout, stderr = ssh.exec_command('uptime')
    print("Uptime, users on server, cpu load 1min, 5min, 15min:")
    print(stdout.read().decode())

def check_memory_usage():
    stdin, stdout, stderr = ssh.exec_command('free -h')
    print("Memory usage:")
    print(stdout.read().decode())

check_disk_usage()
find_big_files()
check_cpu_usage()
check_memory_usage()