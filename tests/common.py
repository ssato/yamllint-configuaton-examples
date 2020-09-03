# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name,missing-function-docstring
"""Common utility test routines and classes.
"""
import os
import pathlib
import subprocess
import typing
import unittest


CURDIR = pathlib.Path(__file__).parent


def yml_path_itr(tcase: str, expect_success: bool = True
                 ) -> typing.Iterator[str]:
    """
    Yield a str represents a command to run given test case.
    """
    pattern = "res/{}*{}*.yml".format(
        tcase, "ok" if expect_success else "ng"
    )
    for yml_path in CURDIR.glob(pattern):
        yield yml_path


def ymllint_cmd(tcase: str, yml_path: str) -> str:
    """
    Yield a str represents a command to run given test case.
    """
    cnf = CURDIR.parent / "conf.d" / "yamllint.{}".format(tcase)
    return "yamllint -c {!s} {}".format(cnf, yml_path)


class YamlLintTestCase(unittest.TestCase):
    """Run ok and ng YAML Lint test cases automatically.
    """
    tcase = None

    def run_cmd(self, expect_success: bool = True):
        """
        Run yamllint.
        """
        if self.tcase is None or not self.tcase:
            return

        for ypath in yml_path_itr(self.tcase, expect_success):
            res = subprocess.run(
                ymllint_cmd(self.tcase, ypath).split(),
                stdout=subprocess.PIPE, check=False, env=os.environ
            )
            if expect_success:
                self.assertEqual(res.returncode, 0, res.stdout.decode("utf-8"))
            else:
                self.assertNotEqual(res.returncode, 0,
                                    res.stdout.decode("utf-8"))

    def test_10_ok_cases(self):
        self.run_cmd(expect_success=True)

    def test_20_ng_cases(self):
        self.run_cmd(expect_success=False)

# vim:sw=4:ts=4:et:
