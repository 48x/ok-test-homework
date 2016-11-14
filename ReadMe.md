## Необходимые системные пакеты
python3.4 
python3.4-pip
chrome 53.0.2785.143+

## Необходимые python-пакеты
selenium (sudo python3-pip install selenium)

## Как запустить
1. Скачать репозиторий
2. Установить все, что указано выше
3. Указать в config.conf логин и пароль для аккаунта ok.ru:   
ok.login: - логин для входа в сервис   
ok.password: - пароль для входа в сервис    
4. В корневой папке проекта необходимо выполнить команду:
python3.4 -m unittest discover --pattern=*.py



