# SpecialCollectionsProject
##Setup Instructions Linux
*[virtualenv](http://virtualenv.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/) are required.*
* Fork this repository.
* `$ git clone git@github.com:<your username>/https://github.com/zissou1898/SpecialCollectionsProject.git`
* `$ cd SpecialCollectionsProject`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py migrate`
* `$ cd SpecialCollectionsProject/bin`
* `$ source activate`
* `$ cd ..`
* `$ python manage.py runserver`
