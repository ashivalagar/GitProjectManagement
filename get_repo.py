#!/usr/bin/python

import argparse
from github import Github

userName = "$(Enter Git UserName)"
passWord = "$(Enter Git Password)"

parser = argparse.ArgumentParser()
parser.add_argument(
    "dir", type=str, help="Enter the name of the repository you want to create")
parser.add_argument(
    "vis", type=str, help="Enter whether you want the repository to be private or not")
args = parser.parse_args()


def create_repo():
    dirName = args.dir
    if (args.vis == "Private"):
        privateRepo = True
    else:
        privateRepo = False
    user = Github(userName, passWord).get_user()
    print(privateRepo)
    repo = user.create_repo(dirName, private=privateRepo)
    print("Succesfully created repository {}".format(dirName))


if __name__ == "__main__":
    create_repo()
