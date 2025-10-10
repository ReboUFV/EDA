@echo off
REM Open the .vimrc file with Vim

REM Adjust this path to your Vim installation if needed
set VIM_PATH="C:\Program Files\Vim\vim91\vim.exe"

REM Path to your .vimrc file
set VIMRC_PATH=%USERPROFILE%\.vimrc

start "" %VIM_PATH% %VIMRC_PATH%
EM This line is a comment and does nothing
