An end-to-end automated regression testing framework for Rocket.Chat, built with Python, Selenium WebDriver, and Pytest.

The framework validates core Rocket.Chat functionality after application changes and helps identify regressions before they reach production. It supports cross-browser testing, parallel execution, BrowserStack integration, and automated HTML and Allure reporting.

Key Features

* End-to-end UI regression testing
* Selenium WebDriver with Python
* Pytest-based test execution
* Cross-browser testing
* Parallel test execution with pytest-xdist
* Remote browser testing with BrowserStack
* HTML reporting with pytest-html
* Allure test reporting

Test Coverage

The regression suite covers major Rocket.Chat workflows, including:

Authentication

* Log in with username and password
* Log out

User Management

* Create a new user
* Search for users

Channels

* Create a new channel
* Add users to a channel
* Create discussions
* Post messages in public channels
* Post messages in private channels
* Search public channels
* Search private channels
* Favorite and unfavorite channels
* Mark channels as read or unread
* Hide and show channels
* Leave and join channels

Direct Messages

* Create a Direct Message (DM)
* Favorite and unfavorite DMs
* Mark DMs as read or unread
* Hide and show DMs

Messaging

* Post emojis
* Add reactions
* Add quotes
* Reply to threads

Display Modes

* Extended mode
* Medium mode
* Condensed mode

⸻

Prerequisites

Before running the test suite, ensure the following are installed:

* Python 3.9+
* pip
* Git
* PyCharm or another Python IDE
* Supported web browsers
* Required WebDriver executables
* Allure, if Allure reporting is required

⸻

Installation

1. Clone the Repository

git clone https://github.com/InaraZahin/Rocket.Chat-Regression-Automation-Suite.git
cd Rocket.Chat-Regression-Automation-Suite

2. Verify Python and pip

python --version
pip --version

Python can be downloaded from:

https://www.python.org/downloads/

3. Install Selenium

pip install -U selenium

4. Install Pytest

pip install pytest

5. Install HTML Reporting

pip install pytest-html

6. Install Allure Pytest

pip install allure-pytest

Install the Allure command-line tool separately.

Windows:

scoop install allure

macOS:

brew install allure

7. Install Parallel Execution Support

pip install pytest-xdist

8. Install BrowserStack Dependencies

Install the required BrowserStack Local package if BrowserStack execution is required.

⸻

Browser Setup

The framework supports cross-browser execution on browsers such as:

* Google Chrome
* Mozilla Firefox
* Safari
* Internet Explorer

Download the required WebDriver executables from:

https://www.selenium.dev/downloads/

Windows

Extract the appropriate WebDriver and add its location to the system PATH. It can also be placed in the Python Scripts directory if that directory is already included in PATH.

macOS

Place the WebDriver executable in a directory available on the system PATH, for example:

/usr/local/bin

Note: Modern versions of Selenium include Selenium Manager, which can automatically manage drivers in many environments. Manual driver installation may therefore not be required when using a recent Selenium version.

⸻

Running Tests

Run the Full Test Suite

pytest Tests

For verbose output:

pytest -v -s Tests

Run a Specific Test File

pytest Tests/filename.py

For verbose output:

pytest -v -s Tests/filename.py

⸻

Parallel Test Execution

The test suite supports parallel execution using pytest-xdist.

For example:

pytest -v -s -n 2 Tests

The value passed to -n specifies the number of parallel workers.

For example:

-n 2

runs tests using two workers.

For automatic worker allocation:

pytest -n auto Tests

⸻

Test Reports

HTML Reports

Generate an HTML report during test execution:

pytest -v -s --html=report.html Tests/filename.py

After execution, open report.html in a browser to view the test results.

To generate a self-contained HTML report:

pytest -v -s --html=report.html --self-contained-html Tests

⸻

Allure Reports

Run the tests and save the Allure results:

pytest -v -s --alluredir="./reports/allure_reports" Tests/filename.py

To generate and view the report:

allure serve ./reports/allure_reports

Allure will generate the report and launch it in the default browser.

⸻

BrowserStack

The framework supports running Selenium tests remotely through BrowserStack, allowing the regression suite to be executed against different combinations of:

* Browsers
* Browser versions
* Operating systems
* Test environments

BrowserStack credentials and capabilities must be configured before remote execution.

Refer to the BrowserStack documentation for setup instructions:

https://www.browserstack.com/docs/

Security: Do not commit BrowserStack usernames, access keys, passwords, or other credentials to the repository. Store credentials in environment variables or another secure configuration mechanism.

⸻

Recommended Project Structure

A typical project structure may look similar to:

QA.Automation/
│
├── Tests/
│   ├── test_login.py
│   ├── test_users.py
│   ├── test_channels.py
│   ├── test_messages.py
│   └── ...
│
├── reports/
│   └── allure_reports/
│
├── requirements.txt
├── pytest.ini
└── README.md

⸻

Installing Dependencies from requirements.txt

For easier project setup, project dependencies should ideally be maintained in a requirements.txt file.

Example:

selenium
pytest
pytest-html
pytest-xdist
allure-pytest
browserstack-local

Install all dependencies with:

pip install -r requirements.txt

⸻

Quick Start

# Clone the repository
git clone https://github.com/RocketChat/QA.Automation.git
# Navigate to the project
cd QA.Automation
# Install dependencies
pip install -r requirements.txt
# Run the regression suite
pytest -v Tests
# Run tests in parallel
pytest -v -n auto Tests
# Generate an HTML report
pytest -v --html=report.html --self-contained-html Tests

⸻

Tech Stack

Technology	Purpose
Python	Test automation language
Selenium WebDriver	Browser automation
Pytest	Test framework and execution
pytest-xdist	Parallel test execution
pytest-html	HTML test reporting
Allure	Detailed test reporting
BrowserStack	Cloud-based cross-browser testing
Git / GitHub	Version control
