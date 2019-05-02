#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fileinfo
----------------------------------

Tests for `fileinfo` module.
"""

import pytest
from fileinfo.fileinfo import FileInfo
from unittest.mock import patch


def test_init():
    filename = 'my_file_name.txt'
    f = FileInfo(filename)
    assert f.filename == filename


def test_init_relative():
    filename = 'my_file_name_with_another_extension.ext'
    relative_path = f'../{filename}'
    f = FileInfo(relative_path)
    assert f.filename == filename


def test_get_info():
    filename = 'somefile.ext'
    original_path = '../{}'.format(filename)
    with patch('os.path.abspath') as abspath_mock:
        test_abspath = 'some/abs/path'
        abspath_mock.return_value = test_abspath
        fi = FileInfo(original_path)
        assert fi.get_info() == (filename, original_path, test_abspath)
