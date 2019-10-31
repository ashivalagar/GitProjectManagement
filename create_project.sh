#!/bin/bash

function create() {
    cd $(dirname "$BASH_SOURCE")
    python3 get_repo.py $1
    cd ~/Desktop/;
    if [ -d "./MyProjects" ]
    then
        cd MyProjects
        # echo this
    else
        mkdir MyProjects
        cd MyProjects
        # echo now this
    fi
    mkdir $1
    cd $1
    git init
    git remote add origin git@github.com:ashivalagar/$1.git
    touch README.md
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
}