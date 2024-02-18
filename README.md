# kobo-transfer

Transfer submissions from XLSX Form to Kobo Project 

Demo: https://drive.google.com/file/d/1yMcsEKqOH3L09O00urFko3iB77PABuFh/view?usp=sharing 

## Usage

For XLSX: 
```bash
python3 run.py -xt -ef [excel_file_path]
```

For data downloaded from Google Form:
```bash
python3 run.py -gt -ef [excel_file_path]
```

## Requirements

Make sure you have the following Python packages installed:

```bash
pip install openpyxl pandas requests xmltodict python-dateutil
```

## Setup

1. Destination project must be deployed and have the same content as xlsx form. All questions should be in same order. 

2. Clone a copy of this repo somewhere on your local machine

3. Copy `sample-config.json` to `config.json` and add your configuration details
   for the source (`src`) and destination (`dest`) projects. If transfering from xls to kobo, duplicate src and destination url and token.
   
### Notes for General XLSX Data Transfer
- for initial transfer from xlsx to kobo, when there is no uuid, the column header for repeat groups must be repeat/{group name}/{xml header for question in repeating group}. Each question in repeat group must have its own column in xlsx.
- to associate media with a specific response/submission for initial transfer, when there is no _uuid column, row number of submission can be used. Media for the submission can be saved in file path ./attachments/{asset_uid}/{row_number}.
- for logical groups, column header can be {group name}/{xml header for question in repeating group}. The group name in the header must match Data Column Name in Kobo project.
- for ranking data, headers must be in this format: {xml header for question}/_1st_choice, {xml header for question}/_2nd_choice, {xml header for question}/_3rd_choice, and so on.

- if data downloaded from kobo as xlsx with XML values and headers, repeat groups span across multiple tabs. Script supports this, and data for these repeat group responses can be edited in the respective tabs and reuploaded.
- to minimise errors with formatting when data needs to be cleaned, it's best to do initial transfer from xlsx, then download the kobo data from xlsx with XML values and headers. The downloaded xlsx from Kobo is best to work from since all headers will be in the format the script expects. 

## Edge Cases
- order of questions in google form, and kobo form can be different
- no effect if some questions in kobo form are not present in google form (the response cells for that column will just be empty)
- responses that are left blank in google form results show up correctly (also blank) in kobo
- if the question strings in kobo form and google form are not exact match, transfer will add columns in kobo data for the "extra" questions in google form 
  
### -w (when warning flag -w is passed)
- prints a warning if question strings/labels in kobo form, and xls seem similar (differences in capitalisation, spacing, and punctuation), but not the same. 
- prints warning if number of questions in kobo form and xlsx form do not match

## Limitations
- If transferring from google form xlsx data (running -gt), submissions will be duplicated each time the script is run. Even when google form xlsx data is uploaded, edited, and then reuploaded, it will show up as a new submission instead of editing the one in kobo. To avoid this, after transferring from google form xlsx into kobo once, download the kobo data in xlsx form and edit/reupload that one with the flag -xt.
- Similarly, if running -xt for initial xlsx data without uuid, submissions will be duplicated each time script is run. To avoid, after initial transfer, download data from kobo as xlsx and edit/work with that. 

<br>

- assumes that kobo project and xlsx form question types and labels match (does not throw error but transferred submissions will be recorded incorrectly)
- labels in xls can not contain '/' if it is not a repeating, or logical group
- any data transferred will be accepted by kobo. For example, if question type is number in kobo, but submission transferred is text/string, it will be saved as such. For questions types such as dropdown/select one, responses in xlsx can be any string and kobo will save (regardless of whether or not it is an option in the kobo project). 
- _submitted_by in Kobo will show username of account running the transfer, for all submissions.
- submission_time in Kobo will show the time transfer was completed. 'end' shows time of response submission.
- data could be recorded in Kobo as 'invalid' but code will not throw error in this case. For example, if date or time format is incorrect when uploading to a Kobo Date or Time question, it will save as "Invalid". 
- If ‘None’ is a response in submission, it will show up as blank after being transferred to kobo
- Although submissions will not be duplicated across multiple runs of the script, if the submissions contain attachment files, the files are duplicated on the server.

 ## Media Upload
Demo walks through this process:
 - for initial data upload, create folder named attachments, with subfolder name being the asset uid of form in kobo. To associate media with a specific submission, create subfolders named after the row number of the submission in the xlsx. For example, without initially having a uuid (in a case where data is imported from a different source), the file path for the media would be attachments/aMhhwTacmk9PLEQuv9etDS/2. Media within that folder must match the filename in xlsx form cell exactly.
- if data already has uuids, create attachments folder with a subfolder asset id. Within asset id subfolder, create folders each named after uuid of a response. Media associated with each uuid should be within that folder.
- If run.py is run with the attachments folder, media should save in kobo correctly. 
 
