# features/steps/selectors.py

from selenium.webdriver.common.by import By

# ==============================================================================
# LOGIN PAGE
# ==============================================================================
USERNAME_INPUT = (By.NAME, "username")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")

# ==============================================================================
# MENU (Navigation latérale)
# ==============================================================================
ACCOUNTS_OVERVIEW_LINK = (By.LINK_TEXT, "Accounts Overview")
OPEN_NEW_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
BILL_PAY_LINK = (By.LINK_TEXT, "Bill Pay")

# ==============================================================================
# ACCOUNTS OVERVIEW
# ==============================================================================
ACCOUNTS_TITLE = (By.XPATH, "//h1[contains(text(),'Accounts Overview')]")
ACCOUNT_LINKS = (By.XPATH, "//table[@id='accountTable']//a[contains(@href,'activity.htm')]")

# ==============================================================================
# OPEN NEW ACCOUNT
# ==============================================================================
ACCOUNT_TYPE_SELECT = (By.ID, "type")
FROM_ACCOUNT_SELECT = (By.ID, "fromAccountId")
OPEN_ACCOUNT_BUTTON = (By.XPATH, "//input[@value='Open New Account']")
ACCOUNT_CREATED_MSG = (By.XPATH, "//h1[contains(text(),'Account Opened')]")

# ==============================================================================
# BILL PAY
# ==============================================================================
PAYEE_NAME = (By.NAME, "payee.name")
ADDRESS = (By.NAME, "payee.address.street")
CITY = (By.NAME, "payee.address.city")
STATE = (By.NAME, "payee.address.state")
ZIP = (By.NAME, "payee.address.zipCode")
PHONE = (By.NAME, "payee.phoneNumber")
ACCOUNT_NUMBER = (By.NAME, "payee.accountNumber")
VERIFY_ACCOUNT = (By.NAME, "verifyAccount")
AMOUNT = (By.NAME, "amount")
FROM_ACCOUNT_ID = (By.ID, "fromAccountId")
SEND_PAYMENT_BUTTON = (By.XPATH, "//input[@value='Send Payment']")
PAYMENT_COMPLETE_MSG = (By.XPATH, "//h1[contains(text(),'Bill Payment Complete')]")
