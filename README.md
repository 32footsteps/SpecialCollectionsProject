# SpecialCollectionsProject
##Setup Instructions for Linux
*[virtualenv](http://virtualenv.readthedocs.org/en/latest/), [MySQL](http://www.mysql.com/) or [mariadb](https://mariadb.org/), and
[Node.js](http://nodejs.org/) are required.*
* `Create special_collections_db database in MySQL.`
* `Create admin user.`
* `Fork this repository.`
* `$ git clone git@github.com:<your username>/https://github.com/zissou1898/SpecialCollectionsProject.git`
* `Update admin password in scwebapp/settings.py.`
* `$ cd SpecialCollectionsProject`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ ./manage.py migrate`
* `$ cd bin`
* `$ source activate`
* `$ cd .. && cd scwebapp`
* `$ ./manage.py runserver`
* `Open your browser to localhost:8000`
