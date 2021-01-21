import time                                 # スリープを使うために必要
from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
 
# サンプルのHTMLを開く
driver.get('https://www.google.com/')       # Googleを開く


 
search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
search.send_keys('hair tonic United States')             # 検索ワードを送信する
search.submit()                             # 検索を実行

def ranking(driver):
    i = 1               # ループ番号、ページ番号を定義
    i_max = 5           # 最大何ページまで分析するかを定義
    title_list = []     # タイトルを格納する空リストを用意
    link_list = []      # URLを格納する空リストを用意
 
    # 現在のページが指定した最大分析ページを超えるまでループする
    while i <= i_max:
        # タイトルとリンクはclass="r"に入っている
        class_group = driver.find_elements_by_class_name('rc')
        # タイトルとリンクを抽出しリストに追加するforループ
        for elem in class_group:
                title_list.append(elem.find_element_by_class_name('LC20lb').text)           #タイトル(class="LC20lb")
                link_list.append(elem.find_element_by_tag_name('a').get_attribute('href'))  #リンク(aタグのhref属性)

 
        # 「次へ」は1つしかないが、あえてelementsで複数検索。空のリストであれば最終ページの意味になる。
        if driver.find_elements_by_id('pnnext') == []:
            i = i_max + 1
        else:
            # 次ページのURLはid="pnnext"のhref属性
            next_page = driver.find_element_by_id('pnnext').get_attribute('href')
            driver.get(next_page)   # 次ページへ遷移する
            i = i + 1               # iを更新
            time.sleep(5)           # 3秒間待機
    return title_list, link_list    # タイトルとリンクのリストを戻り値に指定
 
# ranking関数を実行してタイトルとURLリストを取得する
title, link = ranking(driver)
 
# タイトルリストをテキストに保存
with open('title_.山崎育毛剤.txt', mode='a', encoding='utf-8') as f:
    f.write("\n".join(title))
# URLリストをテキストに保存
with open('link_山崎育毛剤.txt', mode='a', encoding='utf-8') as f:
    f.write("\n".join(link))
 
driver.quit()                               # ブラウザを閉じる