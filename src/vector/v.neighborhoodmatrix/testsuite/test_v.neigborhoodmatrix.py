#!/usr/bin/env python3

############################################################################
#
# MODULE:       test_v.neigborhoodmatrix.py
# AUTHOR:       Salih Tangel
# PURPOSE:      Test neighborhood matrix output format handling of v.neighborhoodmatrix
# COPYRIGHT:    (C) 2026 OpenPlains Inc. and the GRASS Development Team
#               This program is free software under the GNU General
#               Public License (>=v2). Read the file COPYING that
#               comes with GRASS for details.
#
#############################################################################
import os
import grass.script as gs
from grass.gunittest.case import TestCase
from grass.gunittest.gmodules import SimpleModule
from grass.gunittest.main import test
import json

class TestNeighborhoodMatrixFormat(TestCase):
    """Tests for CSV/plain and JSON output handling"""

    vector = "census_wake2000"
    idcolumn = "STFID"

    def test_default_plain_stdout(self):
        """Default behavior: plain output to stdout"""
        module = SimpleModule(
            "v.neighborhoodmatrix",
            input=self.vector,
            idcolumn=self.idcolumn,
            format="plain",
        )
        self.assertModule(module)
        self.assertIn("|", module.outputs.stdout)

if __name__ == "__main__":
    test()
