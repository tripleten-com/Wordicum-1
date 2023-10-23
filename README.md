# Wordicum-1

## Creating a repository
1. Create a repository for yourself, using this template.  
  Press the "Use this template" button and select the "Create a new repository" option.  
  ![image](https://user-images.githubusercontent.com/14962819/235599080-2819c72b-3161-48fe-926d-91c289941c20.png)
  
1. Fill in the **Repository name** and **Description** fields and click the "Create repository from template" button.  
  ![image](https://user-images.githubusercontent.com/14962819/235599367-6b6025e2-5ceb-4b57-87f4-8c3a2ac18a5b.png)


## How to work with the repository
To start the task, you need to copy the URL of your repository and clone it. (Please note that you are cloning your own repository, not the original template!)  
  ![image](https://user-images.githubusercontent.com/14962819/235600053-de6be309-56d5-4c5f-adc3-d466887962f6.png)
  
### Create a virtual environment

1. Launch the Visual Studio Code editor, and through the "*File" / "Open Directory"* menu, open the *Dev/ya-tube-1/* folder. 
2. Launch the terminal in VS Code and make sure you work from the *ya-tube-1/* directory. If you use Windows, make sure Git Bash runs in the terminal, and not through anything else, like PowerShell. Run this command:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
The virtual environment will be deployed in the *wordicum-1/* directory. The `venv` folder will appear there too and will store all the project dependencies. The file structure will look like this:

```
Dev/
 └── ya-tube-1/
     ├── tests/             Тесты Практикума, проверяющие проект
     ├── venv/              Virtual environment directory
     ├── ya-tube-1/         <-- Project directory
     |   ├── ...            <-- Django project structure
     |   └── manage.py      
     ├── .gitignore         List of files and folders hidden from Git tracking 
     ├── db.json            <-- Fixtures for the database    
     ├── LICENSE            License   
     ├── pytest.ini         TripleTen tests configuration
     ├── README.md          Project description 
     └── requirements.txt   Project dependency list
```

### Activation of the virtual environment
In the terminal, navigate to the root directory of the *Dev/wordicum-1/* project and execute this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Now all commands in the terminal will be preceded by the string `(venv)`.

💡 All the following console commands must be run with the working virtual environment.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

### Install the dependencies from the *requirements.txt* file
While in the *Dev/wordicum-1/* folder, execute this command:

```bash
pip install -r requirements.txt
```

#### End of support for dependencies

The LTS versions of dependencies have been chosen.
Для Django выбрана версия 3.2, extended support которой
[ends](https://endoflife.date/django) on April 1, 2024.

### Using migrations

    
In the directory with the "manage.py" file, run this command: 

```bash
python manage.py migrate
```

### Running the project in dev mode

    
In the directory with the "manage.py" file, run this command: 

```bash
python manage.py runserver
```

In response to the command, Django will report that the server is running and the project is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Local test launch
Having finished the task, launch the local tests. In the terminal, navigate to the root directory of the *Dev/wordicum-1/* project and execute this command:
```shell
pytest
```
If all the test cases are successful, the project will be considered completed. Otherwise, you will have to fix the parts that haven't passed the tests and launch them once again.
