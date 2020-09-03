# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name,missing-function-docstring
"""indentation test cases.
"""
from . import common as C


class TestCase(C.YamlLintTestCase):
    """
    indentation test cases.
    """
    tcase = "indentation"

# vim:sw=4:ts=4:et:
