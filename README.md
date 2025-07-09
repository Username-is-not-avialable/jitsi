## Запуск jitsi
### Установите и запустите jitsi по инструкции с официального сайта: https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker
### Скопируйте кастомные файлы конфигурации
```
cp custom_configs/* CONFIG/web
```
Если устанваливать jitsi по инструкции с официального сайта, то CONFIG = ~/.jitsi-meet-cfg

## Инструкция по подключению jitsi к странице:
1. добавить скрипт
```<script src='https://SERVER_URL/external_api.js'></script>```
3. передать имя пользователя через объявление api iframe при помощи кода ниже:
```
const domain = 'SERVER_URL'; // подставить SERVER_URL из config.py
const options = {
                roomName: roomName,
                userInfo: {
                    displayName: userName // переменная userName должна хранить актуальное имя пользователя
                },
                parentNode: document.getElementById('jitsi-container'), // пример parentNode
const api = new JitsiMeetExternalAPI(domain, options);
```
