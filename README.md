# World Skills 2022
Репозиторий с файлами для подготовки к Нац.Финалу

### Ссылки
* [Видео на официальном сайте](https://nationalteam.worldskills.ru/skills/programmnye-resheniya-dlya-biznesa/)
* [Задания](https://disk.yandex.ru/d/CdEwG64Rmj_GPQ)
* [Регламент и библиотеки](https://drive.google.com/drive/folders/1wu9fiemVfVd9zu6eYKd_jIY2vomRFSdU)

### Материалы для обучения
* [PyQT5](https://www.youtube.com/playlist?list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa)

### Запуск
```shell
pip install -r requirements.txt
docker-compose up -d 

# SQL CONSOLE
docker exec -it worldskills2022-database-1 bash
mysql -uworldskills -pworldskills

USE worldskills;
```
