# Задача
Требуется разработать программу-редиректор для прокси-сервера Squid, выполняющую перезапись
(перенаправление) запросов на заданные сайты.

Например, имеется список перенаправлений вида "ключ": "значение":

yandex.ru: google.com
lurkmore.to: wikipedia.org
linux.org.ru: kernel.org

Когда пользователь через Squid обращается на yandex.ru, запрос должен переписываться и перенаправ-
ляться на google.com.

## Требования к программе:

логирование всех действий в syslog;
список перенаправлений должен быть представлен в виде файла с данными в формате JSON;
все изменения в списке перенаправлений должны начинать работать сразу же, не требуя перезапуска Squid;

## Необязательные требования, реализация которых будет учтена особо:

готовый spec-файл для сборки RPM-пакета с программой;
готовые конфиги для rsyslog и logrotate чтобы все сообщения программы попадали в определённый файл лога;


## Предпочтительные средства реализации:

CentOS 6.5;
язык программирования: Python или C;
дополнительные библиотеки: на ваш выбор, лучше если их не будет;
Результаты оформляются в виде git-репозитория со всеми необходимыми файлами: настройками Squid,
исходниками программы и демонстрационным файлом со списком перенаправлений;

## Документация:

http://wiki.squid-cache.org/Features/Redirectors
http://www.squid-cache.org/Doc/config/url_rewrite_program