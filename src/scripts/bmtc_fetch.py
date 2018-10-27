import os
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CUR_DIR)
REPO_DIR = os.path.dirname(ROOT_DIR)

import sys
sys.path.insert(0, ROOT_DIR)

import requests
import unittest
import pandas as pd
from bs4 import BeautifulSoup

from wrappers.logger import loggerFetch
from includes.settings import SITE_URL, BMTC_URL

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

TRIP_PLANNER_URL = '{bmtc_url}/Trip_Planner/'.format(bmtc_url=BMTC_URL)
FARES_URL = '{TRIP_PLANNER_URL}/FareSearchDetails.jsp?selected='.format(TRIP_PLANNER_URL=TRIP_PLANNER_URL)

GENERAL_SERVICE = 'gns'
ATAL_SARIGE_SERVICE = 'ats'
VAYU_VAJRA_SERVICE = 'vvs'
AC_SERVICE = 'acs'

TIMETABLE_URL = '{TRIP_PLANNER_URL}/TimeTableDetails.jsp?select=gens'.format(TRIP_PLANNER_URL=TRIP_PLANNER_URL)
ROUTE_URL = '{TRIP_PLANNER_URL}/Busstoplist.jsp?'.format(TRIP_PLANNER_URL=TRIP_PLANNER_URL)

DATA_DIR = REPO_DIR + '/data'
TIMETABLE_FILE_PREFIX = DATA_DIR + '/TimeTablePage_'
ROUTE_FILE_PREFIX = DATA_DIR + '/RouteNo_'
MAX_PAGE = 128


#############
# Functions
#############

def create_dir(dirname):
    try:
        os.makedirs(dirname)
    except OSError as e:
        if e.errno != os.errno.EEXIST:
            raise

def fetch_fares(logger, dirname, fare_type=None, url=None, mode=None):
    if not fare_type:
        fare_type = GENERAL_SERVICE

    if not url:
        url = FARES_URL + fare_type
    
    filename = '{fare_type}.html'.format(fare_type=fare_type)

    if mode:
        try:
            logger.info('Fetching URL[{url}]'.format(url=url))
            response = requests.get(url)
        except Exception as e:
            logger.error('Caught Exception[{excpetion}]'.format(excpetion=e))
        html_source = response.text
    else:
        with open(filename, 'r') as html_file:
            logger.info('Reading [%s]' % filename)
            html_source = html_file.read()

    bs = BeautifulSoup(html_source, 'html.parser')
    table_list = bs.findAll('table')
    logger.debug(table_list)

    for table in table_list:
        logger.debug(table)
        if False: #FIXME
            filename = dirname + panchayat_name + '.html'
            # logger.info('Reading file[{file}]'.format(file=filename))
            logger.info('Fetching [%s]' % route_url)

            try:
                df = pd.read_html(panchayat_url)[3]
            except Exception as e:
                logger.error('Exception when reading HTML[%s]' % e)
                exit(0)
            logger.info(str(df.head()))
            logger.info('Dumping [%s]' % filename)
            df.to_html(filename)
            filename = filename.replace('.html', '.csv')
            logger.info('Exporting [%s]' % filename)
            df.to_csv(filename, index=False)

            
def fetch_various_fares(logger, dirname=None):
    create_dir(dirname)
    fetch_fares(logger, dirname, fare_type=GENERAL_SERVICE)
    fetch_fares(logger, dirname, fare_type=ATAL_SARIGE_SERVICE)
    fetch_fares(logger, dirname, fare_type=VAYU_VAJRA_SERVICE)
    fetch_fares(logger, dirname, fare_type=AC_SERVICE)

    return 'SUCCESS'

