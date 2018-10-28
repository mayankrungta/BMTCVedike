import os
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(CUR_DIR))
REPO_DIR = os.path.dirname(ROOT_DIR)

import sys
sys.path.insert(0, ROOT_DIR)

import time
import unittest
from bs4 import BeautifulSoup

from wrappers.logger import loggerFetch
from wrappers.sn import driverInitialize, \
    driverFinalize, displayInitialize, displayFinalize

###
# Django Settings for future
###

'''

djangodir = repodir + '/django/{site_url}/src'.format(site_url=SITE_URL)
sys.path.append(djangodir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libtech.settings')

import django

# This is so Django knows where to find stuff.
# This is so my local_settings.py gets loaded.
django.setup()

from bmtc.models import Route, Stop
'''


#######################
# Global Declarations
#######################

timeout = 10

URL = 'http://localhost:8000'


#############
# Functions
#############

def it_worked(logger, driver, url):
    driver.get(url)
    return driver


##########
# Tests
##########

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.logger = loggerFetch('info')
        self.logger.info('BEGIN PROCESSING')
        # Pass 0 for headless
        self.display = displayInitialize(1)
        #, path='/path/to/firefox/')
        self.driver = driverInitialize(browser='firefox')
        self.url = URL

    def tearDown(self):
        driverFinalize(self.driver)
        displayFinalize(self.display)
        self.logger.info('...END PROCESSING')

    @unittest.skip('Skip direct command test')
    def test_direct_cmd(self):
        cmd = 'curl -L -O %s' % url
        os.system(cmd)

    def test_it_worked(self):
        result = 'SUCCESS'
        self.driver.get(URL)
        self.assertIn(
            'Django: the Web framework for perfectionists with deadlines.',
            self.driver.title)
        # self.assertEqual('SUCCESS', result)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
