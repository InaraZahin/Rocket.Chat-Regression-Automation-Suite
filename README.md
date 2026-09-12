# Rocket.Chat Regression Automation Suite

An end-to-end regression test suite for [Rocket.Chat](https://open.rocket.chat), built with **Python**, **Selenium WebDriver**, and **Pytest**, using the Page Object Model to keep tests maintainable as the application changes.

## What it covers

48 automated test cases across 12 functional areas of Rocket.Chat, including:

- Login / logout
- Creating and deleting users, channels, and teams
- Posting, editing, and reacting to messages (Post, Message Actions)
- Direct messages and discussions
- Channel and user options
- Search and directory search
- View modes (condensed / medium / extended)

Each functional area has its own Page Object (in `Pages/`) and a matching test file (in `Tests/`), so a UI change only requires updating one page object rather than every test that touches that page.

## Tech stack

- **Selenium WebDriver** for browser automation
- **Pytest** as the test runner, with fixtures for test setup/teardown
- **BrowserStack** integration for running tests against real remote browsers (Chrome, Firefox, Safari, IE) in addition to local runs
- **Allure** and **pytest-html** for test reporting

## Project structure

```
Config/       Test data and environment configuration
Pages/        Page Object classes, one per screen/feature
Tests/        Test cases, one file per feature area
Screenshots/  Reference screenshots of tested workflows
```

## Setup

1. Clone the repo and install dependencies:
   ```
   git clone https://github.com/InaraZahin/Rocket.Chat-Regression-Automation-Suite.git
   cd Rocket.Chat-Regression-Automation-Suite
   pip install -r requirements.txt
   ```

2. If you want to run tests against BrowserStack (remote browsers), set these environment variables first — never hardcode them:
   ```
   export BROWSERSTACK_USERNAME=your_username
   export BROWSERSTACK_ACCESS_KEY=your_access_key
   ```

## Running the tests

Run the full suite locally (Chrome by default):
```
pytest Tests/
```

Generate an HTML report:
```
pytest Tests/ --html=report.html
```

Generate an Allure report:
```
pytest Tests/ --alluredir=allure-results
allure serve allure-results
```

## Notes

- Test data lives in `Config/data_local.py` (local runs) and `Config/data_open.py` (against the public open.rocket.chat instance) — both use placeholder test accounts, not real credentials.
- `Screenshots/` contains reference captures from test runs, useful for visually confirming what each test covers.
