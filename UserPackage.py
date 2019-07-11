# Enter information below


class UserSettings:
    def __init__(self):
        self.safe_autofill = True
        self.headless = False
        self.pre_start = False
        self.delay = .55


class UserSelection:
    def __init__(self):
        self.keywords = 'Tagless Tees'
        self.style = 'black'


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
