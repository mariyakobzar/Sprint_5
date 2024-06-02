import password
from selenium.webdriver.common.by import By
class TestLocators:

    #кнопка открытия формы регистрации
    SEARCH_REGISTRATION = By.XPATH, '//a[@href="/register"]'
    #заголовок «Вход» в форме авторизации через Личный кабинет
    SEARCH_ENTRANCE = By.XPATH, '//h2[text()="Вход"]'
    #поле ввода имени в форме регистрации
    SEARCH_NAME = By.XPATH, '//input[@name="name"]'
    #поле ввода email в форме регистрации
    SEARCH_EMAIL = By.XPATH, '//form/fieldset[2]/div/div/input'
    #поле ввода пароля в форме регистрации
    SEARCH_PASSWORD = By.XPATH, '//input[@type="password"]'
    #кнопка Зарегистрироваться
    SEARCH_BUTTON_REGISTER = By.XPATH, '//button[text()="Зарегистрироваться"]'

    #заголовок «Вход» в форме авторизации после регистрации
    SEARCH_HEADER_ENTRANCE = By.XPATH, '//h2[text()="Вход"]'
    #поле ввода email
    SEARCH_EMAIL_ENTRANCE = By.XPATH, '//input[@name="name"]'
    #поле ввода пароля
    SEARCH_PASSWORD_ENTRANCE = By.XPATH, '//input[@type="password"]'
    #кнопка «Войти» в форме авторизации после регистрации
    SEARCH_ENTER = By.XPATH, '//button[text()="Войти"]'

    #текст ошибки ввода неверного пароля в форме регистраиции
    SEARCH_INPUT_ERROR = By.XPATH, '//p[@class="input__error text_type_main-default"]'

    #кнопка «Войти в аккаунт» на главной
    SEARCH_ENTER_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]'
    #кнопка «Личный кабинет» на главной
    SEARCH_ACCOUNT = By.XPATH, '//a[@href="/account"]'
    #кнопка «Войти» в форме регистрации
    SEARCH_ENTER_ACCOUNT_FROM_REGISTRATION = By.XPATH, '//a[@href="/login"]'
    #кнопку «Войти» в форме восстановления пароля
    SEARCH_ENTER_ACCOUNT_FROM_FORGOT_PASSWORD = By.XPATH, '//a[@href="/login"]'

    #кнопка восстановления пароля
    SEARCH_BUTTON_FORGOT_PASSWORD = By.XPATH, '//a[@href="/forgot-password"]'
    #заголовок Профиль
    SEARCH_PROFILE = By.XPATH, '//a[@href="/account/profile"]'
    #лого
    SEARCH_LOGO = By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2'
    #заголовок формы Восстановление пароля
    SEARCH_HEADER_PASSWORD_RECOVERY = By.XPATH, '//h2[text()="Восстановление пароля"]'
    #кнопка «Войти» со странице формы Восстановления пароля
    SEARCH_ENTER_FROM_PASSWORD_RECOVERY = By.XPATH, '//a[text()="Войти"]'
    #кнопка конструктор
    SEARCH_CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]'
    #заголовок «Собери бургер»
    SEARCH_HEADER_CONSTRUCTOR = By.XPATH, '//h1[text()="Соберите бургер"]'
    #кнопка «Выход» из личного кабинета
    SEARCH_EXIT_ACCOUNT = By.XPATH, '//button[text()="Выход"]'

    #вкладка «Булки»
    SEARCH_TAB_BREAD = By.XPATH, '//span[text()="Булки"]'
    #вкладка «Соусы»
    SEARCH_TAB_SAUCE = By.XPATH, '//span[text()="Соусы"]'
    #вкладка «Начинки»
    SEARCH_TAB_INGREDIENTS = By.XPATH, '//span[text()="Начинки"]'

    #заголовок «Булки»
    SEARCH_HEADER_BREAD = By.XPATH, '//div/h2[1][@class="text text_type_main-medium mb-6 mt-10"]'
    #заголовок «Соусы»
    SEARCH_HEADER_SAUCE = By.XPATH, '//div/h2[2][@class="text text_type_main-medium mb-6 mt-10"]'
    #заголовок «Начинки»
    SEARCH_HEADER_INGREDIENTS = By.XPATH, '//div/h2[3][@class="text text_type_main-medium mb-6 mt-10"]'