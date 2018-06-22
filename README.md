# Squid_redirector
Перенаправление запросов на заданные сайты

## Установка Squid
```
  sudo apt-get install squid
```
## Настройка
- содать папку build и закинуть туда redirector.py
```
  mkdir /build
  cp redirector /build/
```
- список перенаправлений должен иметь формат JSON и находится в /build/
- добавьте в конфигурацию для squid(/etc/squid/squid.conf)
```
  url_rewrite_extras "%>a %>rm %un"
  url_rewrite_children 1
  url_rewrite_program /build/redirector.py
```
- перезапустите squid
```
systemctl restart squid
```
   или
```
service squid restart
```
