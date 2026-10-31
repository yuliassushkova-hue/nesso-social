# Подключение аккаунтов

Делается один раз. Шаги с входом в аккаунты и токенами делаете вы: токены никогда не вставляются в
чат, только в GitHub Secrets командой `gh secret set` (она сама спросит значение).

## 1. Instagram и Threads

1. **Оба Instagram сделать профессиональными.** В приложении: Настройки → Тип аккаунта и
   инструменты → Переключиться на профессиональный аккаунт → **Бизнес** (или Автор). Публикация через
   API работает только для профессиональных аккаунтов.
2. **Завести Threads из каждого Instagram**, если ещё нет: войти в Threads под итальянским, потом под
   датским аккаунтом.

## 2. Приложение Meta

1. developers.facebook.com → My Apps → **Create app**. Название, например, *Nesso Social*.
2. Добавить два сценария (use cases):
   - **Manage messaging & content on Instagram** (это «Instagram API с входом через Instagram», без
     Facebook-страницы);
   - **Access the Threads API**.
3. App Review не нужен: мы публикуем только в свои аккаунты, а им хватает роли в приложении.

### Токены Instagram

1. В сценарии Instagram → **API setup with Instagram login** → разрешения
   `instagram_business_basic` и `instagram_business_content_publish`.
2. **Generate access tokens → Add account**: войти итальянским аккаунтом, потом датским. Для каждого
   появится токен на 60 дней.
3. В терминале, в папке `nesso-social`:

   ```bash
   gh secret set IG_IT_TOKEN
   gh secret set IG_DK_TOKEN
   ```

### Токены Threads

1. В сценарии Threads → Permissions: `threads_basic`, `threads_content_publish`.
2. **App roles → Roles → Add people → Threads Tester**: добавить оба Threads-профиля. Принять
   приглашение в каждом: Threads → Настройки → Аккаунт → Разрешения веб-сайтов → Приглашения.
3. Короткий токен для каждого профиля: Graph API Explorer, в правом верхнем углу переключить хост на
   **threads.net**, выбрать приложение, Generate Threads Access Token, войти нужным профилем.
4. Обменять короткий токен на долгий (60 дней) и сразу положить в секрет. App Secret берётся в
   приложении: App settings → Basic → **Threads App Secret**. Значения вводятся скрыто:

   ```bash
   read -s THREADS_APP_SECRET; export THREADS_APP_SECRET
   read -s SHORT_TOKEN; export SHORT_TOKEN          # итальянский профиль
   node bin/social.mjs exchange-threads THREADS_IT_TOKEN
   read -s SHORT_TOKEN; export SHORT_TOKEN          # датский профиль
   node bin/social.mjs exchange-threads THREADS_DK_TOKEN
   unset THREADS_APP_SECRET SHORT_TOKEN
   ```

## 3. Хранилище для картинок (Cloudflare R2)

Instagram и Threads скачивают картинку по публичной ссылке, поэтому перед публикацией файл кладётся
в публичный бакет.

1. Cloudflare → R2 → **Create bucket** `nesso-social-media`.
2. Settings бакета → **Public access**: включить r2.dev или подключить свой домен (например,
   `media.nesso.fit`).
3. Settings → **Object lifecycle rules**: удалять объекты старше 30 дней (после публикации файл
   платформам больше не нужен).
4. R2 → **Manage API tokens → Create API token**: Object Read & Write, только для этого бакета.
5. Секреты:

   ```bash
   gh secret set R2_ACCOUNT_ID
   gh secret set R2_ACCESS_KEY_ID
   gh secret set R2_SECRET_ACCESS_KEY
   gh secret set R2_BUCKET          # nesso-social-media
   gh secret set MEDIA_BASE_URL     # https://pub-….r2.dev или https://media.nesso.fit
   ```

## 4. Продление токенов

Токены живут 60 дней. Workflow `refresh-tokens` продлевает их 1-го и 15-го числа и записывает новые
в секреты, для этого ему нужен свой ключ:

1. github.com → Settings → Developer settings → **Fine-grained tokens** → Generate. Доступ только к
   репозиторию `nesso-social`, разрешение **Secrets: Read and write**.
2. `gh secret set SECRETS_PAT`

## 5. Проверка

1. Actions → **whoami** → Run workflow. Должны быть видны четыре имени аккаунтов.
2. Первый настоящий пост поставить в Story или в Threads text, проверить, что вышел, и потом
   включать ленту.