def download_route(logger, route_id, bus_no):
    # the quote to take care of the space in the bus number
    url = ROUTE_URL + 'routeid={route_id}&busno={bus_no}'.format(route_id=route_id, bus_no=requests.utils.quote(bus_no))

    filename = ROUTE_FILE_PREFIX + str(bus_no) + '.csv'
    if os.path.exists(filename):
        # When database is ready, this info can be recorded there
        logger.info('File[{file}] already downloaded. Skipping it'.format(file=filename))
        return 0
    else:
        logger.info('Fetching URL[{url}]'.format(url=url))        
        df = pd.read_html(url)[2] #FIXME why are there 3 tables on this URL
        logger.info('Writing File[{file}]'.format(file=filename))
        df.to_csv(filename, index=False)

    # No point downloading the HTML. Retaining till above FIXME is fixed
    if False:
        logger.info('Fetching URL[{url}]'.format(url=url))
        try:
            response = requests.get(url)
            # df = pd.read_html(url)[1]  # Can't use as we need to collect bus routes from the HTML
        except Exception as e:
            logger.error('Caught Exception[{excpetion}]'.format(excpetion=e))
            exit(0)
        filename = filename.replace('.csv', '.html')
        with open(filename, 'w') as html_file:
            logger.info('Writing [{file}]'.format(file=filename))
            html_file.write(response.text)
        html_source = response.text
        
    return 0

def fetch_timetable_html(logger, page=None, url=None):
    if not page:
        page = 0

    if not url:
        count = page * 20
        url = TIMETABLE_URL  + '&count={count}&page={page}'.format(count=count, page=page)
        logger.info('fetch_timetable_html for url[{url}]'.format(url=url))

    filename = TIMETABLE_FILE_PREFIX + str(page) + '.html'
    if os.path.exists(filename):
        #FIXME When database is ready, this info can be recorded there
        logger.info('File[{file}] already downloaded. Skipping it'.format(file=filename))
        with open(filename, 'r') as html_file:
            logger.info('Reading [{file}]'.format(file=filename))
            html_source = html_file.read()
    else:
        #count = page * 20
        if page == 0:
            url = TIMETABLE_URL  + '&count=0&page=0'
        logger.info('Fetching URL[{url}]'.format(url=url))
        try:
            response = requests.get(url)
            # df = pd.read_html(url)[1]  # Can't use as we need to collect bus routes from the HTML
        except Exception as e:
            logger.error('Caught Exception[{excpetion}]'.format(excpetion=e))
            exit(0)
        with open(filename, 'w') as html_file:
            logger.info('Writing [{file}]'.format(file=filename))
            html_file.write(response.text)
        html_source = response.text

    return html_source

def download_timetable_details(logger, dirname, download_busroutes=None):
    if not download_busroutes:
        download_busroutes=True
        
    page = 0
    while True:
        logger.info('Fetch TimeTableDetails for page[{page}]'.format(page=page))
        html_source = fetch_timetable_html(logger, page)

        # Download the bus routes only if requested, default is download
        if download_busroutes:
            bs = BeautifulSoup(html_source, 'html.parser')
            p_list = bs.findAll('p', attrs={'id':'viewbusstop'})

            # Extract the various bus routes based on bus number
            for p in p_list:
                a = p.a
                logger.info(a['href'])
                (route_id, bus_no) = a['href'].strip('javascript:child_open(').strip(')').split(',')
                download_route(logger, route_id.strip("'"), bus_no.strip("'"))

        # Find next page. href looks like this - TimeTableDetails.jsp?select=gens&count=20&page=1
        try:
            a = bs.select_one("a[href*=page]")
        except Exception as e:
            logger.error('Caught Exception[{excpetion}]'.format(excpetion=e))
            break  #FIXME try to find the exact exception for break raise the rest

        #FIXME - some pages have next missing eg - http://223.30.102.30:8080//Trip_Planner//TimeTableDetails.jsp?select=gens&count=2160&page=108
        if not a:
            logger.warning('Page missing a Next? for page[{page}]'.format(page=page))
            page += 1
            if page > MAX_PAGE:
                break
            continue
        logger.info(a)
        href = a['href']
        page = int(href.split('=')[3])
        logger.info('href[{href}]'.format(href=href))
        logger.info('page[{page}]'.format(page=page))
        
    return 0

    '''
    The below is dead code for the former direct approach using the MAX_PAGE
    '''
    for page in range(0, MAX_PAGE+1): # MAX_PAGE inclusive
        filename = dirname + '{prefix}_{id}'.format(prefix=TIMETABLE_FILE_PREFIX, id=page) + '.csv'
        if os.exists(filename):
            # When database is ready, this info can be recorded there
            logger.info('File[{file}] already downloaded. Skipping it'.format(file=filename))
            continue
    
        count = page * 20
        url = TIMETABLE_URL  + '&count={count}&page={page}'.format(count=count, page=page)
        logger.info('Fetch TimeTableDetails from URL[{url}] page[{page}] into {directory}'.format(url=url, page=page, directory=dirname))
        try:
            df = pd.read_html(url)[1]  # the table of interest from the list
        except Exception as e:
            logger.error('Exception when reading HTML:[{exception}]'.format(exception=e))
            exit(0)
            
        logger.info('Writing to [{file}]'.format(file=filename))
        df.to_csv(filename, index=False)

    return 0

