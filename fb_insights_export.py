import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from location_paths import (
    export_button_path,
    download_button_path,
    insights_selector_paths,
    format_selector_path,
    formats_selector_paths,
)


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)


with open("credentials.yml") as cred:
    creds = yaml.safe_load(cred)
    facebook_credentials = creds["facebook_credentials"]
    fb_page_info = creds["facebook_page_info"]

# in the string/Quotation marks enter the path to where you downloaded the chromedriver.
driver = webdriver.Chrome(
    chrome_options=option, executable_path="chromedriver_linux64/chromedriver"
)
# navigates you to the facebook page.
driver.get(fb_page_info["url"])


def login_to_fb(driver, username, password):
    # find the username and password field and enter the email and password.
    username_field = driver.find_elements_by_css_selector("input[name=email]")
    username_field[0].send_keys(username)
    password_field = driver.find_elements_by_css_selector("input[name=pass]")
    password_field[0].send_keys(password)
    # find the login button and click it.
    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()


def export_page_insights(selected_insights, selected_format):
    export_button = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, export_button_path))
    )
    export_button.click()

    select_insight_types(selected_insights)

    select_format(selected_format)

    download_button = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, download_button_path))
    )
    download_button.click()


def select_format(selected_format):
    option_formats = ["xls", "csv"]
    if selected_format not in option_formats:
        raise ValueError("Invalid df type. Expected one of: %s" % option_formats)

    format_selection_field = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, format_selector_path))
    )
    format_selection_field.click()

    format_selection = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, formats_selector_paths[selected_format])
        )
    )
    format_selection.click()


def select_insight_types(selected_insights):
    option_insights = ["post", "page", "video"]
    if selected_insights not in option_insights:
        raise ValueError("Invalid df type. Expected one of: %s" % option_insights)

    insights_selection = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, insights_selector_paths[selected_insights])
        )
    )
    insights_selection.click()


if __name__ == "__main__":
    username = facebook_credentials["facebook_user"]
    password = facebook_credentials["facebook_password"]
    login_to_fb(driver, username, password)
    export_page_insights("video", "csv")
