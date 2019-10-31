import argparse
from github import Github

userName = "YOUR_GIT_USERNAME"
passWord = "YOUR_GIT_PASSWORD"

parser = argparse.ArgumentParser()
parser.add_argument(
    "git", type=str, help="Enter the name of the repository you want to create")
args = parser.parse_args()


def create_repo():
    dirName = args.git
    user = Github(userName, passWord).get_user()
    repo = user.create_repo(dirName)
    print("Succesfully created repository {}".format(dirName))


if __name__ == "__main__":
    create_repo()
