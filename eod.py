
import datetime

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