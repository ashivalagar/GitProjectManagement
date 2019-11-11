#!/bin/bash

function create() {
    if [ "$1" == "" ]
    then 
        echo Please enter a repository name
    else
        cd $(dirname "$BASH_SOURCE")
        if [ "$2" == "" ]
        then
            python3 get_repo.py $1 Public
        else
            python3 get_repo.py $1 $2
        fi
        cd ~/Desktop/
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
    fi
}

function delete() {
    if [ "$1" == "" ]
    then 
        echo Please enter a repository name
    else
        cd $(dirname "$BASH_SOURCE")
        python3 remove_repo.py $1
        cd ~/Desktop/MyProjects
        rm -rf $1
    fi
}