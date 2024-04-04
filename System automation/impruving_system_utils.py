import psutil
import paramiko
import getpass
import argparse
import logging

# Set up logging
logging.basicConfig(filename='service_management.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='IP address of the server')
parser.add_argument('--username', help='Username')
parser.add_argument('--password', help='Password')
parser.add_argument('--file-size', help='File size to search for (in MB)')
args = parser.parse_args()

# Get user input if not provided as command-line arguments
ip = args.ip or input("Enter the IP address of the server: ")
username = args.username or input("Enter the username: ")
password = args.password or getpass.getpass("Enter the password: ")
file_size = args.file_size or input("Enter the file size to search for (in MB): ")

# Connect to the remote server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)

# Define functions for each task
def check_disk_usage():
    stdin, stdout, stderr = ssh.exec_command('df -h')
    logging.info("Disk usage:")
    logging.info(stdout.read().decode())

def find_big_files():
    stdin, stdout, stderr = ssh.exec_command(f"find / -type f -size +{file_size}M -exec du -h {{}} \; | sort -rh")
    logging.info(f"File size more than {file_size} MB:")
    logging.info(stdout.read().decode())

def check_cpu_usage():
    stdin, stdout, stderr = ssh.exec_command('uptime')
    logging.info("Uptime, users on server, CPU load 1min, 5min, 15min:")
    logging.info(stdout.read().decode())

def check_memory_usage():
    stdin, stdout, stderr = ssh.exec_command('free -h')
    logging.info("Memory usage:")
    logging.info(stdout.read().decode())

def check_service():
    stdin, stdout, stderr = ssh.exec_command('systemctl status ssh.service')
    logging.info("SSH service status:")
    logging.info(stdout.read().decode())

# Execute the tasks
check_disk_usage()
find_big_files()
check_cpu_usage()
check_memory_usage()
check_service()

# Close the SSH connection
ssh.close()