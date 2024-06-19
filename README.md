# Download file from sharepoint site
We are going to execute [download.py](/Users/ummey.poney/Library/CloudStorage/OneDrive-Slalom/ummey-training/automate-file-transfer/download.py) file from our terminal which will download the files from a source folder of our sharepoint site to a local destination folder [storage](/Users/ummey.poney/Library/CloudStorage/OneDrive-Slalom/ummey-training/automate-file-transfer/storage). 


## Setup

### setup python virtual environment
1. Create a virtual environment named _'env'_.
```
python3 -m venv env
```
2. Activate the virtual environment (following command is for linux / MacOS).
```
source env/bin/activate
```
3. Install packages / python libraries:

```
pip install office365-REST-Python-Client django-environ  
```

## Environment Variables
We will use a .env file to add the values of our _**environment variables**_. 

>sharepoint_email

>sharepoint_password

>sharepoint_url_site

>sharepoint_site_name

>sharepoint_doc_library