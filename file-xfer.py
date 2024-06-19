from office365.sharepoint.client_context import ClientContext
from googleapiclient.discovery import build

# ... (authentication setup for both SharePoint and Google Drive)

####inputs########
# This will be the URL that points to your sharepoint site. 
# Make sure you change only the parts of the link that start with "Your"
url_shrpt = 'https://twodegrees1.sharepoint.com/sites/test-event'
username_shrpt = 'YourUsername'
password_shrpt = 'YourPassword'
folder_url_shrpt = '/sites/YourSharepointSiteName/Shared%20Documents/YourSharepointFolderName/'

#######################


###Authentication###For authenticating into your sharepoint site###
ctx_auth = AuthenticationContext(url_shrpt)
if ctx_auth.acquire_token_for_user(username_shrpt, password_shrpt):
  ctx = ClientContext(url_shrpt, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print('Authenticated into sharepoint as: ',web.properties['Title'])

else:
  print(ctx_auth.get_last_error())
############################
  

def migrate_folder(sp_folder, gd_parent_folder_id):
    
    for item in sp_folder.files:
        # ... (download file content)
        gd_file = gd_service.files().create(
            body={'name': item.name, 'parents': [gd_parent_folder_id]},
            media_body=media, 
            fields='id'
        ).execute()

    for item in sp_folder.folders:
        gd_folder = gd_service.files().create(
            body={'name': item.name, 'parents': [gd_parent_folder_id], 'mimeType': 'application/vnd.google-apps.folder'}
        ).execute()
        migrate_folder(item, gd_folder.get('id'))

# ... (start migration from root folder)


if __name__ == "__main__":
    # ... (start migration from root folder)
    # Example:
    root_folder = ClientContext("your_sharepoint_url").web.get_folder_by_server_relative_url("your_sharepoint_folder_path")
    migrate_folder(root_folder, "your_google_drive_parent_folder_id")
