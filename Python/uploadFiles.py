import dropbox

import os
    for root, dirs, files in os.walk(file_from):
        for name in files:
      print(os.path.join(root, name))
        for name in dirs:
      print(os.path.join(root, name))

class TransferData:
#add__init__


    relative_path = os.path.relpath(local_path,file_from)
    dropbox_path = os.path.join(file_to,relative_path)

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
def main():
    access_token = 'sl.A3Gn33IO8iXFlrM7L9jppi8xMzVxArM_xlIDwUDzNlf9cmPjCU4sWPoMkYKDmvvddhnHCEWcJqq5-xwDKJpj9J0JcR6zW1o4f24UE8PW8SySG8_CaAJYlINdAzbimwFBneivZNM'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been succesfully moved")

    
    main()