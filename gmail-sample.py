from __future__ import print_function
import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# This is exactly like in the Google Guide
# I found that token.pickle is really easy to authenticate
# I'm unsure how safe it is to keep that file.

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # All of the below authenticates.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    # Finish Authentication, now run whatever you want.

    # In order to work out a Label you need to know the label ID.
    # The below code is commented but if you run it, it will print
    # the label IDs to get the label id numbers you need.
    # If you have the Label Name without the numbers it does not work.
    # 
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name']+ " "+label['id'])

    
    # This calls the Gmail API and will find my "Label_286"
    # Needs to be in the form of a list.
    label_ids = ["Label_286"]
    
    # Note I am using "Messages" and not "Threads".
    # "me" is allowed and will bring the user which is authorized by the token.
    # Otherwise you can type in "email@gmail.com" or similar.
    response = service.users().messages().list(userId="me", labelIds=label_ids).execute()
    
    # If you want to get Threads, not emails then:
    # response = service.users().threads().list(userId="me", labelIds=label_ids).execute()
    # And change commands accordingly in the response['messages'] vs. response['threads']
    
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])
    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId="me", labelIds=label_ids,
                                           pageToken=page_token).execute()
        messages.extend(response['messages'])
    return messages
   
if __name__ == '__main__':
    jorge = main()
    json_data = json.dumps(jorge)
    item_dict = json.loads(json_data)
    print("The total number of messages in the label is ... " + str(len(item_dict)))
