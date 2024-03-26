import os
import datetime
import shutil

def create_daily_backup():
    source_file = "/var/log/boot.log"
    backup_dir = "/home/ognjenm/beckup"  # Replace with the actual path to your backup directory

    # Create a backup directory with today's date
    today = datetime.date.today().strftime("%Y-%m-%d")
    backup_dir_today = os.path.join(backup_dir, today)
    os.makedirs(backup_dir_today, exist_ok=True)

    # Generate the backup file name
    backup_file = f"boot.log{today}.tar.gz"
    backup_path = os.path.join(backup_dir_today, backup_file)

    # Copy the source file to the backup directory
    shutil.copy2(source_file, backup_path)

    print(f"Backup created: {backup_path}")

def check_current_day_backup():
    backup_dir = "/home/ognjenm/beckup"  # Replace with the actual path to your backup directory
    today = datetime.date.today().strftime("%Y-%m-%d")
    backup_file = f"backup_{today}.tar.gz"
    if backup_file in os.listdir(backup_dir):
        print(f"Backup for today ({today}) found.")
    else:
        print(f"No backup for today ({today}).")


create_daily_backup()
check_current_day_backup()