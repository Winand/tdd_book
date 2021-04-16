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

### Develop using Windows Subsystem for Linux (WSL 1*) ###
1) Enable WSL component in Windows 10
2) Install Alpine WSL from Windows Store
3) Run Alpine WSL to initialize it and create new user
4) Setup Linux environment using script `.vscode/env_setup.bat`
5) [VS Code] Install "Remote - WSL" extension
6) [VS Code] Run command "Remote-WSL: Reopen Folder in WSL"
7) [VS Code] Install "Python" extension
8) [VS Code] Add local WebDriver path to workspace settings (`.vscode/settings.json`) or remote settings ("Preferences: Open Remote settings" command) then restart terminal in VS Code:
```
    "terminal.integrated.env.linux": {
        "PATH": "/mnt/c/Anaconda3/envs/tdd/Library/bin:${env:PATH}"
    }
```
9) Add `"FAIL_FAST": "",  // --failfast` to `.vscode/settings.json`

\* WSL 2 cannot connect to Selenium WebDriver started on `localhost` in Windows
\[[1](https://docs.microsoft.com/ru-ru/windows/wsl/compare-versions#accessing-windows-networking-apps-from-linux-host-ip),
[2](https://github.com/microsoft/WSL/issues/4932#issuecomment-591733193)\]
