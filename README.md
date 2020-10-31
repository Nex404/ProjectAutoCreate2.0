# ProjectAutoCreate2.0 (public version)

this repo is to automate the creation and deletion of git repositories and local folders   

## Installation
clone the folder to your home directory
```
cd   
git clone https://github.com/Nex404/ProjectAutoCreate
cd ProjectAutoCreate2.0
```
install all requirements   
```
pip3 install -r requirements.txt
```
create an .env file    
```
touch .env
```
open the .env file and enter your Github token in this format:   
```
TOKEN = "YOUR_GITHUB_TOKEN"
```
open your .my_commands.sh file and replaye "YOUR_USERNAME" with your Github username   

open your .bashrc in some editor and paste the following to the EOF

```
source ~/ProjectAutoCreate2.0/.my_commands.sh
```
after that source your .bashrc  
```
source .bashrc
``` 
To prevent some unexpected error create the following folder:   
```
cd
mkdir projects
mkdir projects/my_projects
``` 

## Usage

The shell script creates 2 new functions to use globaly.   
   
With the "create" command you create a folder with the name you choose after the command. The folder will be created in the directory ~/projects/my_projects/ 
also a git repository will be created and linked with your local folder. Finaly VS Code will be opened.   

   
The "remove" command removes the folder and the repo of your choice.
