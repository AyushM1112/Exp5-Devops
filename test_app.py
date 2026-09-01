from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_homepage():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://127.0.0.1:5000")

    assert "DevOps Experiment 5" in driver.title
    assert "Welcome to DevOps Experiment 5" in driver.page_source

    driver.quit()