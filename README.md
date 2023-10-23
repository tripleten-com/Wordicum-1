# Wordicum-1

## Creating a repository
1. Create a repository for yourself, using this template.  
  Для этого необходимо нажать кнопку "Use this template" и выбрать пункт "Create a new repository".  
  ![image](https://user-images.githubusercontent.com/14962819/235599080-2819c72b-3161-48fe-926d-91c289941c20.png)
  
1. Заполнить поля **Repository name** и **Description** и нажать кнопку "Create repository from template".  
  ![image](https://user-images.githubusercontent.com/14962819/235599367-6b6025e2-5ceb-4b57-87f4-8c3a2ac18a5b.png)


## Как работать с репозиторием
Чтобы начать выполнение задания необходимо скопировать url вашего репозитория и склонировать его себе (обратите внимание, что вы клонируете именно ваш репозиторий, а не исходный шаблон!).  
  ![image](https://user-images.githubusercontent.com/14962819/235600053-de6be309-56d5-4c5f-adc3-d466887962f6.png)
  
### Создайте виртуальное окружение

1. Запустите редактор Visual Studio Code и через меню «*Файл» / «Открыть директорию»* откройте папку *Dev/ya-tube-1/*. 
2. Запустите терминал в VS Code, удостоверьтесь, что вы работаете из директории *ya-tube-1/* (если вы работаете под Windows, убедитесь, что в терминале запущен Git Bash, а не PowerShell или что-нибудь ещё), и выполните команду:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
В директории *ya-tube-1/* будет развёрнуто виртуальное окружение и появится папка `venv`, в которой будут храниться все зависимости проекта, а структура файлов станет такой:

```
Dev/
 └── ya-tube-1/
     ├── tests/             Тесты Практикума, проверяющие проект
     ├── venv/              Директория виртуального окружения
     ├── ya-tube-1/         <-- Директория проекта
     |   ├── ...            <-- Структура Django проекта
     |   └── manage.py      
     ├── .gitignore         Список файлов и папок, скрытых от отслеживания Git (скрытый) 
     ├── db.json            <-- Фикстуры для базы данных    
     ├── LICENSE            Лицензия   
     ├── pytest.ini         Конфигурация тестов Практикума
     ├── README.md          Описание проекта 
     └── requirements.txt   Список зависимостей проекта
```

### Активация виртуального окружения
в терминале перейдите в корневую директорию проекта *Dev/ya-tube-1/* и выполните команду:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Теперь все команды в терминале будут предваряться строкой `(venv)`.

💡 Все дальнейшие команды в терминале надо выполнять с активированным виртуальным окружением.

Обновите pip:

```bash
python -m pip install --upgrade pip
```

### Установка зависимостей из файла *requirements.txt*:
Находясь в папке *Dev/ya-tube-1/*, выполните команду:

```bash
pip install -r requirements.txt
```

#### End of Support зависимостей

Среди зависимостей выбраны LTS-версии зависимостей.
Для Django выбрана версия 3.2, extended support которой
[заканчивается](https://endoflife.date/django) 1 апреля 2024 года.

### Применение миграций

    
В директории с файлом manage.py выполните команду: 

```bash
python manage.py migrate
```

### Запуск проекта в dev-режиме

    
В директории с файлом manage.py выполните команду: 

```bash
python manage.py runserver
```

В ответ Django сообщит, что сервер запущен и проект доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Локальный запуск тестов
После выполнения задания необходимо локально запустить тесты. В терминале перейдите в корневую директорию проекта *Dev/ya-tube-1/* и выполните команду:
```shell
pytest
```
Если все тесты пройдены успешно, то проект считается выполненным. В противном случае необходимо устранить моменты, которые не прошли проверку и повторно запустить тесты.
