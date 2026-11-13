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

## 3. Хранилище для картинок (Cloudflare R2, не обязательно)

Instagram и Threads скачивают картинку по публичной ссылке. Пока репозиторий **публичный**, ссылка
берётся прямо с GitHub, и этот шаг не нужен. Бакет нужен, только если репозиторий снова станет
приватным.

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

1. Actions → **whoami** → Run workflow. Должны быть видны имена всех подключённых аккаунтов.
2. Первый настоящий пост поставить в Story или в Threads text, проверить, что вышел, и потом
   включать ленту.

## 6. LinkedIn

Публикация идёт через официальный API LinkedIn. Через сам сайт ничего не нажимается: соглашение
LinkedIn запрещает автоматические действия на сайте, а API для этого и сделан.

### Личный профиль (`li-julia`)

1. **Страница компании.** Приложение LinkedIn обязательно привязывается к странице компании. Если у
   Nesso её ещё нет: LinkedIn → For Business → **Create a Company Page**.
2. linkedin.com/developers/apps → **Create app**. Название *Nesso Social*, страница Nesso, ссылка на
   политику конфиденциальности `https://nesso.fit/legal/en/privacy`, логотип.
3. Settings приложения → **Verify**: открыть ссылку под администратором страницы и подтвердить.
4. Вкладка **Products**: подключить **Share on LinkedIn** и **Sign In with LinkedIn using OpenID
   Connect**. Оба подключаются сразу, без проверки.
5. Вкладка **Auth** → Authorized redirect URLs → добавить ровно `http://localhost:8765/linkedin`.
6. Войти, на Mac, в папке `nesso-social`. Client ID и Client Secret на вкладке Auth:

   ```bash
   export LINKEDIN_CLIENT_ID=…
   read -s LINKEDIN_CLIENT_SECRET; export LINKEDIN_CLIENT_SECRET
   node bin/social.mjs linkedin-login li-julia
   unset LINKEDIN_CLIENT_SECRET
   ```

   Откроется LinkedIn, нажать **Allow**. Команда сама положит ключ в секрет `LI_JULIA_TOKEN` и дату
   окончания в переменную `LI_JULIA_TOKEN_EXPIRES`.

   Если LinkedIn не принял адрес из шага 5: linkedin.com/developers/tools/oauth/token-generator →
   выбрать приложение, отметить `openid`, `profile`, `w_member_social` → **Request access token** →
   скопировать ключ, затем:

   ```bash
   read -s LI_TOKEN; export LI_TOKEN
   node bin/social.mjs linkedin-login li-julia
   unset LI_TOKEN
   ```

7. Actions → **whoami**: в строке `li-julia` должно стоять имя владельца профиля.

**Каждые 60 дней вход нужно повторять** (шаг 6). Продлить его автоматически LinkedIn такому
приложению не даёт. Workflow `linkedin-expiry` по понедельникам проверяет дату и за 10 дней до конца
открывает issue с командами.

### Профиль Никиты (`li-nikita`)

Тот же порядок, что для `li-julia`, и то же приложение *Nesso Social*: новое приложение не нужно,
Share on LinkedIn разрешает публиковать любому участнику, который нажал **Allow**.

1. На этом Mac, в Chrome, где открыт LinkedIn **Никиты** (не Юли):
   ```
   export LINKEDIN_CLIENT_ID=…
   read -s LINKEDIN_CLIENT_SECRET; export LINKEDIN_CLIENT_SECRET
   node bin/social.mjs linkedin-login li-nikita
   unset LINKEDIN_CLIENT_SECRET
   ```
   Никита сам нажимает **Allow**. Ключ ляжет в секрет `LI_NIKITA_TOKEN`, дата в `LI_NIKITA_TOKEN_EXPIRES`.
2. Actions → **whoami**: в строке `li-nikita` должно стоять его имя.
3. Только после этого посты переезжают из `drafts/li-nikita/` в `posts/`. Раньше нельзя: без ключа пост
   падает каждые 10 минут и через 36 часов считается пропущенным.

### Страница Nesso (`li-nesso`)

Постить от страницы можно только после проверки LinkedIn (Community Management API).

1. **Отдельное приложение**, привязанное к той же странице: Community Management API должен быть
   единственным продуктом в приложении.
2. Products → **Community Management API** → заявка на **Development tier**. LinkedIn даёт этот API
   только зарегистрированным компаниям.
3. После одобрения заявка на **Standard tier**: политика конфиденциальности, запись экрана того, как
   публикуется пост, соответствие правилам LinkedIn. **При отказе повторно подать с этого же
   приложения нельзя**, только с нового, поэтому заявку готовим вместе.
4. Номер страницы (в адресе админки `linkedin.com/company/<номер>/admin`) записать в `accounts.json`
   как `"li-nesso": "<номер>"`. Это не секрет.
5. Войти, как в шаге 6 выше, но с Client ID и Secret этого приложения:
   `node bin/social.mjs linkedin-login li-nesso`. Входить нужно под администратором страницы.
