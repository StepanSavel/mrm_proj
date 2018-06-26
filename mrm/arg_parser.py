import argparse
import logging
import os
import sys

from mrm_proj.mrm.clear_trash import empty_trash
from mrm_proj.mrm.output_tools import logging_and_silent
from mrm_proj.mrm.read_config import read_config, Policy
from mrm_proj.mrm.recover import recover
from mrm_proj.mrm.regular_expression_rm import regular_expression_rm
from mrm_proj.mrm.remove import remove
from mrm_proj.mrm.show_trash import show_trash
from mrm_proj.mrm.trash_policy import trash_policy

from mrm_proj.mrm.confirm import ask_for_confirm


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("remove", nargs="*", help="file to remove")
    parser.add_argument("-r", dest="recover", help="recover file")
    parser.add_argument("-et", dest="empty", action="store_true", help="empty trash")
    parser.add_argument("-rex", dest="rex", help="remove by regular expression", action="store")
    parser.add_argument("-s", dest="silent", help="Silent mod", action="store_true")
    parser.add_argument("-d", dest="dry", action="store_true", help="dry-run mod")
    parser.add_argument("--show", nargs="?", const="15", help="show N elements in trash")
    parser.add_argument("--size", help="set size policy")
    parser.add_argument("--day", help="set day policy")
    parser.add_argument("--conf", help="load new config")
    parser.add_argument("-c", dest="confirm", action="store_true", help="Ask for confirm")
    parser.add_argument("-p", dest="policy", action="store_true", help="change policy from day to size")

    args = parser.parse_args()

    config = read_config()

    trash_fold = config['trash_p']
    log_path = config['log']
    policy = config['policy']
    day = config['day']
    size = config['size']
    silent = config['silent']
    dry = config['dry']

    trash_path = os.path.join(trash_fold, 'trash')
    info_path = os.path.join(trash_fold, 'info')

    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=log_path)

    if not os.path.exists(trash_path):
        os.mkdir(trash_path)
        os.mkdir(info_path)

    if args.conf:
        new_conf_file = args.conf
        config.update(read_config(new_conf_file))
    if args.silent:
        silent = True
    if args.size:
        size = int(args.size)
    if args.day:
        day = int(args.day)
    if args.dry:
        dry = True
    if args.confirm:
        confirm = ask_for_confirm()
        if confirm is False:
            sys.exit(0)
    if args.policy:
        policy = Policy.SIZE
        print("policy set on size")
    if args.remove:
        for target in args.remove:
            path, function_code, performance_code = remove(target, trash_path, info_path, dry)
            logging_and_silent(path, function_code, performance_code, silent)
    if args.recover:
        for target in args.recover:
            path, function_code, performance_code = recover(target, trash_path, info_path, dry)
            logging_and_silent(path, function_code, performance_code, silent)
    if args.empty:
        path, function_code, performance_code = empty_trash(trash_path, info_path, dry)
        logging_and_silent(path, function_code, performance_code, silent)
    if args.rex:
        subtree = '/home/stepan/test'
        path, function_code, performance_code = regular_expression_rm(subtree, args.rex, trash_path, info_path)
        logging_and_silent(path, function_code, performance_code, silent)
    if args.show:
        number_of_elements = int(args.show)
        content_to_show = show_trash(trash_path, number_of_elements, dry)
        if not content_to_show:
            print('No content to show')
        else:
            print('last' + str(number_of_elements) + 'elements in trash' + str(content_to_show))
    if not args.recover:
        path, function_code, performance_code = trash_policy(trash_path, info_path, policy, day, size)
        logging_and_silent(path, function_code, performance_code, silent)


if __name__ == '__main__':
    main()
