# Enter information below


class DriverSettings:
    def __init__(self):
        self.supreme_start_page = "http://www.supremenewyork.com/shop/all/accessories"
        self.supreme_checkout = 'http://www.supremenewyork.com/checkout'
        self.supreme_start_time = '08:00:00.010000'
        self.autofill_url = "https://chrome.google.com/webstore/detail/autofill/nlmmgnhgdeffjkdckmikfpnddkbbfkkk?hl=en"


class UserSettings:
    def __init__(self):
        self.safe_autofill = True
        self.headless = False
        self.pre_start = False
        self.delay = .75
        self.driver_path = "helper_utilities/chromedriver"
        # self.user = "user-data-dir=user"
        self.user = None
        self.headless = False


class UserSelection:
    def __init__(self):
        self.keywords = 'Keychain'
        self.style = ''
        self.size = 'M'


class UserProfile:
    def __init__(self):
        self.name = 'firstname lastname'
        self.email = 'test@botmail.com'
        self.tel = '8082771390'
        self.address = '123 My Address'
        self.apt = '123Z'
        self.zip = '12345'
        self.city = ''
        self.card = '1234567812345678'
        self.month = '12'
        self.year = '2020'
        self.cvv = '123'
        self.safe_autofill = True