def aggregate_timetable_details(logger):
    """
    Join all the pages of time table into one single sheet
    """
    df_array = []
    for page in range(0, MAX_PAGE+1): # MAX_PAGE inclusive
        filename = dirname + 'TimeTablePage_{}'.format(page) + '.csv'
        if os.exists(filename):
            # When database is ready, this info can be recorded there
            logger.info('File[{file}] already downloaded. Reading it'.format(file=filename))
            url = filename
        else:
            count = page * 20
            url = TIMETABLE_URL  + '&count={count}&page={page}'.format(count=count, page=page)
            logger.info('Fetch TimeTableDetails from URL[{url}] page[{page}] into {directory}'.format(url=url, page=page, directory=dirname))
            
        try:
            df = pd.read_html(url)[1]  # the table of interest from the list
        except Exception as e:
            logger.error('Exception when reading HTML:[{exception}]'.format(exception=e))
            exit(0)

        logger.info('Writing to [{file}]'.format(file=filename))
        df.to_csv(filename, index=False)
        df_array.append(df)

    df = pd.concat(df_array)
    print(df.head())
    print(df.tail())

    return 0

def fetch_timetable_details(logger, dirname=None):
    if not dirname:
        dirname = './Data/'

    download_timetable_details(logger, dirname)
    exit(0)
    #FIXME - This may no longer be required - read into DB directly perhaps
    aggregate_timetable_details(logger)

    return 0


def parse_timetable_details(logger, dirname=None):
    if not dirname:
        dirname = DATA_DIR
    files = os.listdir(dirname)
    logger.info('Files[%s]' % files)

    for basename in os.listdir(dirname):
        filename=os.path.join(dirname,basename)
        if TIMETABLE_FILE_PREFIX not in filename:
            logger.info('Skipping [{file}]'.format(file=filename))
            continue

        logger.info('Reading [{file}]'.format(file=filename))
        try:
            df = pd.read_csv(filename, encoding='utf-8-sig', header = None, names = column_names)
        except Exception as e:
            logger.error('Exception when reading filename[%s] - EXCEPT[%s:%s]' % (filename, type(e), e))

        logger.info(df.head())

        df.fillna('', inplace=True)
        logger.info(df.head())

        #FIXME Work in Progress

    return 0


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.logger = loggerFetch('info')
        self.logger.info('BEGIN PROCESSING...')

    def tearDown(self):
        self.logger.info('...END PROCESSING')

    def test_fetch_bmtc_data(self):
        dirname = '../../data/'
        #result = fetch_bmtc_data(self.logger, dirname=dirname)
        result = fetch_timetable_details(self.logger, dirname=dirname)
        self.assertEqual(result, 0)
        
    def test_parse_bmtc_data(self):
        dirname = '../../data/'
        result = parse_bmtc_data(self.logger, dirname=dirname)
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()
    
