import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A3Gn33IO8iXFlrM7L9jppi8xMzVxArM_xlIDwUDzNlf9cmPjCU4sWPoMkYKDmvvddhnHCEWcJqq5-xwDKJpj9J0JcR6zW1o4f24UE8PW8SySG8_CaAJYlINdAzbimwFBneivZNM'
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been succesfully moved")

    
    main()