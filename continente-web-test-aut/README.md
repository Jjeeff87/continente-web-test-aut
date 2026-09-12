# Continente: Test Automation (continente.pt product search)

Same idea as the other projects in my list (IKEA-WEB_TEST_AUT, Trotiurban,
Shein), now applied to the **product search** flow on the
[continente.pt](https://www.continente.pt/) site, already with a few
improvements I've been carrying over from one project to the next.

## Structure

| File/Folder               | Role                                                                             |
| -------------------------- | --------------------------------------------------------------------------------- |
| `data.py`                  | Site URL and search terms, read from `.env` with a fallback                       |
| `helpers.py`               | Utilities: checking if the site is up, "humanized" typing/pauses, reading `.env`   |
| `common/base_page.py`      | `BasePage` with common operations (find, click, humanized typing)                 |
| `CONTINENTE.py`            | Page Objects: `ContinenteHomePage`, `ContinenteSearchResultsPage`, `ContinenteProductPage` |
| `conftest.py`              | Driver fixture (Chrome) + automatic screenshot on failure                         |
| `TestersiteContinente.py`  | pytest tests                                                                       |
| `.github/workflows/`       | CI: runs the tests on every push/PR                                               |

## What's new compared to the previous baseline (IKEA)

- Driver via **Selenium Manager**, no need to manually download/configure chromedriver.
- `chrome_driver` fixture in `conftest.py` instead of `setup_class`/`teardown_class`.
- Config via `.env` (`python-dotenv`) instead of hardcoded values in `data.py`.
- Shared `BasePage`, reusable across projects (Shein, Continente, IKEA...).
- Automatic screenshot when a test fails (saved to `screenshots/`).
- CI workflow (GitHub Actions) running the suite on every push/PR.

## About the "humanized" typing

Instead of filling the search field instantly, `helpers.human_type` types
character by character with small random pauses, and `helpers.human_pause` adds
short pauses between actions, giving the automation a rhythm that's closer to
a real person interacting with the site.

## Test cases

- Searching for a valid term ("arroz") returns results.
- Searching for a nonexistent term shows a "no results" message.
- Opening the first product in the list shows a title and price.
- Adding the first product to the cart.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env   # adjust CONTINENTE_URL / SEARCH_TERM if needed
```

Requires Chrome installed locally (Selenium Manager handles the driver automatically).

## Running the tests

```bash
pytest -v
```

## Important note

The locators in `CONTINENTE.py` are a starting point (marked with `TODO`). I
couldn't inspect the real DOM via a simple fetch while putting this project
together, and the site may ask for a store/address before allowing search.
**Confirm/adjust the selectors on the live site before running this for real.**

## Publishing to GitHub

```bash
git init
git add .
git commit -m "Product search test automation - continente.pt"
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```
