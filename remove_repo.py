#!/usr/bin/python

import argparse
from github import Github
import github
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

userName = "$(Enter Git UserName)"
passWord = "$(Enter Git Password)"

g = Github(userName, passWord)

parser = argparse.ArgumentParser()
parser.add_argument(
    "dir", type=str, help="Enter the name of the repository you want to create")
args = parser.parse_args()
repoName = args.dir

options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()
browser.get('http://github.com/login')


def remove_repo():
    browser.find_elements_by_xpath(
        "//input[@name='login']")[0].send_keys(userName)
    browser.find_elements_by_xpath(
        "//input[@name='password']")[0].send_keys(passWord)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    try:
        checkExistence = g.get_repo(userName + "/"+repoName)
    except github.GithubException:
        return "Repo Not Found"
    browser.get('https://github.com/' + userName +
                "/" + repoName + '/settings')
    # return "Repository Not Found. Please Check That You Have Entered The Correct Name"
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(repoName)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    try:
        checkDeleted = g.get_repo(userName + "/"+repoName)
    except github.GithubException:
        return "Sucessfully Deleted"


if __name__ == "__main__":
    result = remove_repo()
    print(result)
    browser.quit()
