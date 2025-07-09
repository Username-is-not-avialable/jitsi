# Запуск jitsi
## Установите и заупстите jitsi по инструкции с официального сайта: https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker
## Скопируйте кастомные файлы конфигурации
```
cp custom_configs/* ~/.jitsi-meet-cfg/web

Инструкция по подключению jitsi к странице:
1. добавить скрипт <script src='https://SERVER_URL/external_api.js'></script>
2. передать имя пользователя через объявление api iframe при помощи кода ниже:
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
