import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

def create():
	folderName = str(sys.argv[1])
	user = Github(token).get_user()
	user.create_repo(folderName)
	
	print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
