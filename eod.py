# Description: This script is used to fill the EOD excel sheet with the information from the email
import datetime
import openpyxl # is use for reading and writing excel files
import outlook # is use for reading emails from outlook
import pyOutlook # is use for reading emails from outlook
import os # is use for reading and writing files

# get the email from the outlook

access_token = pyOutlook.get_access_token(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    scopes=['https://outlook.office.com/mail.read']
)

pyOutlook.Message.get_messages(
    access_token=access_token,
    folder_name='Inbox',
    select_fields=['subject', 'receivedDateTime', 'sender', 'bodyPreview'],
    search_query='from:
    "your_email_address" AND subject: "EOD Morning Shift 08 - 16"',
)

# nadji ime fajla za koji je potrebno unete info


# for Morning shift 08 - 16

Job_Name_Morning = [
    "Extraction of SABINE data for T24",
    "EGCP Batch 131 File",
    "EGCP Batch 124 File",
    "EGCP Batch 126 File",
    "EGCP Batch 127 File",
    "EGCP Batch 129 File",
    "EGCP Batch 133 File",
    "EGCP Batch 135 File",
    "EGCP Batch 141 File",
    "Generate T24Outgoing from merchant payments",
    "Export merchant payment files",
    "Generate merchant reports",
    "Export DCID213 file (Daily Report for Merchants)",
    "Posting of Account Limits",
    "Report of unexecuted FT for Merchant POS usage",
]

# Row that need to be filled in the excel sheet

Actual_Start_Timeo = () # from email prat Started:26/03/2024 # take this part 16:00:00

Actual_End_time = () # form email part Ended:26/03/2024 # take this part 16:02:35

Actual_Duration = Actual_Start_Timeo - Actual_End_time

Status = "Success" or "Not Executed"

Email_Notification =  "Arrived" or "Not Arrived"