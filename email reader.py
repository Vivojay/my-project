import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = "vivanjaiswal12@gmail.com"
password = "123paranjaiswal@"

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)
