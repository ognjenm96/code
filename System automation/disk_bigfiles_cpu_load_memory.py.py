# This script is used to check the disk usage, find big files, check CPU usage and check memory usage of a remote Linux server.
import paramiko
import getpass
import logging
import datetime

ip = input("Enter the IP address of the server: ")

logging.basicConfig(filename=f"server({ip})stats{datetime.datetime.now().strftime('%Y-%m-%d')}.log", level=logging.ERROR, format='%(asctime)s - %(message)s')

username = input("Enter the username: ")
password = getpass.getpass("Enter the password: ")
file_size = input("Enter the file size to search for (in MB): ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)

print("..............................................................................")

def check_disk_usage():
    stdin, stdout, stderr = ssh.exec_command('df -h')
    logging.info(print("Disk usage:"))
    print(" ")
    logging.info(stdout.read().decode())
    print("..............................................................................")

def find_big_files():
    stdin, stdout, stderr = ssh.exec_command(f"find / -type f -size +{file_size}M -exec du -h {{}} \; | sort -rh")
    print(f"File size more then {file_size} /* :")
    print(" ")
    print(stdout.read().decode())
    print("..............................................................................")

def check_cpu_usage():
    stdin, stdout, stderr = ssh.exec_command('uptime')
    print("Uptime, users on server, cpu load 1min, 5min, 15min:")
    print(" ")
    print(stdout.read().decode())
    print("..............................................................................")

def check_memory_usage():
    stdin, stdout, stderr = ssh.exec_command('free -h')
    print("Memory usage:")
    print(" ")
    print(stdout.read().decode())
    print("..............................................................................")

def check_servise():
    stdin, stdout, stderr = ssh.exec_command('systemctl status ssh.service')
    print("SSH service status:")
    print(" ")
    print(stdout.read().decode())
    print("..............................................................................")


check_disk_usage()
find_big_files()
check_cpu_usage()
check_memory_usage()
check_servise()