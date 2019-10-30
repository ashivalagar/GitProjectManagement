import argparse
from github import Github

userName = "$(Enter Your Git User Name)"
passWord = "$(Enter Your Git Password)"

parser = argparse.ArgumentParser()
parser.add_argument(
    "git", type=str, help="Enter the name of the repository you want to create")
args = parser.parse_args()


def create_repo():
    directoryName = args.git
    user = Github(userName, passWord).get_user()
    repo = user.create_repo(directoryName)
    print("Succesfully created repository {}".format(directoryName))


if __name__ == "__main__":
    create_repo()