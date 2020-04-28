# portfolio
WebStructure

#### example_shop
#### command for run
#### create project folder
<code>
mkdir portfolio && cd portfolio
</code>

<code>
git clone https://github.com/Nurzhan097/portfolio.git
</code>

#### создание и активация вирт окружения windows
<code>
python -m venv env
.\env\Scripts\activate.bat
cd portfolio
pip install -r req.txt
</code>

#### запуск django приложения
#### Создание бд и супер пльзователя
<code>
manage.py migrate
manage.py createsuperuser
</code>

#### заполнить поля (email можно пропустить)

#### запуск суквера
<code>
manage.py runserver
</code>

