import data
import helpers
from CONTINENTE import ContinenteHomePage, ContinenteProductPage, ContinenteSearchResultsPage


class TestContinenteSearch:
    """Testes automatizados da busca de produtos em continente.pt."""

    def setup_method(self):
        if not helpers.is_url_reachable(data.CONTINENTE_URL):
            print("Não foi possível conectar ao site da Continente. Verifique sua conexão.")

        self.driver.get(data.CONTINENTE_URL)
        self.home_page = ContinenteHomePage(self.driver)
        self.home_page.reject_cookies_if_present()

    def test_search_returns_results(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = ContinenteSearchResultsPage(self.driver)
        results_text = results_page.get_results_count_text()

        assert results_text != ""

    def test_search_with_no_results_shows_message(self):
        self.home_page.search_for(data.SEARCH_TERM_NO_RESULTS)

        results_page = ContinenteSearchResultsPage(self.driver)
        assert results_page.has_no_results_message()

    def test_open_first_product_shows_title_and_price(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = ContinenteSearchResultsPage(self.driver)
        results_page.open_first_product()

        product_page = ContinenteProductPage(self.driver)

        assert product_page.get_title() != ""
        assert product_page.is_price_displayed()

    def test_add_first_product_to_cart(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = ContinenteSearchResultsPage(self.driver)
        results_page.open_first_product()

        product_page = ContinenteProductPage(self.driver)
        product_page.add_to_cart()

        # Verificação simples; ajustar depois de confirmar o comportamento
        # exato do carrinho (ex.: contador no header, mini-cart, etc.).
        helpers.human_pause()
