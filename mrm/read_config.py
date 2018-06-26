"""
This module creates trash dir if it is not exist and reads config file
"""
import os
import json


class Policy(object):
    SIZE = 0
    DAY = 1


class DefaultPath(object):
    """This class contains default paths"""
    HOME_DIR = str(os.getenv('HOME'))
    DEFAULT_CONF = str(os.path.join(HOME_DIR, 'mrm_trash/conf_mrm.json'))
    DEFAULT_TRASH_DIR = str(os.path.join(HOME_DIR, 'mrm_trash'))
    DEFOULT_LOG = str(os.path.join(HOME_DIR, 'mrm_trash/MRM_trash.log'))
    BOLEANS = ["0", "1"]


def read_config(conf_file=DefaultPath.DEFAULT_CONF):
    """This function reads config file"""
    trash_path = str(DefaultPath.DEFAULT_TRASH_DIR)
    log_path = str(DefaultPath.DEFOULT_LOG)
    config = {
        "trash_p": trash_path,
        "log": log_path,
        "policy": 1,
        "silent": "False",
        "dry": "False",
        "day": 7,
        "size": 1000000
    }
    if not os.path.exists(conf_file):
        os.mkdir(trash_path)
        with open(conf_file, 'w') as jconf:
            json.dump(config, jconf)
    else:
        conf_type = os.path.splitext(conf_file)[1]

        if conf_type is '.json':
            with open(conf_file, 'r') as jconf:
                config = json.load(jconf)
        elif conf_type is'.txt':
            with open(conf_file, 'r') as txtconf:
                content = txtconf.readlines()
                content = [x.strip() for x in content]
                for x in content:
                    line = (x.split(" : "))
                    if line[1] in DefaultPath.BOLEANS:
                        config[line[0]] = (line[1])
                    else:
                        config[line[0]] = (line[1])

        return config
