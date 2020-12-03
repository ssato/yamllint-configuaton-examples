# Copyright (C) 2020 Satoru SATOH
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name,missing-function-docstring
"""ansible-typical test cases.
"""
from . import common as C


class TestCase(C.YamlLintTestCase):
    """
    ansible-typical test cases.
    """
    tcase = "ansible-typical"

# vim:sw=4:ts=4:et:
