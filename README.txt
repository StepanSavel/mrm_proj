
own rm for linux

INSTALL:
Write: sudo python setup.py install to install app

COMMANDS:
mrm file: remove file
mrm --lst number_of_files (int): show number_of_files in trash
mrm -r file: recover file
mrm -rex: remove by regular expression
mrm -et: empty trash
mrm -s: silent mode
mrm -d: dry\run mode
mrm --size: policy:size
mrm --day: policy:size
mrm --conf: load own configuration file
mrm -c: confirm mod

MODULES:
arg_parser
    Pars arguments of command line
    entry point of app
clear_trash
    Clears trash with help of its function empty_trash
confirm
    Asks for confirmation, returns confirm variable (True/False)
output_tools
    This module contains identification codes of functions and codes of performance, works with
    this codes ,silent mode and logging
read_config
    This module creates trash dir if it is not exist and reads config file, contains class with default paths
recover
    Contains function for restoring files or dirs from trash
remove
    Contains function for removing files or dirs in trash
regular_expression_rm
    Contains function for removing files in trash by regular expression
Show_trash
    Shows last N elements in trash
Show_progress
    Shows progress of removing
    Cosmetic tool
Trash_policy
    Removes files by policy (time/size)
