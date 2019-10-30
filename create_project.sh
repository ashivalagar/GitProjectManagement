#!/bin/bash

function create() {
    cd $(dirname "$BASH_SOURCE")
    python3 get_repo.py $1
    cd ~/Desktop/;
    if [ -d "./MyProjects" ]
    then
        cd MyProjects
        echo this
    else
        mkdir MyProjects
        cd MyProjects
        echo now this
    fi
    mkdir $1
    cd $1
}