import time
from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



email = "zainulabideendev@gmail.com"
password = "L@MbD@110funct!0n"
delay = 3
artist = 'strings'
song_delay = 40

driver = webdriver.Chrome()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def hover_and_click(song_name):
    time.sleep(10)
    a = ActionChains(driver)
    hover = driver.find_element(By.XPATH, '//button[@aria-label="'+song_name+'"]')
    a.move_to_element(hover).click().perform()
    time.sleep(song_delay)


def play_music(artist):
    driver.find_element(By.XPATH, '//a[@href="/search"]').click()
    time.sleep(15)
    input_artist = driver.find_element(By.XPATH, '//input[@class="Type__TypeElement-goli3j-0 bWzOVV QO9loc33XC50mMRUCIvf"]')
    ar = artist.replace(' ', '%20')
    input_artist.send_keys(ar)
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[@href="/search/'+ar+'/tracks"]').click()
    time.sleep(10)
    all_songs = driver.find_element(By.XPATH, "//div[@class='ShMHCGsT93epRGdxJp2w Ss6hr6HYpN4wjHJ9GHmi']")
    inner_html = all_songs.get_attribute('innerHTML')
    song_soup = BeautifulSoup(inner_html, 'html.parser')
    all_tags = [tag for tag in song_soup.find_all()]
    for tag in all_tags:
        tag_name = tag.name
        if tag_name == 'button':
            class_name = tag['class']
            if class_name[0] == 'RfidWIoz8FON2WhFoItU':
                aria_name = tag['aria-label']
                hover_and_click(aria_name)
    

def login(e, p, a):
    driver.get("https://open.spotify.com/")
    try:
        btnLogin = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/header/div[4]/div[1]/button[2]/span')))
        btnLogin.click()
        input_user_name = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//input[@id="login-username"]')))
        input_user_pass = driver.find_element(By.XPATH, '//input[@id="login-password"]')
        input_user_name.send_keys(e)
        input_user_pass.send_keys(p)
        driver.find_element(By.XPATH, '//button[@id="login-button"]').click()
        time.sleep(20)
        play_music(a)
    except TimeoutException:
        print("Main Page loading taking too much time!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time.sleep(10)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print(d1)
    my_list = d1.split("/")
    if int(my_list[1]) > 3 and int(my_list[2]) >= 2022:
        print('Error:404 Session Expired')
    else:
        e = input('Gmail: ')
        p = input('Password: ')
        a = input('Singer Name: ')
        login(e, p, a)