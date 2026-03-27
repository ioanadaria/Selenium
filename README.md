# Selenium with Python

A collection of Selenium WebDriver automation scripts and a pytest test suite demonstrating common browser automation techniques using Python.

## Project Structure

```text
Selenium-with-Python/
├── conftest.py              # Shared pytest fixtures (Chrome & Firefox drivers)
├── requirements.txt         # Pinned dependencies
├── tests/                   # pytest test suite
│   ├── test_alert.py
│   ├── test_authentication.py
│   ├── test_basic_navigation.py
│   ├── test_browser_dimensions.py
│   ├── test_checkboxes.py
│   ├── test_cookies.py
│   ├── test_file_upload.py
│   ├── test_resize_element.py
│   ├── test_select.py
│   └── test_stale_element.py
├── Selenium.py                       # Basic navigation with Firefox
├── Selenium_AddCookies.py            # Add and retrieve cookies
├── Selenium_DeleteAllCookies.py      # Delete all cookies
├── Selenium_DeleteCookieByName.py    # Delete a specific cookie by name
├── Selenium_alertAPI.py              # Handle browser alert dialogs
├── Selenium_ClickCheckbox.py         # Click a single checkbox
├── Selenium_ClickAllCheckboxes.py    # Click all checkboxes on a page
├── Selenium_selectByIndex.py         # Select dropdown option by index
├── Selenium_selectByValue.py         # Select dropdown option by value
├── Selenium_SelectAllMethods.py      # All Select class methods demonstrated
├── Selenium_HandleStaleElement.py    # Handle StaleElementReferenceException
├── Selenium_ResizeWebElement.py      # Resize a web element via ActionChains
├── Selenium_SetBrowserDimensions.py  # Set, maximize, minimize browser window
├── Selenium_AuthenticationWindows.py # Basic HTTP authentication via URL
├── Selenium_FileUpload_AutoIt.py     # File upload with AutoIt fallback
└── Selenium_xl.py                    # Read Excel files with openpyxl
```

## Prerequisites

- Python 3.8+
- Google Chrome (for Chrome-based tests)
- Firefox (for `test_basic_navigation.py` and `Selenium.py`)

ChromeDriver and GeckoDriver are managed automatically via `webdriver-manager` — no manual driver installation required.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ioanadaria/Selenium.git
   cd Selenium/Selenium-with-Python
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

Run the full test suite:

```bash
pytest tests/ -v
```

Run with an HTML report:

```bash
pytest tests/ -v --html=report.html
```

Run a specific test file:

```bash
pytest tests/test_cookies.py -v
```

## Test Coverage

| Test File | What It Covers |
| --- | --- |
| `test_alert.py` | JavaScript alert dialog handling |
| `test_authentication.py` | Basic HTTP authentication via URL |
| `test_basic_navigation.py` | Page navigation and element lookup (Firefox) |
| `test_browser_dimensions.py` | Window resize, maximize |
| `test_checkboxes.py` | Single and bulk checkbox interaction |
| `test_cookies.py` | Add, retrieve, delete cookies |
| `test_file_upload.py` | File upload via `send_keys` |
| `test_resize_element.py` | Drag-to-resize with ActionChains |
| `test_select.py` | Select by index, value, visible text; deselect |
| `test_stale_element.py` | Retry logic for `StaleElementReferenceException` |

## Running Individual Scripts

Each script in the root of `Selenium-with-Python/` can be run standalone:

```bash
python Selenium_alertAPI.py
python Selenium_AddCookies.py
```

### Environment Variables

Some scripts support configuration via environment variables:

| Variable | Script | Description |
| --- | --- | --- |
| `BASIC_AUTH_USER` | `Selenium_AuthenticationWindows.py` | Username (default: `admin`) |
| `BASIC_AUTH_PASS` | `Selenium_AuthenticationWindows.py` | Password (default: `admin`) |
| `UPLOAD_FILE_PATH` | `Selenium_FileUpload_AutoIt.py` | Absolute path to file for upload |
| `EXCEL_FILE_PATH` | `Selenium_xl.py` | Absolute path to `.xlsx` file |

## Dependencies

| Package | Version | Purpose |
| --- | --- | --- |
| `selenium` | 4.27.1 | WebDriver automation |
| `pytest` | 8.3.4 | Test framework |
| `webdriver-manager` | 4.0.2 | Automatic ChromeDriver/GeckoDriver management |
| `pytest-html` | 4.1.1 | HTML test reports |
| `openpyxl` | 3.1.5 | Excel file reading |
