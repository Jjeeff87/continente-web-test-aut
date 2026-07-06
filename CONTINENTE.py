from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base_page import BasePage
from helpers import human_pause
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContinenteHomePage(BasePage):
    """Page Object da página inicial do continente.pt (barra de busca).

    TODO: confirmar os seletores reais no site (validar manualmente antes de
    rodar em CI; o site usa banner de cookies e pode pedir loja/morada antes
    de mostrar a busca).
    """

    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"], input#search, input[name="q"]')
    COOKIE_ACCEPT_BUTTON = (
        By.CSS_SELECTOR,
        "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll, "
        "#CybotCookiebotDialogBodyButtonAccept, "
        "#CybotCookiebotDialogBodyLevelButtonAccept"
)

    def reject_cookies_if_present(self):
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)
            )
            button.click()
            human_pause()
        except Exception:
            pass

    def search_for(self, term):
        """Digita o termo de forma humanizada e confirma com Enter."""
        self.type_human(self.SEARCH_INPUT, term)
        self.find(self.SEARCH_INPUT).send_keys(Keys.RETURN)
        human_pause()


class ContinenteSearchResultsPage(BasePage):
    """Page Object da página de resultados de busca."""

    RESULTS_COUNT_TEXT = (By.XPATH, '//*[contains(text(), "resultados") or contains(text(), "produtos")]')
    NO_RESULTS_TEXT = (By.XPATH, '//*[contains(text(), "Sem resultados") or contains(text(), "não encontr")]')
    FIRST_PRODUCT_LINK = (By.XPATH, '(//a[contains(@href, "/produto/") or contains(@class, "product")])[1]')
    FIRST_PRODUCT_ADD_TO_CART_BUTTON = (
        By.XPATH,
        '(//button[contains(., "Adicionar") or contains(@class, "add-to-cart")])[1]',
    )

    def get_results_count_text(self):
        return self.find(self.RESULTS_COUNT_TEXT).text

    def has_no_results_message(self):
        return self.is_visible(self.NO_RESULTS_TEXT)

    def open_first_product(self):
        self.find_clickable(self.FIRST_PRODUCT_LINK).click()
        human_pause()

    def get_first_product_name(self):
        return self.find(self.FIRST_PRODUCT_LINK).text

    def add_first_product_to_cart(self):
        """Adiciona o primeiro produto ao carrinho direto da listagem (sem abrir a página do produto)."""
        self.find_clickable(self.FIRST_PRODUCT_ADD_TO_CART_BUTTON).click()
        human_pause()


class ContinenteProductPage(BasePage):
    """Page Object da página de detalhe de um produto."""

    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
    PRICE = (By.XPATH, '//*[contains(text(), "€")]')
    ADD_TO_CART_BUTTON = (By.XPATH, '(//button[contains(., "Adicionar") or contains(@class, "add-to-cart")])[1]')

    def get_title(self):
        return self.find(self.PRODUCT_TITLE).text

    def is_price_displayed(self):
        return self.is_visible(self.PRICE)

    def add_to_cart(self):
        self.find_clickable(self.ADD_TO_CART_BUTTON).click()
        human_pause()
