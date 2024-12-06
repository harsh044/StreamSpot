from fastapi import APIRouter
from utils.response import response
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from utils.dbconnect import mydb

router = APIRouter()

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file', 
          'https://www.googleapis.com/auth/drive']

mycol = mydb["streamspot"]

@router.post("/sync_movies")
def sync_movies_api():
    try:
        # service = authentication()
        """Authenticate the user and return the Drive API service."""
        creds = None

        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=8080)
        
        # Build the Drive API service
        service = build('drive', 'v3', credentials=creds)

    except Exception as e:
        return response(1000)

    query = "visibility = 'anyoneWithLink' and name = 'Movies'"

    results = service.files().list(
        pageSize=10, fields="files(id, name)", q=query).execute()
    items = results.get('files', [])

    if not items:
        return response(1008)

    flag = None
    for item in items:
        # flag = check_files(item, service)
        try:
            # List all permissions for the folder
            permissions = service.permissions().list(fileId=item['id']).execute()

            # Check if anyone has access to the folder
            for permission in permissions.get('permissions', []):
                if permission.get('type') == 'anyone':
                    # Check the role (can be 'reader', 'writer', or 'commenter')
                    role = permission.get('role')
                    print(f"Folder is shared with anyone. Role: {role}")
                    flag = True
                else:
                    # If not shared with anyone, create a permission for 'anyone'
                    print("Folder is not shared with anyone. Sharing it now...")
                    new_permission = {
                        'type': 'anyone',
                        'role': 'reader',  # You can change this to 'writer' or 'commenter' based on your needs
                    }

                    # Create the permission
                    service.permissions().create(fileId=item['id'], body=new_permission).execute()
                    print("Folder has been shared with anyone successfully.")
                    flag = True
        
        except Exception as e:
            return response(1005)

    if flag:
        # files_links = get_links(item, service)
        try:
            """Get all files in the folder by folder ID and return shareable links."""
            # Query the folder to list its files
            query = f"'{item['id']}' in parents"
            results = service.files().list(
                pageSize=1000,  # Adjust as necessary
                fields="files(id, name)",
                q=query
            ).execute()

            files = results.get('files', [])
            if not files:
                print('No files found in the folder.')
                return response(1008)

            print('Files and their shareable links:')
            files_links = []
            already_exist = []
            for file in files:
                file_id = file['id']
                file_name = file['name']

                check_name = mycol.find_one({"movie_name": file_name})

                if check_name:
                    already_exist.append(check_name)
                    continue
                
                # Construct the shareable links
                file_link = f"https://drive.google.com/file/d/{file_id}/view"
                download_link = f"https://drive.google.com/uc?id={file_id}&export=download"
                print(f"{file_name}: {file_link}")
                print(f"Download link: {download_link}")

                # Prepare data for insertion
                mydata = {
                    "movie_name": file_name,
                    "movie_link": file_link,
                    "download_link": download_link,
                    "movie_poster_link": None,
                    "movie_category": None
                }
                files_links.append(mydata)

            # Insert data into the database
            if len(files_links) > 0:
                mycol.insert_many(files_links)
                return response(1010)
            elif len(already_exist) > 0:
                return response(1012)
            else:
                return response(1011)

        except Exception as e:
            return response(1005)