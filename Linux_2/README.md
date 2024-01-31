# Linux user management

## Problem

The management of personal information such as usernames, passwords, and email addresses often lacks organization and security, leading to difficulties in accessing and safeguarding sensitive data. Existing solutions may be complex or inadequate for individual needs, necessitating the development of a simple and efficient Personal Record Management System.

## Todo

- Create a dedicated user account specifically for the personal record management system using the Linux "useradd" command.

- Set a strong password for the user account using the "passwd" command.

- Use your preferred text editor (e.g., Nano or Gedit) to create a file structure like below.

```sh
Personal_Record_System/
├── credentials/
│   ├── usernames.txt
│   ├── passwords.txt
│   └── email_addresses.txt
├── notes/
│   ├── personal_notes.txt
│   └── important_dates.txt
└── backups/
    ├── backup_2023-06-13.zip
    └── backup_2023-06-20.zip
```
- Set restrictive permissions on their personal record files using the "chmod" command, ensuring only the user can access and modify them.

- Create backups for all your files.


```bash
$ sudo useradd developer

```