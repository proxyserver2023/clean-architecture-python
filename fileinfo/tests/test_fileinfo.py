#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fileinfo
----------------------------------

Tests for `fileinfo` module.
"""

import pytest
from fileinfo.fileinfo import FileInfo


def test_init():
    filename = 'my_file_name.txt'
    f = FileInfo(filename)
    assert f.filename == filename


def test_init_relative():
    filename = 'my_file_name_with_another_extension.ext'
    relative_path = f'../{filename}'
    f = FileInfo(relative_path)
    assert f.filename == filename
