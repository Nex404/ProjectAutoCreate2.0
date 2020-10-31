#!/bin/bash

function create() 
{
    cd
    cd ProjectAutoCreate
    python3 .create.py $1
    cd ~/projects/my_projects/
    mkdir $1
    echo "Folder created"
    cd $1
    git init
    git remote add origin https://github.com/YOUR_USERNAME/$1.git
    echo "remote added"
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
    echo "first commit finished"
}

function remove()
{
    cd
    cd ProjectAutoCreate
    python3 .remove.py $1
    cd ~/projects/my_projects/
    echo "Do you realy want to delete your local repo? (y/n):"
    read state
    if [ $state == "y" ]; then
        rm -r -f $1
        echo "Folder successfully deleted!"
    else
        echo "Abborded!"
    fi
}

