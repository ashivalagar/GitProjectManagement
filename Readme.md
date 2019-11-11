# Git Project Automation

This is a simple set of command line functions to help automate creating and deleting of project repositories both on github and locally.

![Git Logo](assets/git-logo.jpg)

Setup
------
If you just want to dive right in and begin using these command line functions, you will need to clone the repository.

### Dependencies
Run,

```bash
$ pip install -r requirements.txt
```

to install all the necessary python dependencies.

You will also need to download and install ChromeDriver for Selenium. Instructions for installation of ChromeDriver can be found [here](https://yizeng.me/2014/04/20/install-chromedriver-and-phantomjs-on-linux-mint/).

You have successfully installed all the required dependencies! Yay!

### Environment
In essence our python script is funtional. We need to add our credentials in to make them completely executable but first let's make our bash command executable.

For this we need to source our shell script. This can simply be done by executing the following command in the terminal,

```bash
$ source "Enter Path_TO_Directory"
```

Enter the path to this git repository on your local machine.

What this does is makes the functions inside your shell script an executable command in your terminal. But this only works in the current runtime of your terminal. To make the command available indefinitely we can add it to our environment initialiser.

---
#### For Mac

```bash
$ nano ~/.bash_profile
```

#### For Linux

```bash
$ nano ~/.bashrc
```
---

Running the commands above should open a text editor in your terminal. Navigate to the bottom of the file and add in the following line.

```bash
source "{Enter Path_TO_Directory}"
```

You are now all set to use the automation commands.

Use
-----
This package comes with 2 commands,

### Create
To create a git repository. This command has 2 arguements.

```bash
$ create arg1 arg2
```

arg1 - Name of Repository

arg2 - Private

arg1 is a required but arg2 is an optional arguement. The repository created is public by default.

### Delete
To delete an existing git repository. This command has only 1 arguement.

```bash
$ delete arg1
```

arg1 - Name of Repository

Conclusion
===

Hope these commands help streamline your project management and that you guys enjoy using them!