import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
user = Github(token).get_user()
folderName = str(sys.argv[1])


def remove():
    if input("Do you realy want to remove your Github repo {} (y/n)? :" .format(folderName)) == "y":
        try:
            repo = user.get_repo(folderName)
            repo.delete()
            print("Repo {} successfully deleted!" .format(folderName))
            
        except Exception as e:
            print("There is no such repo!")
            

if __name__ == "__main__":
    remove()
