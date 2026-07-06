from helpers import get_env

CONTINENTE_URL = get_env("CONTINENTE_URL", "https://www.continente.pt/")

# Termos usados na busca de produtos
SEARCH_TERM = get_env("SEARCH_TERM", "arroz")
SEARCH_TERM_NO_RESULTS = "xzzqwnaoexisteprodutoassim"

# Fragmento esperado no nome do produto no topo dos resultados (pode mudar com o tempo/estoque)
EXPECTED_PRODUCT_NAME_FRAGMENT = "arroz"
