# KeepIt Backup Preparation
When downloading zip files from Keepit (SaaS SharePoint backup solution), for some reason it makes an empty file for every item in the zip folder. This empty file has the same name as the actual file but has Fields in the file extension. No idea why it does this. This python script deletes each of those files with Fields in the file extension.
