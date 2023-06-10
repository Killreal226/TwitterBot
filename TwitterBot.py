from selenium import webdriver  #wire 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
from multiprocessing import Pool
import random
    #--------------------Функция настройки браузера----------
def setting (person_list):
    proxy = person_list [0]
    User_Agent = person_list [4]
        #настройка прокси у браузера
    proxy_options = {'proxy':{'https':f'https://{proxy}'}}
    option = webdriver.ChromeOptions ()
        #Скрытие того, что на сайте бот (для сайта)
    option.add_argument ('--disable-blink-features=AutomationControlled')
        #Скрытие того, что на сайте бот (для хрома)
    option.add_experimental_option ('excludeSwitches', ['enable-automation'])
        #Перемещение работы хрома в фоновый режим
    #option.headless = True
        #Настройка UserAgent
    option.add_argument (f'user-agent={User_Agent}')
        #Отключение уведомлений в хроме
    option.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path='C:\\Python38\chromedriver.exe', options = option) #seleniumwire_options= proxy_options,
    return browser
    #--------------------------------------------------------

    #-----Функция настройки браузера второго поколения-------
def setting_2_generation (person_list):
    User_Agent = person_list [3]
    option = webdriver.ChromeOptions ()
        #Скрытие того, что на сайте бот (для сайта)
    option.add_argument ('--disable-blink-features=AutomationControlled')
        #Скрытие того, что на сайте бот (для хрома)
    option.add_experimental_option ('excludeSwitches', ['enable-automation'])
        #Перемещение работы хрома в фоновый режим
    #option.headless = True
        #Настройка UserAgent
    option.add_argument (f'user-agent={User_Agent}')
        #Отключение уведомлений в хроме
    option.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path='C:\\Python38\chromedriver.exe', options = option) #seleniumwire_options= proxy_options,
    return browser
    #--------------------------------------------------------

    #---------------Функция авторизации в твиттере-----------
