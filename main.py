import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select

data = pd.DataFrame()
links = []
Hotel_Name = []
Overall_rat = []
comment_hotel = []
ratings_hotel = []

class d(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def initials(self):
        city = []
        t = []
        self.driver.get('https://booking.com')
        self.driver.find_element(by=By.CLASS_NAME, value='sb-destination__input').send_keys('Bangkok')
        self.driver.find_element(by=By.CLASS_NAME, value='sb-searchbox__button ').click()
  `      for c in range(0,2000):
            city.append('Bangkok')
        data['City Name'] = city
        #Hotel_name = [None] * 2000
        g= 0
        index = []
        hotel_name = []
        over_rat = []
        lin = []
        i = 0
        while g<3:
            s = []

            name = self.driver.find_elements(by=By.CLASS_NAME, value="a23c043802")
            rat = self.driver.find_elements(by=By.CLASS_NAME, value='d10a6220b4')
            link = self.driver.find_elements(by=By.CLASS_NAME, value="e13098a59f")
            s = self.driver.find_elements(by=By.CLASS_NAME, value='db63693c62')
            #print(len(s), len(name), len(rat))
            for a in range(len(s)):
                hotel_name.append(name[a].text)
                over_rat.append(rat[a].text)
                lin.append(link[a].get_attribute('href'))
                b = s[a].text
                b = b.split()
                #print(b[0])
                if int(b[0].replace(',', '')) > 500:
                    t.append(int(b[0].replace(',', '')))
                    index.append(i)
                i += 1
            self.driver.implicitly_wait(5)
            #print(index)
            self.driver.find_element(by=By.XPATH, value='//*[@id="search_results_table"]/div/div/div/div/div[7]/div[2]/nav/div/div[3]/button')
            g += 1
        index = index[:20]
        for x in index:
            x = int(x)
            a = hotel_name[x]
            for i in range(0,100):
                Hotel_Name.append(a)
                Overall_rat.append(over_rat[x])
            links.append(lin[x])


        data['Hotel Name'] = Hotel_Name
        data['Overall Ratings '] = Overall_rat

    def later(self):
        i = 0
        comments = [None] * 100
        indi_rat = [None] * 100
        l = [None] * 100
        for link in links:
            j = k = 0
            self.driver.get(link)
            self.driver.implicitly_wait(20)
            self.driver.find_element(by=By.ID, value='show_reviews_tab').click()
            self.driver.implicitly_wait(40)
            WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="review_lang_filter"]/button'))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="review_lang_filter"]/div/div/ul/li[2]/button'))).click()
            self.driver.implicitly_wait(30)
            t = Select(self.driver.find_element(by=By.ID, value='review_sort'))
            t.select_by_index(1)
            self.driver.implicitly_wait(20)

            time.sleep(5)
            while True:
                time.sleep(5)
                x = self.driver.find_elements(by=By.CLASS_NAME, value='bui-review-score__badge')
                time.sleep(5)
                l = self.driver.find_elements(by=By.CLASS_NAME, value='c-review__title--ltr')
                for y in l:
                    self.driver.implicitly_wait(20)
                    if j != 100:
                        if y.text != '':
                            comments[j] = y.text
                            j += 1

                for yt in range(len(x)):
                    if k != 100:
                        indi_rat[k] = x[yt].text
                        k += 1
                time.sleep(5)
                self.driver.find_element(by=By.CLASS_NAME, value='pagenext').click()
                time.sleep(5)

                if j == 100:
                    break

            for e in range(len(comments)):
                comment_hotel.append(comments[e])
                ratings_hotel.append(indi_rat[e])
            i += 1
            print(len(comments))
            print(len(indi_rat))
            if i == 20:
                break
        data['Hotel Comments'] = comment_hotel
        data['individual ratings'] = ratings_hotel


s = d()
s.initials()
s.later()
data.to_csv("Hotel_List.csv")
