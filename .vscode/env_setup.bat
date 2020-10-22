wsl -d Alpine su -c "sh env_alpine.sh"
REM Settings for non-root user:
wsl -d Alpine git config --global core.autocrlf true
