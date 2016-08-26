from lettuce import before, world, after
import time
from selenium import webdriver
from lettuce import step
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import AssertContextManager
from lettuce_webdriver.util import find_button,find_field
from lettuce_webdriver.util import find_option
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import config


@before.all
def setup_browser():
    print config.GLOBALS['env'], "GLOBALS"
    if config.GLOBALS['env'] == 'firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0")
        world.browser = webdriver.Firefox(profile)
        world.browser.maximize_window()
        world.browser.delete_all_cookies()
    else :
        headers = {'letmein':'p0o9iJJ66ete54'}
        for key, value in enumerate(headers):
            webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)]= value
        world.browser = webdriver.PhantomJS()
        world.browser.maximize_window()
        world.browser.delete_all_cookies()


@after.all
def tear_down(total):
    print "Total %d of %d scenarios passed!" % ( total.scenarios_ran, total.scenarios_passed)
    world.browser.quit()

@after.each_scenario
def get_screenshot(scenario):
    if scenario.passed == False:
        world.browser.save_screenshot('fdi.jpeg')

