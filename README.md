# SpecialCollectionsProject
##Setup Instructions for Linux
*[virtualenv](http://virtualenv.readthedocs.org/en/latest/), [MySQL](http://www.mysql.com/) or [mariadb](https://mariadb.org/), and
[Node.js](http://nodejs.org/) are required.*
* `Import special_collections_db.sql into MySQL.`
* `Fork this repository.`
* `$ git clone git@github.com:<your username>/https://github.com/zissou1898/SpecialCollectionsProject.git`
* `Update admin password in specialcollections/settings.py.`
* `$ cd SpecialCollectionsProject`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ cd bin`
* `$ source activate`
* `Create admin user by running ./manage.py createsuperuser`
* `$ ./manage.py migrate`
* `$ cd .. && cd specialcollections`
* `$ ./manage.py runserver`
* `Open your browser to localhost:8000`
