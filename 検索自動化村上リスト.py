# coding: UTF-8
import time                                 # スリープを使うために必要
from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
values=["レグセル株式会社 linkedin ","炎重工株式会社 linkedin ","株式会社ALE linkedin ","株式会社Alivas linkedin ","株式会社DG TAKANO linkedin ","株式会社GRA linkedin ","株式会社ispace linkedin ","株式会社Lily MedTech linkedin ","株式会社Luxonus linkedin ","株式会社P・マインド linkedin ","株式会社Photo electron Soul linkedin ","株式会社QPS研究所 linkedin ","株式会社インフォステラ linkedin ","株式会社サイフューズ linkedin ","株式会社センシンロボティクス linkedin ","株式会社チャレナジー linkedin ","株式会社ファームシップ linkedin ","株式会社ファーメンステーション linkedin ","株式会社ブレイゾン・セラピューティクス linkedin ","株式会社ポーラスター・スペース linkedin ","株式会社マテリアル・コンセプト linkedin ","株式会社ミューラボ linkedin ","株式会社ムスカ linkedin ","株式会社メガカリオン linkedin ","株式会社メタジェン linkedin ","株式会社メトセラ linkedin ","株式会社メルティンMMI linkedin ","株式会社リプロセル linkedin ","株式会社ルートレック・ネットワークス linkedin ","日本環境設計株式会社 linkedin ","THK株式会社 linkedin ","アドバンス理⼯株式会社 linkedin ","エスペック株式会社 linkedin ","オーエスジー株式会社 linkedin ","オプテックス株式会社 linkedin ","カンケンテクノ株式会社 linkedin ","ダイナミックマップ基盤株式会社 linkedin ","ナブテスコ株式会社 linkedin ","ニッポン⾼度紙⼯業株式会社 linkedin ","パウダーテック株式会社 linkedin ","フィガロ技研株式会社 linkedin ","フジクリーン⼯業株式会社 linkedin ","マニー株式会社 linkedin ","マルヤス⼯業株式会社 linkedin ","ユナイテッド・プレシジョン・テクノロジーズ株式会社 linkedin ","レーザーテック株式会社 linkedin ","レオン⾃動機株式会社 linkedin ","旭サナック株式会社 linkedin ","伊東電機株式会社 linkedin ","株式会社Ｃ＆Ａ linkedin ","株式会社industria linkedin ","株式会社JEOL RESONANCE linkedin ","株式会社SCREENグラフィックソリューションズ linkedin ","株式会社アタゴ linkedin ","株式会社イシダ linkedin ","株式会社オーケーエム linkedin ","株式会社グラノプト linkedin ","株式会社コイケ linkedin ","株式会社ジェイテックコーポレーション linkedin ","株式会社ジャムコ linkedin ","株式会社ソディック linkedin ","株式会社ソノテック linkedin ","株式会社ダイドー電⼦ linkedin ","株式会社トヨテック linkedin ","株式会社ナベル linkedin ","株式会社ニッカリ linkedin ","株式会社ニューフレアテクノロジー linkedin ","株式会社パトライト linkedin ","株式会社フルヤ⾦属 linkedin ","株式会社ホリゾン linkedin ","株式会社マキタ linkedin ","株式会社ミツヤ linkedin ","株式会社モリカワ linkedin ","株式会社技研製作所 linkedin ","株式会社志⽔製作所 linkedin ","株式会社昭和真空 linkedin ","株式会社松浦機械製作所 linkedin ","株式会社神崎⾼級⼯機製作所 linkedin ","株式会社電⼦制御国際 linkedin ","株式会社東郷製作所 linkedin ","株式会社武⽥機械 linkedin ","株式会社福井製作所 linkedin ","株式会社流機エンジニアリング linkedin ","株式会社⼤阪チタニウムテクノロジーズ linkedin ","株式会社⼩森コーポレーション linkedin ","株式会社⼭⽥ドビー linkedin ","株式会社⽚岡製作所 linkedin ","株式会社⽩鳳堂 linkedin ","株式会社⽩⼭ linkedin ","株式会社⾣島製作所 linkedin ","関東精機株式会社 linkedin ","京⻄テクノス株式会社 linkedin ","興研株式会社 linkedin ","兼房株式会社 linkedin ","古野電気株式会社 linkedin ","湖北⼯業株式会社 linkedin ","三州産業株式会社 linkedin ","泉鋼業株式会社 linkedin ","太平洋⼯業株式会社 linkedin ","第⼀稀元素化学⼯業株式会社 linkedin ","中興化成⼯業株式会社 linkedin ","朝⽇インテック株式会社 linkedin ","帝國製薬株式会社 linkedin ","東京応化⼯業株式会社 linkedin ","東洋合成⼯業株式会社 linkedin ","藤井精⼯株式会社 linkedin ","萩原⼯業株式会社 linkedin ","牧野フライス精機株式会社 linkedin ","理光フロートテクノロジー株式会社 linkedin ","廣瀬製紙株式会社 linkedin ","碌々産業株式会社 linkedin ","⼆九精密機械⼯業株式会社 linkedin ","⼟肥研磨⼯業株式会社 linkedin ","⼤塚テクノ株式会社 linkedin ","⼤同⼯業株式会社 linkedin ","⼭⼋⻭材⼯業株式会社 linkedin ","⽇華化学株式会社 linkedin ","⽇機装株式会社 linkedin ","⽇伸⼯業株式会社 linkedin ","⽇進⼯具株式会社 linkedin ","⽇精エー・エス・ビー機械株式会社 linkedin ","⽇本分析⼯業株式会社 linkedin ","⽥中科学機器製作株式会社 linkedin ","⽥中貴⾦属⼯業株式会社 linkedin ","⽩⽯⼯業株式会社 linkedin ","⾼砂電気⼯業株式会社 linkedin "]
for j in range(0, len(values)):
# サンプルのHTMLを開く
    driver.get('https://www.google.com/')       # Googleを開く


    
    search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
    search.send_keys(values[j])             # 検索ワードを送信する
    search.submit()                             # 検索を実行

    def ranking(driver):
        i = 1               # ループ番号、ページ番号を定義
        i_max = 1           # 最大何ページまで分析するかを定義
        title_list = []     # タイトルを格納する空リストを用意
        link_list = []      # URLを格納する空リストを用意
    
        # 現在のページが指定した最大分析ページを超えるまでループする
        while i <= i_max:
            # タイトルとリンクはclass="r"に入っている
            class_group = driver.find_elements_by_class_name('tF2Cxc')
            # タイトルとリンクを抽出しリストに追加するforループ
            for elem in class_group:
                    title_list.append(elem.find_element_by_class_name('yuRUbf').text)           #タイトル(class="LC20lb")
                    link_list.append(elem.find_element_by_tag_name('a').get_attribute('href'))  #リンク(aタグのhref属性)

    
            # 「次へ」は1つしかないが、あえてelementsで複数検索。空のリストであれば最終ページの意味になる。
            if driver.find_elements_by_id('pnnext') == []:
                i = i_max + 1
            else:
                # 次ページのURLはid="pnnext"のhref属性
                next_page = driver.find_element_by_id('pnnext').get_attribute('href')
                driver.get(next_page)   # 次ページへ遷移する
                i = i + 1               # iを更新
                time.sleep(10)           # 3秒間待機
        return title_list, link_list    # タイトルとリンクのリストを戻り値に指定
    
    # ranking関数を実行してタイトルとURLリストを取得する
    title, link = ranking(driver)
    
    # タイトルリストをテキストに保存
    with open('title＿.村上.txt', mode='a', encoding='utf-8') as f:
        f.write("\n".join(title))
    # URLリストをテキストに保存
    with open('link__村上.txt', mode='a', encoding='utf-8') as f:
        f.write("\n".join(link))
    
    driver.quit()                            # ブラウザを閉じる