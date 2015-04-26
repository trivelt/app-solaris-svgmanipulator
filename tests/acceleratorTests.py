#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Accelerator import Accelerator
from src.Device import Device
import src.svg as svg
from lxml import etree


class TestAccelerator(unittest.TestCase):
    def setUp(self):
        self.acc = Accelerator()

    def testAcceleratorInit(self):
        acc = Accelerator()
        self.assertNotEqual(acc.sections, None)




    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()