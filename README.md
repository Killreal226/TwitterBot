# TwitterBot

Данный бот предназначен для увеличения вероятности выигрыша Giveaway в twitter, путем их прохождения массой аккаунтов. А также он включает в себя возможность:
1. настройки новых аккаунтов (создание куки, настройки аватарки);
2. Выкладывания твитов, как с картинками, так и без;
3. Массовой подписки на один какой то канал;
4. Прохождения Giveaway (т.е. Лайк поста, ретвит поста, и теганье друзей)
5. Массовой подписки на множество инфлюинсеров 
6. Подписки своих аккаунтов друг на друга

Все действия делаются с личных прокси, реализовано все с помощью Selenium

## Установка 
1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение 
3. Установите зависимости 
`pip install -r requirements.txt`
4. Для установки __Selenium WebDriver__ воспользуйтесь этим источником [https://habr.com/ru/articles/248559/](https://habr.com/ru/articles/248559/)

##Настройка бота

Для настройки бота нужно сначала нужно подготовить все данные аккаунтов:
1. В файл __proxy_new.txt__ На каждый аккаунт напишите личный прокси аккаунта в виде: _Логин:Пароль@IP:Порт_
Пример:
```
ccDbb4N9:Y6eZzsqL@193.232.88.157:56141
ccDbb4N9:Y6eZzsqL@45.138.6.250:58290
ccDbb4N9:Y6eZzsqL@77.83.7.212:55703
ccDbb4N9:Y6eZzsqL@195.208.119.68:48508
ccDbb4N9:Y6eZzsqL@195.208.120.132:56079
```
2.В файл __login_password_new.txt__ на каждый аккаунт напишите логин и пароль от входа в виде: _Логин/Пароль/Номер телефона_
Пример:
```
GladW763229629/Lx9zfmwqzl1mOtm/6283545450832
KaraGr165812561/yAnyog4jjSxVMED/6282155297469
Jasmin11851fe7/EX61L6BJzOiutn6/628258103011
AmandaW63728937/gpMFgFgqErWEiF5jSl/624589142216
LizTorF27636/GfDzVcEqzeM9N5SQ/62898854520941
```
3. В файл __User-Agent_new__ на каждый аккаунт напишите UserAgent
Пример:
```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.17
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36
Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36
Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
```
4. В папку __avatar__ сохраните картинки для авотарок своих аккаунтов в виде номер аккаунта.png
Пример: `2.png`
5. Теперь активируйте программу командой 
`python TwitterBot.py`
И следуйте указаниям программы по настройки аккаунтов

6. После того, как программа закончит настройку, работающие аккаунты скопируйте в соответсвующие прошлым пунктам __proxy.txt__, __login_password.txt__, __User-Agent.txt__

## Дополнительные функции

### Выкладывание твитов

#### Без картинки 
Для работы этой функции в файл __phrases.txt__ напишите в каждую строку фразу, которую хотите твитнуть 
Пример:
```
Everything you can imagine is real. 
Life is a progress, and not a station 
You can never understand one language until you understand at least two.
You can never be overdressed or overeducated. 
Don’t let yesterday take up too much of today.
```
Теперь активируйте программу командой 
`python TwitterBot.py` 
и нажмите 2, после чего следуйте указаниям программы
#### С картинкой 
Для работы этой функции помимо фраз из предыдущего пункта перейдите в папку cookies\img_tweet и сохраните туда картинки для твитов (названия должны быть номер аккаунта.png)
Пример: `3.png`

Теперь активируйте программу командой 
`python TwitterBot.py` 
и нажмите 2, после чего следуйте указаниям программы

### Массовая подписка на один аккаунт

Для работы этой фукции просто активируйте программу командой
`python TwitterBot.py` 
Нажмите 3 и следуйте указаниям программы

### Прохождение Giveaway 

Для работы этой функции в файл __tegs.txt__ напишите то, кого будете тегать, а также (по желанию) любой текст, который будет сопровождать тег
Пример:
```
@Charlie0345263 @Merilyn81785307 @Majorie742552 oh it's great!!  
@So23824845 @Tamela34407476 @Sixta75847399  
@Gretche85479942 @Elvie58727120 @Else75201605 Let's see ..  	  
@Selena41255946 @Maryann7854592 @Breanne124564700  
@Kenisha8785228029 @Shaquit12043777 @Ramona14287464   
```
После чего Для работы этой фукции просто активируйте программу командой
`python TwitterBot.py` 
Нажмите 4 и следуйте указаниям программы

### Массовая подписка на множество инфлюинсеров

Для работы этой функции в файл __crypto_fonds.txt__ напишите ссылки на аккаунты инфлюинсеров
Пример:
```
https://twitter.com/caseykcaruso
https://twitter.com/mizbani_
https://twitter.com/snmishra311
https://twitter.com/_charlienoyes
https://twitter.com/danrobinson
https://twitter.com/_Dave__White_
```
После чего Для работы этой фукции просто активируйте программу командой
`python TwitterBot.py` 
Нажмите 5 и следуйте указаниям программы

### Подписка своих аккаунтов друг для друга

Для работы этой фукции просто активируйте программу командой
`python TwitterBot.py` 
Нажмите 7 и следуйте указаниям программы


