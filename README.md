# interactactwel-django-app
Front-end development of ScGap

### Set up  ###

* Install [Cactus](https://github.com/eudicots/Cactus/blob/master/README.md) with the following one liner

**sudo easy_install cactus**

* Clone this repository in to your local machine

### Building your site ###

When you build your site it will generate a static version in the build folder that you can upload to any host. Basically it will render each page from your pages folder, copy it over to the build folder and add all the static assets to it so it becomes a self contained website. You can build your site like this:

cd directory-where-cloned/interactactwel-django-app/

**cactus build**

Your rendered website can now be found in the (hidden) [path]/.build folder. Cactus can also run a small webserver to preview your site and update it when you make any changes. This is really handy when developing to get live visual feedback.

You can run it like this:

**cactus serve**

View site at http://127.0.0.1:8000
