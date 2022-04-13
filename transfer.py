import dropbox
class Transfer:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def upload(self,src,destination):
        dbx = dropbox.Dropbox(self.accessToken)
        with open(src,'rb') as f:
            dbx.files_upload(f.read(),destination)

transfer = Transfer('sl.BFor3tBjYN85VZ-JKXU7VIN1101rAzVvc3hGN-WHkBgvRAxQWZKAab-pnfYz2gauAMB4aBKSK9m-zxiEVMsYd171p-FkJyR8yTQpT8H4644jloQy-Wy0-srCp65x5i4Le2ddvXQ')
src = input('Enter source path: ')
destination = input('Enter destination path: ')
transfer.upload(src,destination)
print('Files Uploaded')


