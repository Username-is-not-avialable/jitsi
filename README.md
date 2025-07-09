# Запуск Jitsi Meet через Docker Compose

## Подготовка окружения

1. **Клонирование репозитория**  
   Выполните команду для клонирования репозитория:
   ```bash
   git clone https://github.com/Username-is-not-avialable/docker-jitsi-meet.git
   cd docker-jitsi-meet
   ```
2. **Настройка переменных окружения**
   Создайте файл .env на основе примера:
   
   ```bash
   cp env.example .env
   ```
3. **Генерация паролей**
   Запустите скрипт для установки безопасных паролей:
   
   ```bash
   ./gen-passwords.sh
   ```
4. **Создание ```CONFIG``` директорий**
   Выполните команду для создания ```CONFIG``` директорий
   
   ```bash
   mkdir -p ~/.jitsi-meet-cfg/{web,transcripts,prosody/config,prosody/prosody-plugins-custom,jicofo,jvb,jigasi,jibri}
   ````
5. **Скопируйте кастомные файлы конфигурации в   ```CONFIG/web``` директорию**
   ```
   cp custom_configs/* ~/.jitsi-meet-cfg/web
   ```
6. **Запустите проект с помощью docker compose**
   ```bash
   docker compose up -d
   ```
7. **Откройте в браузере**
   Перейдите на https://localhost:8443/
   Подробнее на официальном сайте https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker

## Инструкция по подключению jitsi к веб странице:
1. добавить скрипт
```<script src='https://SERVER_URL/external_api.js'></script>```
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
