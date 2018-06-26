"""MODULES:
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
    Removes files by policy (time/size)"""


from mrm_proj.mrm.arg_parser import main
from mrm_proj.mrm.clear_trash import empty_trash
from mrm_proj.mrm.confirm import ask_for_confirm
from mrm_proj.mrm.output_tools import FunctionsCodes, PerformanceCodes, logging_and_silent
from mrm_proj.mrm.read_config import read_config, DefaultPath, Policy
from mrm_proj.mrm.recover import recover
from mrm_proj.mrm.regular_expression_rm import regular_expression_rm
from mrm_proj.mrm.remove import remove
from mrm_proj.mrm.show_trash import show_trash_
from mrm_proj.mrm.show_progress import progress
from mrm_proj.mrm.trash_policy import trash_policy
from mrm_proj.mrm.add_trash import add_trash