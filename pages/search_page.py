from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_placeholder("Search")
        self.search_button = page.locator("//button[@class='btn btn-default btn-lg']")

    def search(self, text: str):
        self.search_input.fill(text)
        self.search_button.click()

    def is_product_present(self, product_name: str) -> bool:
        locator = self.page.locator(f"text={product_name}")
        try:
            return locator.count() > 0
        except Exception:
            return False