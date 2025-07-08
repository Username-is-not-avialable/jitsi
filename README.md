Для работы с jitsi необходимо:
1. добавить скрипт <script src='https://SERVER_URL/external_api.js'></script>
2. передать имя пользователя через объявление api iframe при помощи
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
