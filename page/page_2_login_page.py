from links.links import Links


class Page2LoginPage:

    url = Links.login_page

    username_field = ('xpath', '//input[@id="username"]')
    password_field = ('xpath', '//input[@id="password"]')
    login_button = ('xpath', '//button[text()="Login"]')



