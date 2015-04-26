#!/usr/bin/python

from deviceTest import TestDevice
from acceleratorTests import TestAccelerator
from linacTests import TestLinac
from ringTests import TestRing
from sectionTests import TestSection
from linacAbstractSectionTests import TestLinacAbstractSection
from linacSectionTests import TestSectionBase, TestSectionElements
from linacSubsectionTests import TestLinacSubsection
from ringAbstractSectionTests import TestRingAbstractSection
from ringSectionTests import TestRingSection
from ringSubsectionTests import TestRingSubsection
from iconTests import TestIcon
from svgTests import TestSvg
from arcDrawingToolsTests import TestArcTools
import unittest

unittest.main()