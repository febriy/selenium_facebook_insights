# selenium_facebook_insights

Use Selenium to export facebook insights without Graph API.

## Installation

1. Clone the repository.

2. add credentials.yml in the main directory to include your fb_page link and credentials.

```yml
facebook_page_info:
    url: "https://www.facebook.com/xxxx/insights/?referrer=page_insights_tab_button"

facebook_credentials:
    facebook_user: "xxx@hotmail.com"
    facebook_password: "xxx"
```

3. Download [chromedriver](https://chromedriver.storage.googleapis.com/index.html). I use version 72.0.xx.  

## Usage

You can choose between posts, page, and video for the insights type, and between csv and xls for format type. Scroll down close to the end of the code and you will see the following:

```python
if __name__ == "__main__":
    username = facebook_credentials["facebook_user"]
    password = facebook_credentials["facebook_password"]
    login_to_fb(driver, username, password)
    export_page_insights("video", "csv") <- MODIFY THIS LINE ACCORDINGLY
```

After confirming your code, run it

`python fb_insights_export.py`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
