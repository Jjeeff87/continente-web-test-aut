from helpers import get_env

CONTINENTE_URL = get_env("CONTINENTE_URL", "https://www.continente.pt/")

# Terms used in the product search
SEARCH_TERM = get_env("SEARCH_TERM", "arroz")
SEARCH_TERM_NO_RESULTS = "xzzqwnaoexisteprodutoassim"

# Expected fragment in the top result's product name (may change over time/stock)
EXPECTED_PRODUCT_NAME_FRAGMENT = "arroz"
