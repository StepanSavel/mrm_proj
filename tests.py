import unittest, os

from mrm_proj.mrm.output_tools import FunctionsCodes, PerformanceCodes
from mrm_proj.mrm.add_trash import add_trash
from mrm_proj.mrm.remove import remove
from mrm_proj.mrm.recover import recover
from mrm_proj.mrm.regular_expression_rm import regular_expression_rm
from mrm_proj.mrm.arg_parser import empty_trash
from mrm_proj.mrm.show_trash import show_trash
from mrm_proj.mrm.read_config import read_config
from mrm_proj.mrm.output_tools import logging_and_silent


class DefaultTestPath(object):
    HOME_DIR = str(os.getenv('HOME'))
    DEFAULT_TRASH_DIR = str(os.path.join(HOME_DIR, 'mrm_trash'))
    TRASH_PATH = str(os.path.join(DEFAULT_TRASH_DIR, "trash"))
    INFO_PATH = str(os.path.join(DEFAULT_TRASH_DIR, "info"))
    LOG_PATH = str(os.path.join(DEFAULT_TRASH_DIR, "MRM.log"))
    DEFAULT_CONF = str(os.path.join(DEFAULT_TRASH_DIR, 'conf_mrm.json'))


silent = False


class TestMRM(unittest.TestCase):

    def setUp(self):
        os.mkdir("testDir")
        os.mkdir("testDir2")

        files = ["test1", "test2", "test3"]
        for file in files:
            with open("testDir/%s.txt" % file, "w"):
                pass

    def test_remove_file(self):
        file = "testDir/test1.txt"
        remove(file, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists(file))
        self.assertTrue(os.path.exists(os.path.join(DefaultTestPath.TRASH_PATH, "test1.txt")))

    def test_remove_empty_dir(self):
        file = "testDir2"
        remove(file, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists(file))
        self.assertTrue(os.path.exists(os.path.join(DefaultTestPath.TRASH_PATH, "testDir2")))

    def test_recover_file(self):
        file = "testDir/test2.txt"
        remove(file, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists(file))
        recover("test2.txt", DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertTrue(os.path.exists(file))

    def test_rex(self):
        files = "testDir/*.txt"
        regular_expression_rm(files, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists("testDir/test2.txt"))
        self.assertTrue(os.path.exists(os.path.join(DefaultTestPath.TRASH_PATH, "test2.txt")))

    def test_remove_dir(self):
        dir = "testDir"
        remove(dir, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists(dir))
        self.assertTrue()

    def test_recover_dir(self):
        dir = "testDir"
        remove(dir, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists(dir))
        recover(dir, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertTrue(os.path.exists(dir))

    def test_clear_trash(self):
        dir = "testDir"
        remove(dir, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH, dry=False)
        empty_trash(DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH, dry=False)
        self.assertFalse(os.path.exists(os.path.join(DefaultTestPath.TRASH_PATH, dir)))
        self.assertTrue()

    def test_show_trash(self):
        trash_content = show_trash(DefaultTestPath.TRASH_PATH, number_of_elem=10, dry=False)
        if trash_content:
            self.assertTrue()
        else:
            self.assertFalse()

    def test_read_config(self):
        config = read_config(DefaultTestPath.DEFAULT_CONF)
        if config:
            self.assertTrue()
        else:
            self.assertFalse()

    def test_regular_exp(self):
        dir = 'tesstDir'
        rex = 'testDir/*.txt'
        regular_expression_rm(rex, DefaultTestPath.TRASH_PATH, DefaultTestPath.INFO_PATH)
        self.assertFalse(os.path.exists(os.path.join(dir, '3.txt')))
        self.assertTrue(os.path.exists(os.path.join(DefaultTestPath.TRASH_PATH, '3.txt')))

    def test_output_lools(self):
        code = logging_and_silent(target="test", function_code=FunctionsCodes.REMOVE, performance_code=PerformanceCodes.GOOD)
        self.assertFalse(code != 0)
        self.assertTrue()
