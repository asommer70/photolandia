#!/usr/bin/python
#
# Test the server.
#

import sys
import os
sys.path.insert(0, '../')
import server
import unittest
import json

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def tearDown(self):
        """Do the cleanup..."""

    def test_get_json(self):
        rv = self.app.get('/')

        assert type(json.loads(rv.data)) == dict


if __name__ == '__main__':
    unittest.main()
