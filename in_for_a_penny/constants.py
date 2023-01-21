
APP_NAME = "In For A Penny"
COPYRIGHT_YEAR = 2023
COPYRIGHT = "Team InForAPenny"

# Namespace related
BASE_APP_NAME = "base"

# Base routes related
HOME_URL = "/"

HOME_ROUTE_NAME = "home"
LANDING_ROUTE_NAME = "landing"

# Admin routes related
ADMIN_URL = "admin/"

# Accounts routes related
ACCOUNTS_URL = "accounts/"

# mounting allauth on 'accounts' and copying paths from
# allauth/account/urls.py
LOGIN_URL = f"{ACCOUNTS_URL}login/"
LOGOUT_URL = f"{ACCOUNTS_URL}logout/"
REGISTER_URL = f"{ACCOUNTS_URL}signup"
# copying route names from allauth/account/urls.py
LOGIN_ROUTE_NAME = "account_login"
LOGOUT_ROUTE_NAME = "account_logout"
REGISTER_ROUTE_NAME = "account_signup"