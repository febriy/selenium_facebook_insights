# selenium_facebook_insights

Use Selenium to export facebook insights without Graph API

## Installation
Clone the repository

add credentials.yml in the main directory to include your fb_page link and credentials.

```yml
facebook_page_info:
    url: "https://www.facebook.com/xxxx/insights/?referrer=page_insights_tab_button"

facebook_credentials:
    facebook_user: "xxx@hotmail.com"
    facebook_password: "xxx"
```
Download [chromedriver](https://chromedriver.storage.googleapis.com/index.html). I use version 72.0.xx.  

## Usage

You can choose between posts, page, and video for the insights type, and between csv and xls for format type. 
```python
if __name__ == "__main__":
    username = facebook_credentials["facebook_user"]
    password = facebook_credentials["facebook_password"]
    login_to_fb(driver, username, password)
    export_page_insights("video", "csv")   <---- you can modify this. 
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)