#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.SettingsCloud import SettingsCloud

class TestSettingsCloud(unittest.TestCase):
    def setUp(self):
        SettingsCloud.resetSettings()

    def testSetGetValue(self):
        color = "red"
        SettingsCloud.setParameter("color", color)
        self.assertEqual(SettingsCloud.getParameter("color"), "red")
        self.assertEqual(SettingsCloud.getParameter("colour"), None)

    def testClearSettings(self):
        self.assertEqual(SettingsCloud.getParameter("color"), None)
        SettingsCloud.setParameter("color", "green")
        self.assertEqual(SettingsCloud.getParameter("color"), "green")
        SettingsCloud.resetSettings()
        self.assertEqual(SettingsCloud.getParameter("color"), None)

    def testUpdateSettings(self):
        SettingsCloud.setParameter("size", "20")
        self.assertEqual(SettingsCloud.getParameter("size"), "20")
        SettingsCloud.setParameter("size", "153")
        self.assertEqual(SettingsCloud.getParameter("size"), "153")

    def tearDown(self):
        SettingsCloud.resetSettings()

if __name__ == '__main__':
    unittest.main()