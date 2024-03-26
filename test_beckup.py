import os
import datetime
import shutil
from beckup import create_daily_backup, check_current_day_backup

def test_create_daily_backup():
    # Set up test environment
    source_file = "/var/log/boot.log"
    backup_dir = "/home/ognjenm/beckup"
    today = datetime.date.today().strftime("%Y-%m-%d")
    backup_dir_today = os.path.join(backup_dir, today)
    backup_file = f"boot.log{today}.tar.gz"
    backup_path = os.path.join(backup_dir_today, backup_file)

    # Call the function to create daily backup
    create_daily_backup()

    # Assert that the backup directory is created
    assert os.path.exists(backup_dir_today)

    # Assert that the backup file is created
    assert os.path.exists(backup_path)

def test_check_current_day_backup():
    # Set up test environment
    backup_dir = "/home/ognjenm/beckup"
    today = datetime.date.today().strftime("%Y-%m-%d")
    backup_file = f"backup_{today}.tar.gz"

    # Call the function to check current day backup
    check_current_day_backup()

    # Assert that the backup file is found
    assert f"Backup for today ({today}) found." in captured_output

    # Assert that the backup file is not found
    assert f"No backup for today ({today})." in captured_output

if __name__ == "__main__":
    test_create_daily_backup()
    test_check_current_day_backup()