# Squid_redirector
Перенаправление запросов на заданные сайты

## Установка Squid
### Автоматическая
```
sudo python3 setup.py
```
### Ручная
```
sudo apt-get install squid
squid -v | grep Version
```
Squid Cache: Version 3.5.27

#### Настройка
- содать папку build и закинуть туда redirector.py
```
mkdir /build
cp redirector.py /build/
```
- список перенаправлений должен иметь формат JSON, имя "config.json" и находится в /build/
- добавьте в конфигурацию для squid(/etc/squid/squid.conf)
```
url_rewrite_extras "%>a %>rm %un"
url_rewrite_children 1
url_rewrite_program /build/redirector.py
```
- выдать права для того чтобы писались логи в файл logs.log
```
chmod -R 777 /build
```
- перезапустите squid
```
systemctl restart squid
```
   или
```
service squid restart
```
