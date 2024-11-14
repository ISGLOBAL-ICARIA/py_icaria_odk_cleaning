#!/usr/bin/env python

import odk_clean
import tokens

__author__ = "Andreu Bofill Pumarola"
__copyright__ = "Copyright 2024, ISGlobal Maternal, Child and Reproductive Health"
__credits__ = ["Andreu Bofill Pumarola"]
__license__ = "MIT"
__version__ = "0.0.1"
__date__ = "20241111"
__maintainer__ = "Andreu Bofill"
__email__ = "andreu.bofill@isglobal.org"
__status__ = "Dev"


if __name__ == '__main__':
    odk_clean.csv_cleaning(tokens.file_path,tokens.final_path)