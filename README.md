# Gmail API Samples
Simple Gmail APIs with Python

# Few samples ready to retrieve
- Number of emails in a label
- Number of threads in a label

# Authentication
I found it very easy to run a small piece of code in my local computer.
This way, with a link, it will lead to a Browser which you can authenticate and will generate a token.pickle file. You can then upload that one to the cloud. I found it much easier than learning how to work with other authentication protocols in the Gmail API stack like OAUTH2.0.

You need to run the first part of the code with the authentication. Then on the Command Line you will get a link and the file will be downloaded to your computer. After that just get the token.pickle file and put it on your script's %WORKING_DIR% or in a secure one if that makes more sense.

# Dependencies
If easier to get started: https://developers.google.com/gmail/api/quickstart/python
