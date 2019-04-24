# Description
Command line tool to split a given file into multiple files by passing in max number of rows allowed in each file
# Currently Supported Formats
All formats that `fopen` of python can handle
# Setup
After pulling the repo, add the following line in your ~/.bash_profile. Replace the path to the path where this project is pulled
```
alias split='python3 {Absolute path of file-splitter folder}/run.py'
```
To load the changes
```
source ~/.bash_profile
```
# Command
```
split {Absolute path to file} {Max rows in each splitted file} {{-preserve-headers}} {{-debug}}
```
Command will generate a folder with splitted files
```
-preserve-headers
```
Optional parameter to include headers in each file that will generated
```
-debug
```
Optional parameter to turn on debug for a verbose output