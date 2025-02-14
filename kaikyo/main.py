import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
from logging import getLogger

logger = getLogger(__name__)

def scrape_products():
    # Chromeドライバのオプション設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    
    # サイトURL (site[0]のURL)
    url = "https://www.mobile-ichiban.com/Prod/2"
    driver.get(url)
    
    time.sleep(3)
    
    # site.jsonのlist XPath要素 "//*[@id=\"dateAndPager\"]/div[2]" で要素を取得
    list_element = driver.find_element(By.XPATH, '//*[@id="dateAndPager"]/div[2]')
    html = list_element.get_attribute("innerHTML")
    
    # BeautifulSoupでHTMLをパース
    soup = BeautifulSoup(html, 'html.parser')
    
    # 商品詳細が格納されているdivのクラスは "col-6 col-md-4 col-lg-3 mb-1"
    product_divs = soup.find_all("div", class_="card-body text-center py-1 px-0")
    
    products = []
    for prod in product_divs:
        # 商品名はcard-body内の最初の<label>タグ（classに"hideText"が含まれる）から取得
        name_label = prod.find("label", class_=re.compile("hideText"))
        name = name_label.get_text(strip=True) if name_label else ""
    
        # 価格は、idが "NewPrice_..." となっている<label>タグから取得
        price_label = prod.find("label", id=re.compile(r"^NewPrice_"))
        price = price_label.get_text(strip=True) if price_label else ""
    
        # 商品の情報を辞書形式で格納
        product = {"name": name, "price": price}
        products.append(product)
    
    driver.quit()
    return products


def main(request):
    """
    引数requestの形式

    Args:
        request: リクエストオブジェクト
            {
                "daily": boolean  # 全商品取得フラグ（必須）
                "query": string   # 検索クエリ（dailyがfalseの場合は必須）
            }
    """
    # リクエストのJSONを取得
    try:
        request_json = request.get_json()
    
        # dailyパラメータの検証
        if not request_json or 'daily' not in request_json:
            return {'error': 'daily parameter is required'}, 400
        daily = request_json['daily']

        # queryパラメータの検証（dailyがfalseの場合）
        if not daily:
            if 'query' not in request_json or not request_json['query']:
                return {'error': 'query parameter is required when daily is false'}, 400
            query = request_json['query']
        else:
            query = None
        logger.info(f"daily: {daily}, query: {query}")
    except:
        return {'error': 'Error during request parsing'}, 400

    '''
    # dailyがtrueの場合、サイト内の全ての商品を取得
    if daily:
        products = scrape_all_products()
    else:
        # dailyがfalseの場合、queryを用いて商品を取得
        products = scrape_product(query)
    '''
    # 今はとりあえずホームに表示される商品のみ取得
    products = scrape_products()
    
    return products

def test(query=None):
    if query is None:
        products = scrape_products()
    else:
        # 検索クエリを用いて商品を取得
        return
    
    return products

#　ローカルでのテスト用
if __name__ == "__main__":
    result = test()
    print(result)