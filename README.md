# "Obey The Testing Goat"
To-Do list project from ["Test Driven Development With Python"](https://www.obeythetestinggoat.com) book

### Environment ###
* Anaconda
* VS Code
* Python 3.8
* Django 3.0.3
* Chrome 83
* Selenium 3.141.0
* ChromeDriver 2.38
* Bootstrap 4.5

### Develop using Windows Subsystem for Linux (WSL 1) ###
1) Enable WSL component in Windows 10
2) Install Alpine WSL from Windows Store
3) Run Alpine WSL to initialize it and create new user
4) Setup Linux environment using script `.vscode/env_setup.bat`
5) [VS Code] Install "Remote - WSL" extension
6) [VS Code] Run command "Remote-WSL: Reopen Folder in WSL"
7) [VS Code] Install "Python" extension
8) [VS Code] Run "Preferences: Open Remote settings" and add path to local WebDriver to remote settings:
```
    "terminal.integrated.env.linux": {
        "PATH": "/mnt/c/Anaconda3/envs/tdd/Library/bin:${env:PATH}"
    }
```
