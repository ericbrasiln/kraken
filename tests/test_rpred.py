# -*- coding: utf-8 -*-
import os
import unittest

from PIL import Image
from pytest import raises

from kraken.lib.models import load_any
from kraken.rpred import rpred
from kraken.lib.exceptions import KrakenInputException

thisfile = os.path.abspath(os.path.dirname(__file__))
resources = os.path.abspath(os.path.join(thisfile, 'resources'))

class TestRecognition(unittest.TestCase):

    """
    Tests of the recognition facility and associated routines.
    """
    def setUp(self):
        self.im = Image.open(os.path.join(resources, 'bw.png'))

    def tearDown(self):
        self.im.close()

    def test_rpred_outbounds(self):
        """
        Tests correct handling of invalid line coordinates.
        """
        with raises(KrakenInputException):
            nn = load_any(os.path.join(resources, 'toy.clstm'))
            pred = rpred(nn, self.im, {'boxes': [[-1, -1, 10000, 10000]], 'text_direction': 'horizontal'}, True)
            next(pred)
