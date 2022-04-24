import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://seleniumhub:4444",
        desired_capabilities=DesiredCapabilities.CHROME.copy(),
        options=options,
    )

    search_word = "ちいかわ うさぎ"

    try:
        # 新しいタブを作成する
        driver.execute_script("window.open()")

        # 新しいタブに切り替える
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])

        driver.get("https://www.google.com/")

        wait = WebDriverWait(driver, 10)

        # 検索テキストボックスがレンダリングされるまで待つ
        locator_search_textbox = (By.CSS_SELECTOR, "input[title=検索]")
        wait.until(expected_conditions.visibility_of_element_located(locator_search_textbox))

        # 検索ワードを入力する
        driver.find_element(*locator_search_textbox).clear()
        driver.find_element(*locator_search_textbox).send_keys(search_word)

        # 検索ボタンを押す
        # driver.find_element(By.NAME, "btnK").click() # 上にdivとかが被ってると発動しなかったりする
        driver.execute_script('document.querySelector("input[name=btnK]").click();')

        # 検索結果画面の結果エリアがレンダリングされるまで待つ
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.main")))

        # 検索結果のリンク要素を取得
        links_search_result = driver.find_elements(By.CSS_SELECTOR, "h3.LC20lb")

        # 検索結果のリンクが１つ以上あったら、ランダムにクリックする
        if links_search_result:
            links_search_result[random.randint(0, len(links_search_result)-1)].click()
    finally:
        driver.quit()


main()