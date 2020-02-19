# Appium & Selenium example

![Python application](https://github.com/vescuderog/appium-selenium-example/workflows/Python%20application/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Basic example of test cases with Appium and Selenium

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For building and running the application you need:

- [Python 3](https://www.python.org/) 
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [BrowserStack account](https://www.browserstack.com/)

### Installing

Create a virtual environment and activate it (Windows):

```shell
py -m venv env
.\env\Scripts\activate
```

Now that you’re in your virtual environment you can install the project packages:

```bash
pip install -r requirements.txt
```

If you want to leave your virtual environment:

```bash
deactivate
```
### Environment variables

* `BROWSERSTACK_USER` - BrowserStack username
* `BROWSERSTACK_ACCESS_KEY` - BrowserStack [access key](https://www.browserstack.com/app-automate/rest-api)
* `FACEBOOK_EMAIL` - Facebook username to log in to Facebook in the Selenium test
* `FACEBOOK_PASS` - Facebook password to log in to Facebook in the Selenium test

## Usage

Run all tests:

```python
pytest
```

More info: [Pytest usage and invocations](http://doc.pytest.org/en/latest/usage.html)

## Built With

* [Pytest](https://docs.pytest.org/en/latest/contents.html) - Testing framework
* [Selenium](https://selenium.dev/)
* [Appium](http://appium.io/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
