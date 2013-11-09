#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import twoch
import unittest
import tempfile

class TwochTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, twoch.app.config["DATABASE"] = tempfile.mkstemp()
        twoch.app.config["TESTING"] = True
        self.app = twoch.app.test_client()
        twoch.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(twoch.app.config["DATABASE"])

    def test_empty_db(self):
        rv = self.app.get("/")
        print(rv.data)
        assert rv.data

if __name__ == "__main__":
    unittest.main()
