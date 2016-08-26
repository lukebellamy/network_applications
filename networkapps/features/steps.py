from lettuce import *
from nose.tools import assert_equal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import signal


@step('I should see login button')
def check_text_present(step):
    time.sleep(5)

    try:
      world.browser.find_element_by_xpath("//*[@id='Login']")
    except NoSuchElementException as e:
      print e.message


@step(u'Given user go to "([^"]*)"')
def given_user_go_to_url(step, url):
    world.browser.get(url)
    time.sleep(20)


@step('I go to "([^"]*)"')
def i_go_to(step, location):
    world.browser.get(location)
    time.sleep(5)


@step(u'When a user click on "([^"]*)"')
def when_i_click_on_checkbox(step, css):
    world.browser.find_element_by_css_selector(css).click()
    time.sleep(5)

@step(u'When a user click "([^"]*)"')
def when_a_user_click_install(step, label):
    world.browser.find_element_by_link_text(label).click()




@step(u'When a user log in as "([^"]*)"')
def when_a_user_log_in_as_username(step, username):
    try:
        element = WebDriverWait(world.browser,10).until(EC.presence_of_element_located((By.ID, "logonbox-logoimage")))
    except NoSuchElementException as e:
        print e.message
    if element:
        username_field = world.browser.find_element_by_id("username")
        password_field = world.browser.find_element_by_id("password")
        username_field.send_keys(username)
        password_field.send_keys('xxxxxxxx')
        login_button = world.browser.find_element_by_id("loginBtn")
        login_button.click()
        time.sleep(2)


@step(u'And the user sees the app icon "([^"]*)"')
def and_the_user_sees_the_app_icon_image(step, image):
    world.browser.find_element_by_css_selector(image)


@step(u'When the user clicks on "([^"]*)"')
def when_the_user_clicks_on_apps_button(step, apps_button):
    apps_button = world.browser.find_element_by_id(apps_button)
    apps_button.click()
    time.sleep(5)


@step(u'And the user clicks on add apps')
def and_the_user_clicks_on_add_apps(step):
    add_apps_plus = world.browser.find_element_by_xpath(".//*[@id='resources-navigationbar']/a")
    add_apps_plus.click()
    time.sleep(5)


@step(u'And user should see the link with the text "([^"]*)"')
def and_user_should_see_the_link_with_the_text_apps(step, apps):
    app_options_list = world.browser.find_elements_by_xpath(".//a[@class='categoryname']")
    citrix_apps_text_list = []
    for obj in app_options_list:
        citrix_apps_text_list.append(obj.text)
    print "Apps:: ", apps
    print "---"
    assert apps in citrix_apps_text_list, "Citrix Administration Tools not present"


@step(u'When user click username with id "([^"]*)"')
def when_user_click_username_with_id_user(step, user):
    user_name_id = world.browser.find_element_by_id(user)
    user_name_id.click()


@step(u'And user clicks Log Off "([^"]*)"')
def and_user_clicks_log_off_button_off(step, button_off):
    log_off_button = world.browser.find_element_by_id(button_off)
    log_off_button.click()
    time.sleep(2)


@step(u'Then a "([^"]*)" should be seen')
def then_a_button_should_be_seen(step, button):
    log_on_element = world.browser.find_element_by_xpath(".//a[@class='button']")
    button_text = log_on_element.text
    print "button text", button_text, type(button_text)
    print "---"
    print "button", button, type(button)
    assert_equal(button,button_text)
    assert button == button_text, "Citrix Log off not successful"
    time.sleep(10)

#@step(u'Then cancel the download popup')
#def then_cancel_the_download_popup(step):
    #world.browser.switch_to().window(world.browser.get_window_handle())