def authorization (person_list):
    try:
        login = person_list [1]
        password = person_list [2]
        number = person_list [3]
        numer =  person_list [5]
        browser = setting (person_list)
                #Неявное ожидание
        browser.implicitly_wait(8) #4
        browser.delete_all_cookies()
        browser.get ('https://twitter.com/i/flow/login')
        browser.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys (f'{login}')
        browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//input[@name="password"]').send_keys(f'{password}')
        time.sleep(1)
        browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
        time.sleep (1)
        try:
            browser.find_element (By.XPATH, '//input[@autocomplete="tel"] ').send_keys(f'{number}')
            browser.find_element (By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
        except Exception as d:
            print (d)
        time.sleep (3)
        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\cookies\\cookie{numer}.txt', 'wb') as cook:
            pickle.dump (browser.get_cookies(), cook)
        time.sleep (1)
        try:
            browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div")
        except Exception as e:
            print (e)
        time.sleep (1)
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        try:
            browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        time.sleep (10)
    except Exception as ex:
        time.sleep (150)
        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\cookies\\cookie{numer}.txt', 'wb') as cook:
            pickle.dump (browser.get_cookies(), cook)
        time.sleep (1)
        try:
            browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div")
        except Exception as e:
            print (e)
        time.sleep (1)
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        try:
            browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
            time.sleep (2)
        except Exception as e:
            print(e)
    finally:
        return browser
    #--------------------------------------------------------

    #--Функция авторизации в твиттере аккаунтов 2 поколения--
def authorization_2_generation (person_list):
    try:
        login = person_list [0]
        password = person_list [1]
        mail = person_list [2]
        numer =  person_list [4]
        browser = setting_2_generation (person_list)            
                #Неявное ожидание
        browser.implicitly_wait(4)
        browser.delete_all_cookies()
        browser.get ('https://twitter.com/i/flow/login')
        browser.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys (f'{login}')
        browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//input[@name="password"]').send_keys(f'{password}')
        time.sleep(1)
        browser.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()
        time.sleep (1)
        try:
            browser.find_element (By.XPATH, '//input[@autocomplete="email"] ').send_keys(f'{mail}')
            browser.find_element (By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
        except Exception as d:
            print (d)
        time.sleep (5)
        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\cookies\\cookie{numer}.txt', 'wb') as cook:
            pickle.dump (browser.get_cookies(), cook)
        time.sleep (1)
        try:
            browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div")
        except Exception as e:
            print (e)
        time.sleep (1)
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        try:
            browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
            time.sleep (2)
        except Exception as e:
            print(e)
    finally:
        return browser
    #--------------------------------------------------------

# for i in range (5):
    #        a = browser.find_elements(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1sw30gj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-18kxxzh r-1q142lx r-eu3ka r-5oul0u r-11wrixw r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')
     #       if not (a == []):
      #          browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1sw30gj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-18kxxzh r-1q142lx r-eu3ka r-5oul0u r-11wrixw r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]').click ()
       #         time.sleep(2)
        #        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\cookies\\cookie{numer}.txt', 'wb') as cook:
         #           pickle.dump (browser.get_cookies(), cook)
          #      time.sleep(1)
           #     break
            #else:
             #   time.sleep (120)
              #  browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/span/span').click ()
               # time.sleep (5)
                #continue
            
    #-----------------функция подписки на канал--------------
def subscription (link, browser, proxy):
    try:
        browser.get (f'{link}')
        time.sleep (1)
        browser.refresh ()
        browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()                                                   
        time.sleep (4)
        indicator = 1
        return indicator
    except Exception as ex:
        v = browser.find_elements(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')
        if not (v == []):
            browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click ()
            time.sleep (2)
        browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()                                                   
        time.sleep (4)
        final (proxy)
        indicator = 0
        print (ex)
        return indicator
        #//div[@class="css-1dbjc4n r-6gpygo"] - xpath старый follow
    #--------------------------------------------------------
    
    #-------------функция подписки на инфлюинсеров-----------
def subscription_infl (link, browser, proxy):
    try:
        browser.get (f'{link}')
        time.sleep (1)
        browser.refresh ()
        browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()                                                   
        time.sleep (3)
        indicator = 1
        return indicator
    except Exception as ex:
        try:
            time.sleep (1)
            try:
                browser.find_element(By.XPATH,'//div[@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (1)
            except Exception as e:
                browser.refresh ()
                time.sleep (3)
            browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()
            return indicator
        except Exception:
            time.sleep (4)
            final (proxy)
            indicator = 0
            print (ex)
            return indicator
    #--------------------------------------------------------
        
    #-------функция подписки на аккаунты 1го поколения-------
def subscription_on_1_generation (link, browser):
    try:
        browser.get (f'{link}')
        time.sleep (1)
        browser.refresh ()
        time.sleep (3)
        browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()                                                   
        time.sleep (3)
    except Exception as ex:
        try:
            time.sleep (1)
            try:
                browser.find_element(By.XPATH,'//div[@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (1)
            except Exception as e:
                time.sleep (120)
                browser.refresh ()
                time.sleep (3)
            browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()
        except Exception:
            time.sleep (1)
            print (ex)
    #--------------------------------------------------------

    #-------функция подписки на аккаунты 2го поколения-------
def subscription_on_2_generation (link, browser):
    try:
        browser.get (f'{link}')
        time.sleep (1)
        browser.refresh ()
        time.sleep (1)
        browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()                                                   
        time.sleep (3)
    except Exception as ex:
        try:
            try:
                a = browser.find_element (By.XPATH, '//a[@href="/settings/profile"]')
            except Exception as e:
                browser.refresh ()
                time.sleep (3)
            browser.find_element(By.XPATH, '//div[@data-testid="placementTracking"]').click()
        except Exception:
            time.sleep (1)
            print (ex)
    #--------------------------------------------------------

    #-------------------------Лайк---------------------------
def like (link, browser, proxy):
    try:
        browser.get (f'{link}')
        time.sleep (1)
        browser.find_element(By.XPATH, '//div[@data-testid="like"]').click()                             
        time.sleep (1)
        indicator = 1
        return indicator
    except Exception as ex:
        time.sleep (1)
        browser.refresh ()
        time.sleep (3)
        try:
            browser.find_element(By.XPATH, '//div[@data-testid="like"]').click()
            time.sleep (1)
            indicator = 1
            return indicator
        except Exception:
            final (proxy)
            indicator = 0
            print (ex)
            return indicator
    #------------------------------------------------------

    #-------Авторизация в твиттере с помощью куки----------
def authorization_cookie (person_list):
    try:
        numer =  person_list [5]
        browser = setting (person_list)
                #Неявное ожидание
        browser.implicitly_wait(6)
        browser.get ('https://twitter.com')
        time.sleep (1)
        browser.delete_all_cookies()
        time.sleep (1)
        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\cookies\\cookie{numer}.txt', 'rb') as cook:
            for cookie in pickle.load (cook):
                browser.add_cookie(cookie)
        time.sleep (2)
        browser.refresh ()
        time.sleep (2)
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        return browser
    except Exception as ex:
        for i in range (5):
            v = browser.find_elements(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')
            w = browser.find_elements(By.XPATH, '//input[@type="submit"]')
            if not (v == []):
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (3)
            elif not (w == []):
                browser.find_element(By.XPATH, '//input[@type="submit"]').click ()
                time.sleep (3)
            else:
                browser.refresh ()
                break
        time.sleep(2)
        return browser
    #------------------------------------------------------

    #--Авторизация с помощью куки аккаунтов 2го поколения--
def  authorization_cookie_on_2_generation (person_list):
    try:
        numer =  person_list [4]
        browser = setting_2_generation (person_list)
                #Неявное ожидание
        browser.implicitly_wait(10)
        browser.get ('https://twitter.com')
        time.sleep (1)
        browser.delete_all_cookies()
        time.sleep (1)
        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\cookies\\cookie{numer}.txt', 'rb') as cook:
            for cookie in pickle.load (cook):
                browser.add_cookie(cookie)
        time.sleep (5)
        browser.refresh ()
        time.sleep (2)
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        return browser
    except Exception as ex:
        time.sleep (180)
        for i in range (5):
            v = browser.find_elements(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')
            w = browser.find_elements(By.XPATH, '//input[@type="submit"]')
            if not (v == []):
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (3)
            elif not (w == []):
                browser.find_element(By.XPATH, '//input[@type="submit"]').click ()
                time.sleep (3)
            else:
                browser.refresh ()
                break
        time.sleep(2)
        return browser
    #------------------------------------------------------

    #-Функция котора просто авторизуетс для раоты "руками"-
def authorization_cookie_examination (person_list):
    try:
        numer =  person_list [5]
        browser = setting (person_list)
                #Неявное ожидание
        browser.implicitly_wait(10)
        browser.get ('https://twitter.com')
        time.sleep (1)
        browser.delete_all_cookies()
        time.sleep (1)
        with open (f'C:\\Users\\79775\\Desktop\\bots\\twitter\\cookies\\cookie{numer}.txt', 'rb') as cook:
            for cookie in pickle.load (cook):
                browser.add_cookie(cookie)
        time.sleep (2)
        browser.refresh ()
        time.sleep (3)
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span').click()
            time.sleep (2)
        except Exception as e:
            print(e)
        time.sleep (7)
    except Exception as ex:
        for i in range (5):
            v = browser.find_elements(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')
            w = browser.find_elements(By.XPATH, '//input[@type="submit"]')
            if not (v == []):
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-1mnahxq r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (3)
            elif not (w == []):
                browser.find_element(By.XPATH, '//input[@type="submit"]').click ()
                time.sleep (3)
            else:
                browser.refresh ()
                break
        time.sleep(2)
    #------------------------------------------------------
 
    #----------------------Ретвит--------------------------
def retweet (browser, proxy):
    try:
        browser.find_element(By.XPATH, '//div[@data-testid="retweet"]').click()
        browser.find_element(By.XPATH, '//div[@data-testid="retweetConfirm"]').click()
        time.sleep (1)
        indicator = 1
        return indicator
    except Exception as ex:
        time.sleep (10)
        final (proxy)
        indicator = 0
        print (ex)
        return indicator
     #------------------------------------------------------

    #---теганье трех друзей и написание сообщения в теге---
def teg (tegs, browser, proxy):
    k = 0
    time.sleep (2)
    browser.find_element(By.XPATH, '//div[@data-testid="reply"]').click()
    for i in range (5):
        try:
            browser.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]').click()
            browser.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]').send_keys (f'{tegs}')
            browser.find_element(By.XPATH, '//div[@data-testid="tweetButton"]').click()
            time.sleep (2)
            indicator = 1
            return indicator
            break
        except Exception as ex:
            browser.refresh ()
            time.sleep (3)
            k +=1
            continue
    if k == 4:   
        final (proxy)
        indicator = 0
        print (ex)
        return indicator
    #------------------------------------------------------

    #--------выкладывание своего твита без картинки--------
def tweet_only_phrase (person_list):
    try:
        for i in range (5):
            try:
                phrase = person_list [6]
                browser = authorization_cookie (person_list)  
                browser.find_element(By.XPATH, '//*[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys (f'{phrase}')
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (5)
                break
            except Exception as ex:
                time.sleep (1)
                try:
                    browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1niwhzg r-1ets6dv r-sdzlij r-1phboty r-rs99b7 r-1ydw1k6 r-1r5su4o r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
                    time.sleep (2)
                except Exception as a:
                    print ('ошибка')
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (10)
                break
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------
        
    #---------выкладывание своего твита скартинкой---------
def tweet_pool(person_list):
    try:
        for i in range (5):
            try:
                phrase = person_list [6]
                numer =  person_list [5]
                browser = authorization_cookie (person_list)
                browser.find_element(By.XPATH, '//*[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys (f'{phrase}')
                browser.find_element(By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"]').send_keys(f'C:\\Users\\79775\\Desktop\\bots\\twitter\\img_tweet\\{numer}.jpg')
                time.sleep(1)
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (10)
                break
            except Exception as ex:
                time.sleep (1)
                try:
                    browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-1niwhzg r-1ets6dv r-sdzlij r-1phboty r-rs99b7 r-1ydw1k6 r-1r5su4o r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]').click()
                    time.sleep (2)
                except Exception as a:
                    print ('ошибка')
                browser.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]').click ()
                time.sleep (10)
                break
    finally:
        browser.close ()
        browser.quit ()
    #-------------------------------------------------------
    
    #------------------Настройка аватарки-------------------
def avatar (person_list):
    try:
        numer =  person_list [5]
        login = person_list [1]
        browser = authorization (person_list)
        browser.find_element (By.XPATH, f'//a[@href="/{login}"]').click ()
        browser.find_element (By.XPATH, '//a[@href="/i/flow/setup_profile"]').click ()
        time.sleep (1)
        browser.find_element(By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp"]').send_keys(f'C:\\Users\\79775\\Desktop\\bots\\twitter\\avatar\\{numer}.jpg')
        browser.find_element(By.XPATH, '//div[@data-testid="applyButton"]').click ()
        browser.find_element(By.XPATH, '//div[@data-testid="ocfSelectAvatarNextButton"]').click()                          
        time.sleep (10)
    except Exception as ex:
        time.sleep (150)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/span/span').click()
        browser.find_element (By.XPATH, f'//a[@href="/{login}"]').click ()
        browser.find_element (By.XPATH, '//a[@href="/i/flow/setup_profile"]').click ()
        browser.find_element(By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp"]').send_keys(f'C:\\Users\\79775\\Desktop\\bots\\twitter\\avatar\\{numer}.jpg')
        browser.find_element(By.XPATH, '//div[@data-testid="applyButton"]').click ()
        browser.find_element(By.XPATH, '//div[@data-testid="ocfSelectAvatarNextButton"]').click()                             
        time.sleep (10)
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------

    #--------Настройка аватарки второго поколения----------
def avatar_2_generation (person_list):
    try:
        numer =  person_list [4]
        login = person_list [0]
        browser = authorization_2_generation (person_list)                       
        browser.find_element (By.XPATH, f'//a[@href="/{login}"]').click ()
        browser.find_element (By.XPATH, '//a[@href="/i/flow/setup_profile"]').click ()
        time.sleep (1)
        browser.find_element(By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp"]').send_keys(f'C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\avatar\\{numer}.jpg')
        browser.find_element(By.XPATH, '//div[@data-testid="applyButton"]').click ()
        browser.find_element(By.XPATH, '//div[@data-testid="ocfSelectAvatarNextButton"]').click()                          
        time.sleep (10)
    except Exception as ex:
        time.sleep (150)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/span/span').click()
        browser.find_element (By.XPATH, f'//a[@href="/{login}"]').click ()
        browser.find_element (By.XPATH, '//a[@href="/i/flow/setup_profile"]').click ()
        browser.find_element(By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp"]').send_keys(f'C:\\Users\\79775\\Desktop\\bots\\twitter\\avatar\\{numer}.jpg')
        browser.find_element(By.XPATH, '//div[@data-testid="applyButton"]').click ()
        browser.find_element(By.XPATH, '//div[@data-testid="ocfSelectAvatarNextButton"]').click()                             
        time.sleep (10)
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------
        
    #-----------функция просто подписки на проект----------
def only_subscription (person_list):
    try:
        proxy = person_list [0]
        list_links = person_list [6]
        list_individual = []
        browser = authorization_cookie (person_list)
        for i in list_links:
            while True:
                random_index = random.randint (0,len(list_links)-1)
                if random_index in list_individual:
                    continue
                else:
                    list_individual += [random_index]
                    link = list_links [random_index]
                    break
                
            indicator = subscription (link, browser, proxy)
            if indicator == 1:
                time.sleep (3)
            else:
                print ('ошибка')
    except Exception as ex:
        print (ex)
    #finally:
        #browser.close ()
        #browser.quit ()
    #------------------------------------------------------
        
    #-----функция запуска абуза giveaway без подписки------
def Giveaway_not_subscription (person_list):
    try:
        proxy = person_list [0]
        list_links = person_list [6]
        tegs = person_list [7]
        list_individual = []
        browser = authorization_cookie (person_list)
        for i in list_links:
            while True:
                random_index = random.randint (0,len(list_links)-1)
                if random_index in list_individual:
                    continue
                else:
                    list_individual += [random_index]
                    link = list_links [random_index]
                    break
                
            indicator1 = like (link, browser, proxy)
            if indicator1 == 1:
                indicator2 = retweet (browser, proxy)
                if indicator2 == 1:
                    indicator3 = teg(tegs, browser, proxy)
                    if indicator3 == 1:
                        time.sleep (1)
                    else:
                        print ('ошибка')
                else:
                    print ('ошибка')
            else:
                print ('ошибка')
            time.sleep (4)
    except Exception as ex:
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------
        
    #-----функция запуска абуза giveaway с подпиской------
def Giveaway_with_subscription (person_list):
    try:
        proxy = person_list [0]
        list_links_giveaway = person_list [6]
        tegs = person_list [7]
        list_links_project = person_list [8]
        browser = authorization_cookie (person_list)
        list_individual = []
        for i in list_links_giveaway:
            while True:
                random_index = random.randint (0,len(list_links_giveaway)-1)
                if random_index in list_individual:
                    continue
                else:
                    list_individual += [random_index]
                    link_giveaway = list_links_giveaway [random_index]
                    link_project = list_links_project [random_index]
                    break
                
            indicator1 = subscription (link_project, browser, proxy)
            if indicator1 == 1:
                indicator2 = like (link_giveaway, browser, proxy)
                if indicator2 == 1:
                    indicator3 = retweet (browser, proxy)
                    if indicator3 == 1:
                        indicator4 = teg(tegs, browser, proxy)
                        if indicator4 == 1:
                            time.sleep (2)
                        else:
                            print ('ошибка')
                    else:
                        print ('ошибка')
                else:
                   print ('ошибка')
            else:
                print ('ошибка')
    except Exception as ex:
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------

    #----------------Подписка на инфлюинсеров--------------
def subscription_fonds (person_list):
    try:
        proxy = person_list [0]
        amount_infl = person_list [6]
        list_crypto_fonds = person_list [7]
        browser = authorization_cookie (person_list)
        list_individual = []
        for i in range (amount_infl):
            while True:
                random_index = random.randint (0,len(list_crypto_fonds)-1)
                if random_index in list_individual:
                    continue
                else:
                    list_individual += [random_index]
                    link = list_crypto_fonds [random_index]
                    break

            indicator = subscription_infl (link, browser, proxy)
            if indicator == 1:
                time.sleep (3)
            else:
                print ('ошибка')
    except Exception as ex:
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------

    #-----------Подписка на аккаунты 1го поколения---------
def subscription_accounts_1_generation (person_list):
    try:
        amount_links = person_list [5]
        list_links_1_generation = person_list [6]
        browser = authorization_cookie_on_2_generation (person_list)     
        list_individual = []
        for i in range (amount_links):
            while True:  
                random_index = random.randint (0,len(list_links_1_generation)-1)                
                if random_index in list_individual:
                    continue
                else:
                    list_individual += [random_index]
                    link = list_links_1_generation [random_index]
                    break

            subscription_on_1_generation (link, browser)
    except Exception as ex:
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------

    #-----------Подписка на аккаунты 2го поколения---------
def subscription_accounts_2_generation (person_list):
    try:
        amount_links = person_list [5]
        list_links_2_generation = person_list [6]
        browser = authorization_cookie_on_2_generation (person_list)     
        for i in range (amount_links):
            link = list_links_2_generation [i]
            subscription_on_2_generation (link, browser)
    except Exception as ex:
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------

    #---Подписка на свои новые аккаунты со своих старых----
def subscription_on_new_account (person_list):
    try:
        proxy = person_list [0]
        list_link = person_list [6]
        amount_accounts = random.randint(1, len (list_link))
        browser = authorization_cookie (person_list)
        for i in range (amount_accounts):
            indicator  = subscription_infl (list_link[i], browser, proxy)
            if indicator == 1:
                time.sleep (3)
            else:
                print ('ошибка')
    except Exception as ex:
        print (ex)
    finally:
        browser.close ()
        browser.quit ()
    #------------------------------------------------------
        
    #-Фун.,открывающая нью файлы и передающая их в списки--
def files_lists_new(N):
        #Список прокси
    proxy = open ('proxy_new.txt', 'r')
    list_proxy_dirty = proxy.readlines ()
    list_proxy = []
    for i in list_proxy_dirty:
        proxy_clean = i.replace('\n', '')
        list_proxy += [proxy_clean]
    del list_proxy[N:len(list_proxy)]
    proxy.close ()
        #Списки логина, пароля, телефона
    login_password = open ('login_password_new.txt', 'r')
    list_login_password_number_dirty = login_password.readlines ()
    list_login_password_number = []
    for i in list_login_password_number_dirty :
        a_clean = i.replace('\n', '')
        list_login_password_number += [a_clean]
    list_data = []
    list_login = []
    list_password = []
    list_number = []
    for i in list_login_password_number:
        list_data = i.split('/')
        list_login += [list_data [0]]
        list_password +=  [list_data [1]]
        list_number += [list_data [2]]
        list_data = []
    del list_login [N:len(list_login)]
    del list_password [N:len(list_password)]
    del list_number  [N: len(list_number)]
    login_password.close ()
        #Список User-Agent
    User_Agent = open ('User-Agents_new.txt', 'r')
    list_User_Agent_dirty = User_Agent.readlines ()
    list_User_Agent =[]
    for i in list_User_Agent_dirty:
        User_clean = i.replace('\n', '')
        list_User_Agent += [User_clean]
    del list_User_Agent [N:len(list_User_Agent)]
    User_Agent.close ()
    return list_proxy, list_login, list_password, list_number, list_User_Agent
    #------------------------------------------------------

    #-открывает нью файлы 2го поколения и передает в list--
def files_lists_new_2_generation(N):
        #Списки логина, пароля, телефона
    login_password = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\login_password_new.txt', 'r')
    list_login_password_mail_dirty = login_password.readlines ()
    list_login_password_mail = []
    for i in list_login_password_mail_dirty :
        a_clean = i.replace('\n', '')
        list_login_password_mail += [a_clean]
    list_data = []
    list_login = []
    list_password = []
    list_mail = []
    for i in list_login_password_mail:
        list_data = i.split(':')
        list_login += [list_data [0]]
        list_password +=  [list_data [1]]
        list_mail += [list_data [2]]
        list_data = []
    del list_login [N:len(list_login)]
    del list_password [N:len(list_password)]
    del list_mail  [N: len(list_mail)]
    login_password.close ()
        #Список User-Agent
    User_Agent = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\User-Agents_new.txt', 'r')
    list_User_Agent_dirty = User_Agent.readlines ()
    list_User_Agent =[]
    for i in list_User_Agent_dirty:
        User_clean = i.replace('\n', '')
        list_User_Agent += [User_clean]
    del list_User_Agent [N:len(list_User_Agent)]
    User_Agent.close ()
    return list_login, list_password, list_mail, list_User_Agent
    #------------------------------------------------------

    #--Функция,открывающая файлы и передающая их в списки--
def files_lists(N,index_first):
        #Список прокси
    proxy = open ('proxy.txt', 'r')
    list_proxy_dirty = proxy.readlines ()
    del list_proxy_dirty [0:index_first-1]
    list_proxy = []
    for i in list_proxy_dirty:
        proxy_clean = i.replace('\n', '')
        list_proxy += [proxy_clean]
    del list_proxy[N:len(list_proxy)]
    proxy.close ()
        #Списки логина, пароля, телефона
    login_password = open ('login_password.txt', 'r')
    list_login_password_number_dirty = login_password.readlines ()
    del list_login_password_number_dirty [0:index_first-1]
    list_login_password_number = []
    for i in list_login_password_number_dirty :
        a_clean = i.replace('\n', '')
        list_login_password_number += [a_clean]
    list_data = []
    list_login = []
    list_password = []
    list_number = []
    for i in list_login_password_number:
        list_data = i.split('/')
        list_login += [list_data [0]]
        list_password +=  [list_data [1]]
        list_number += [list_data [2]]
        list_data = []
    del list_login [N:len(list_login)]
    del list_password [N:len(list_password)]
    del list_number  [N: len(list_number)]
    login_password.close ()
        #Список User-Agent
    User_Agent = open ('User-Agents.txt', 'r')
    list_User_Agent_dirty = User_Agent.readlines ()
    del list_User_Agent_dirty [0:index_first-1]
    list_User_Agent =[]
    for i in list_User_Agent_dirty:
        User_clean = i.replace('\n', '')
        list_User_Agent += [User_clean]
    del list_User_Agent [N:len(list_User_Agent)]
    User_Agent.close ()
    return list_proxy, list_login, list_password, list_number, list_User_Agent
    #------------------------------------------------------

    #--открывает файлы 2го поколения и передает в списки---
def files_lists_2_generation(N,index_first):
        #Списки логина, пароля, почты
    login_password = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\login_password.txt', 'r')
    list_login_password_mail_dirty = login_password.readlines ()
    del list_login_password_mail_dirty [0:index_first-1]
    list_login_password_mail = []
    for i in list_login_password_mail_dirty :
        a_clean = i.replace('\n', '')
        list_login_password_mail += [a_clean]
    list_data = []
    list_login = []
    list_password = []
    list_mail = []
    for i in list_login_password_mail:
        list_data = i.split(':')
        list_login += [list_data [0]]
        list_password +=  [list_data [1]]
        list_mail += [list_data [2]]
        list_data = []
    del list_login [N:len(list_login)]
    del list_password [N:len(list_password)]
    del list_mail  [N: len(list_mail)]
    login_password.close ()
        #Список User-Agent
    User_Agent = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\User-Agents.txt', 'r')
    list_User_Agent_dirty = User_Agent.readlines ()
    del list_User_Agent_dirty [0:index_first-1]
    list_User_Agent =[]
    for i in list_User_Agent_dirty:
        User_clean = i.replace('\n', '')
        list_User_Agent += [User_clean]
    del list_User_Agent [N:len(list_User_Agent)]
    User_Agent.close ()
    return list_login, list_password, list_mail, list_User_Agent
    #------------------------------------------------------

    #-функц. делающ список ссылок из файла новых аккаунтов-
def list_new_link ():
    new_link = open ('login_password_new.txt', 'r')
    list_account = new_link.readlines ()
    list_login = []
    list_data = []
    for i in list_account:
        list_data = i.split ('/')
        list_login += [list_data[0]]
        list_data = []                                                                      
    list_link = []
    for i in list_login:
        a = 'https://twitter.com/' + i
        list_link += [a]
    new_link.close ()
    return list_link     
    #------------------------------------------------------

    #-------Функция дозаписи в файлы новых элементов-------
def record():
    proxy_new = open ('proxy_new.txt', 'r')
    list_proxy_dirty = proxy_new.readlines ()
    proxy = open ('proxy.txt', 'a')
    for i in list_proxy_dirty:
        proxy.write (i)
    proxy.close ()
    proxy_new.close()
    login_password_new = open ('login_password_new.txt', 'r')
    list_login_password_number_dirty = login_password_new.readlines ()
    login_password = open ('login_password.txt', 'a')
    for i in list_login_password_number_dirty:
        login_password.write (i)
    login_password.close ()
    login_password_new.close()
    User_Agent_new = open ('User-Agents_new.txt', 'r')
    list_User_Agent_dirty = User_Agent_new.readlines ()
    User_Agent = open ('User-Agents.txt', 'a')
    for i in list_User_Agent_dirty:
        User_Agent.write (i)
    User_Agent.close ()
    User_Agent_new.close()
    #------------------------------------------------------

    #--Функция дозаписи в файлы новых элементов(2 покол.)--
def record_2_generation():
    login_password_new = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\login_password_new.txt', 'r')
    list_login_password_mail_dirty = login_password_new.readlines ()
    login_password = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\login_password.txt', 'a')
    for i in list_login_password_mail_dirty:
        login_password.write (i)
    login_password.close ()
    login_password_new.close()
    User_Agent_new = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\User-Agents_new.txt', 'r')
    list_User_Agent_dirty = User_Agent_new.readlines ()
    User_Agent = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\User-Agents.txt', 'a')
    for i in list_User_Agent_dirty:
        User_Agent.write (i)
    User_Agent.close ()
    User_Agent_new.close()
    #------------------------------------------------------

    #-Фун., открывающая файл с друзьями и перевод в списки-
def file_tegs (N, index_first):
    tegs = open ('tegs.txt', 'r')
    list_tegs_dirty = tegs.readlines ()
    del list_tegs_dirty [0:index_first-1]
    list_tegs = []
    for i in list_tegs_dirty:
        teg_clean = i.replace('\n', '')
        list_tegs += [teg_clean]
    del list_tegs[N:len(list_tegs)]
    tegs.close ()
    return list_tegs
    #------------------------------------------------------

    #--фун., открывает файл с инфлюинс. и перевод в list---
def file_crypto_fonds ():
    crypto_fonds = open ('crypto_fonds.txt', 'r')
    crypto_fonds_dirty = crypto_fonds.readlines ()
    list_crypto_fonds = []
    for i in crypto_fonds_dirty:
        link_clean = i.replace ('\n', '')
        list_crypto_fonds += [link_clean]
    crypto_fonds.close()
    return list_crypto_fonds
    #------------------------------------------------------

   #--фун., открывает файл с 1м поколен и перевод в list---
def file_accounts_1_generation():
    accounts_1_generation = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\accounts.txt', 'r')
    accounts_1_generation_dirty = accounts_1_generation.readlines ()
    list_links_1_generation = []
    list_data = []
    for i in accounts_1_generation_dirty:
        account = i.replace ('\n', '')
        list_data = account.split ('/')
        login = list_data[0]
        a = 'https://twitter.com/' + login
        list_links_1_generation += [a]
    accounts_1_generation.close()
    return list_links_1_generation
    #------------------------------------------------------

   #--фун., открывает файл с 2м поколен и перевод в list---
def file_accounts_2_generation():
    accounts_2_generation = open ('C:\\Users\\79775\\Desktop\\bots\\twitter\\second generation\\login_password.txt', 'r')
    accounts_2_generation_dirty = accounts_2_generation.readlines ()
    list_links_2_generation = []
    list_data = []
    for i in accounts_2_generation_dirty:
        account = i.replace ('\n', '')
        list_data = account.split (':')
        login = list_data[0]
        a = 'https://twitter.com/' + login
        list_links_2_generation += [a]
    accounts_2_generation.close()
    return list_links_2_generation
    #------------------------------------------------------ 

    #------функция изменения прокси в случаи ошибки--------
def final (proxy):
    r = open ('proxy.txt', 'r')
    list_proxy = r.readlines ()
    for i in range (len(list_proxy)):
        if proxy in list_proxy[i]:
            new_proxy = '*' + proxy + '\n'
            list_proxy[i] = new_proxy
    r.close ()
    r = open ('proxy.txt', 'w')
    for i in list_proxy:
        r.write (i)
    r.close ()
    #------------------------------------------------------

    #--функция,проверяющая прокси и запускающие пуск ф-ии--
def Check_tweet_only_phrase (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        tweet_only_phrase (person_list)
    else:
        tweet_only_phrase (person_list)

def Check_tweet_pool (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        tweet_pool (person_list)
    else:
        tweet_pool (person_list)
 
def Check_only_subscription (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        only_subscription (person_list)
    else:
        only_subscription (person_list)

def Check_Giveaway_not_subscription (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        Giveaway_not_subscription (person_list)
    else:
        Giveaway_not_subscription (person_list)

def Check_Giveaway_with_subscription (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        Giveaway_with_subscription (person_list)
    else:
        Giveaway_with_subscription (person_list)


def Check_subscription_fonds (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        subscription_fonds (person_list)
    else:
        subscription_fonds (person_list)

def Check_subscription_on_new_account (person_list):
    proxy = person_list [0]
    if '**' in proxy:
        print ('skip')
    elif '*' in proxy:
        proxy_clean = proxy.replace ('*','')
        person_list [0] = proxy_clean
        subscription_on_new_account (person_list)
    else:
        subscription_on_new_account (person_list)
    #------------------------------------------------------

    
if __name__ == '__main__':
    print('Итак, ты попал в самого охренительного бота. Выбери, что тебе нужно:\n'
         '1)У меня новые аккаунты твиттера, надо их настроить (Куки и аватарку поставить)\n'
         '2)Мне нужно что нибудь твитнуть c аккаунтов, чтобы не думали, что я бот\n'
         '3)Мне бы просто подписаться всей своей сворой на один канал\n'
         '4)Мне надо пройти Giveaway (Тоесть лайк, ритвит, тегнуть)\n'
         '5)Надо определенным количством аккаунтов подписаться на всяких инфлюенсеров\n',
         '6)Просто надо зайти на один из аккаунтов и что то там проверить\n'
         '7)Мне надо своими аккаунтами подписаться на новые аккаунты (а то они совсем пустые)\n'
         '8)Надо вторым поколением подписаться на свои аккаунты\n')

    answer = input()
    #-------------------------------------------------------
    if answer == '1':
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists_new(N)
        list_lord = []
        numer_old = int (input ('Можешь пж еще зайти в файл куки и сказать номер последнеко кука?\n'))
        for i in range (N):
            list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], numer_old+1]]
            numer_old +=1
        processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
        p = Pool (processes=processes)
        p.map (avatar, list_lord)
        answer2 = input ('Ну вроде как все, заходи в файл куки, проверяй все ли на месте, если да, то нажми 1, если нет... Поговорим об этом позже\n')
        if answer2 == '1':
            record()
            print ('Все перезаписал')
    #--------------------------------------------------------
    if answer == '2':
        index_first = int (input('Начиная с какого по счету аккаунта загонять?\n'))
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists(N,index_first)
        list_lord = []
        answer2 = input ('Ты просто хочешь твитнуть какую нибудь фразу или фразу с картинкой?\n'
                         '1)Хочу твитнуть фразы из файла\n'
                         '2)Хочу твитнуть фразы и с файла и картинками\n')
        phrases = open ('phrases.txt', 'r', encoding = 'utf-8')
        list_phrases_dirty = phrases.readlines ()
        del list_phrases_dirty [0:index_first-1]
        list_phrases = []
        for i in list_phrases_dirty:
            phrases_clean = i.replace('\n', '')
            list_phrases += [phrases_clean]
        del list_phrases[N:len(list_phrases)]
        phrases.close ()
        index_first -= 1 
        processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
        if answer2 == '1':
            for i in range (N):
                list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, list_phrases[i]]]
                index_first += 1
            p = Pool (processes=processes)
            p.map (Check_tweet_only_phrase, list_lord)
        if answer2 == '2':
            for i in range (N):
                list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, list_phrases[i]]]
                index_first += 1
            p = Pool (processes=processes)
            p.map (Check_tweet_pool, list_lord)
    #---------------------------------------------------------
    if answer == '3':
        index_first = int (input('Начиная с какого по счету аккаунта загонять?\n'))
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists(N, index_first)
        list_lord = []
        amount_links = int(input ('Сколько ссылок будет?\n'))
        list_links = []
        print ('Вводи ссылку и нажимай Enter')
        for i in range (amount_links):
            link = input ()
            list_links += [link]
        index_first -= 1
        for i in range (N):
            list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, list_links]]
            index_first += 1
        processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
        p = Pool (processes=processes)
        p.map (Check_only_subscription, list_lord)
    #---------------------------------------------------------
    if answer == '4':
        index_first = int (input('Начиная с какого по счету аккаунта загонять?\n'))
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists(N,index_first)
        list_tegs = file_tegs (N,index_first)
        list_lord = []
        index_first -= 1
        answer2 = input ('У тебя уже есть подписка на проект у этих аккаунтов?\n'
                         '1)Да\n'
                         '2)Нет\n')
        if answer2 == '1':
            amount_links = int (input ('Сколько ссылок будет?\n'))
            list_links = []
            print ('Вводи ссылку на Giveaway и нажимай Enter\n')
            for i in range (amount_links):
                link = input ()
                list_links += [link]
            for i in range (N):
                list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, list_links, list_tegs [i]]]
                index_first += 1
            processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
            p = Pool (processes=processes)
            p.map (Check_Giveaway_not_subscription, list_lord)
        if answer2 == '2':
            amount_links = int (input ('Сколько ссылок будет?\n'))
            list_links_project = []
            list_links_Giveaway = []
            print ('Вводи ссылку на проект потом на его Giveaway и нажимай Enter после каждой ссылки\n')
            for i in range (amount_links):
                link_project = input ()
                link_Giveaway = input ()
                list_links_project += [link_project]
                list_links_Giveaway += [link_Giveaway]
            for i in range (N):
                list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, list_links_Giveaway, list_tegs [i], list_links_project]]
                index_first += 1
            processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
            p = Pool (processes=processes)
            p.map (Check_Giveaway_with_subscription, list_lord)
    #----------------------------------------------------------
    if answer == '5':
        index_first = int (input('Начиная с какого по счету аккаунта прогоняять?\n'))
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists(N,index_first)
        list_crypto_fonds = file_crypto_fonds ()
        print ('Сейчас введи промежуток от скольки до скольки примерно ссылок загнать\n')
        start = int (input ('От:'))
        end = int (input ('До:'))
        list_lord = []
        index_first -= 1
        for i in range (N):
                amount_infl = random.randint (start, end)
                list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, amount_infl, list_crypto_fonds ]]
                index_first += 1
        processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
        p = Pool (processes=processes)
        p.map (Check_subscription_fonds, list_lord)
    #----------------------------------------------------------
    if answer == '6':
        index_first = int (input('Начиная с какого по счету аккаунта прогоняять?\n'))
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists(N,index_first)
        list_lord = []
        index_first -= 1
        for i in range (N):
                list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1]]
                index_first += 1
        processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
        p = Pool (processes=processes)
        p.map (authorization_cookie_examination, list_lord)
    #----------------------------------------------------------
    if answer == '7':
        index_first = int (input('Начиная с какого по счету аккаунта прогоняять?\n'))
        N = int (input ('Сколько у тебя аккаунтов?\n'))
        list_proxy, list_login, list_password, list_number, list_User_Agent =  files_lists(N,index_first)
        list_link = list_new_link ()
        list_lord = []
        index_first -= 1
        for i in range (N):
            list_lord += [[list_proxy[i], list_login[i], list_password[i], list_number[i], list_User_Agent[i], index_first+1, list_link]]
            index_first += 1
        processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
        p = Pool (processes=processes)
        p.map (Check_subscription_on_new_account, list_lord)
    #-----------------------------------------------------------
    if answer == '8':
        answer2 = input ('Надо подписаться на первое поколение аккаунтов или на второе (друг на друга)?\n'
                         '1)Подписаться на первое поколение\n'
                         '2)Подписаться друг на друга\n'
                         '3)Авторизаться сначала нужно и сохранить куки и юзеры\n')
        if answer2 == '3':
            N = int (input ('Сколько у тебя аккаунтов?\n'))
            list_login, list_password, list_mail, list_User_Agent = files_lists_new_2_generation(N)
            list_lord = []
            numer_old = int (input ('Можешь пж еще зайти в файл куки и сказать номер последнеко кука?\n'))
            for i in range (N):
                list_lord += [[list_login[i], list_password[i], list_mail[i], list_User_Agent[i], numer_old+1]]
                numer_old +=1
            processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
            p = Pool (processes=processes)
            p.map (avatar_2_generation, list_lord)
            answer2 = input ('Ну вроде как все, заходи в файл куки, проверяй все ли на месте, если да, то нажми 1, если нет... Поговорим об этом позже\n')
            if answer2 == '1':
                record_2_generation()
                print ('Все перезаписал')
        if answer2 == '1':
            index_first = int (input('Начиная с какого по счету аккаунта прогоняять?\n'))
            N = int (input ('Сколько у тебя аккаунтов?\n'))
            list_login, list_password, list_mail, list_User_Agent =  files_lists_2_generation (N,index_first)
            list_links_1_generation = file_accounts_1_generation ()
            start = len (list_links_1_generation) - 5
            end = len (list_links_1_generation)-1
            list_lord = []
            index_first -= 1
            for i in range (N):
                amount_links = random.randint (start, end)
                list_lord += [[list_login[i], list_password[i], list_mail[i], list_User_Agent[i], index_first+1, amount_links, list_links_1_generation]]
                index_first += 1
            processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
            p = Pool (processes=processes)
            p.map (subscription_accounts_1_generation, list_lord)
        if answer2 == '2':
            index_first = int (input('Начиная с какого по счету аккаунта прогоняять?\n'))
            N = int (input ('Сколько у тебя аккаунтов?\n'))
            list_login, list_password, list_mail, list_User_Agent =  files_lists_2_generation (N,index_first)
            list_links_2_generation = file_accounts_2_generation ()
            list_lord = []
            index_first -= 1
            for i in range (N):
                amount_links = len(list_links_2_generation) 
                list_lord += [[list_login[i], list_password[i], list_mail[i], list_User_Agent[i], index_first+1, amount_links, list_links_2_generation]]
                index_first += 1
            processes =  int(input('Сколько параллельно процессов будем запускать?\n'))
            p = Pool (processes=processes)
            p.map (subscription_accounts_2_generation, list_lord)








