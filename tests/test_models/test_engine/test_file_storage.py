#!/usr/bin/python3
"""Test file for FileStorage"""
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """Tests for the storage engine class"""
    def test_file_path(self):
        """tests if __file_path is a str"""
        self.assertTrue(type(FileStorage._FileStorage__file_path) == str)
