# 简单问答系统

```
pip freeze >requirements.txt

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

git clone https://github.com/django-notifications/django-notifications
cd django-notifications
python setup.py install

python -m venv <name>  #python3创建虚拟环境
```
##django-allauth
简介：Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

GitHub 地址：https://github.com/pennersr/django-allauth

文档地址：https://django-allauth.readthedocs.io/en/latest/

点评：增强 Django 内置的 django.contrib.auth 模块，提供登录、注册、邮件验证、找回密码等一切用户验证相关的功能。另外还提供 OAuth 第三方登录功能，例如国内的微博、微信登录，国外的 GitHub、Google、facebook 登录等，几乎囊括了大部分热门的第三方账户登录。配置简单，开箱即用。

##django-crispy-forms
简介：The best way to have DRY Django forms. The app provides a tag and filter that lets you quickly render forms in a div format while providing an enormous amount of capability to configure and control the rendered HTML.

GitHub 地址：https://github.com/django-crispy-forms/django-crispy-forms

文档地址：http://django-crispy-forms.rtfd.org/

点评：大大增强 Django 内置的表单功能，Django 内置的表单生成原生的 HTML 表单代码还可以，但为其设置样式是一个麻烦的事情。django-crispy-forms 帮助你使用一行代码渲染一个 Bootstrap 样式的表单，当然它还支持其它一些热门的 CSS 框架样式的渲染。

##django-mptt
简介：Utilities for implementing a modified pre-order traversal tree in django.

GitHub 地址：https://github.com/django-mptt/django-mptt

文档地址：https://django-mptt.readthedocs.io/

点评：配合 Django 的 ORM 系统，为数据库的记录生成树形结构，并提供便捷的操作树型记录的 API。例如可以使用它实现一个多级的评论系统。总之，只要你的数据结构可能需要使用树来表示，django-mptt 将大大提高你的开发效率。

##django-contrib-comments
简介：Django used to include a comments framework; since Django 1.6 it's been separated to a separate project. This is that project.

This framework can be used to attach comments to any model, so you can use it for comments on blog entries, photos, book chapters, or anything else.

GitHub 地址：https://github.com/django/django-contrib-comments

文档地址：https://django-contrib-comments.readthedocs.io/

点评：用于提供评论功能，最先集成在 django 的 contrib 内置库里，后来被移出来单独维护（可能觉得评论并非是一个通用的库吧）。这个评论库提供了基本的评论功能，但是只支持单级评论。好在这个库具有很好的拓展性，基于上边提到的 django-mptt，就可以构建一个支持层级评论的评论库，就像 我的博客评论区 中展示的这样（个人博客的评论模块就是基于 django-contrib-comments 和 django-mptt 写的）。

##django-notifications-hq
简介：GitHub notifications alike app for Django

GitHub 地址：https://github.com/django-notifications/django-notifications

文档地址：https://pypi.python.org/pypi/django-notifications-hq/

点评：没什么好说的，为你的网站提供类似于 GitHub 这样的通知功能。未读通知数、通知列表、标为已读等等。

##django-activity-stream
简介：Generate generic activity streams from the actions on your site. Users can follow any actors' activities for personalized streams.

GitHub 地址：https://github.com/justquick/django-activity-stream

文档地址：http://django-activity-stream.rtfd.io/en/latest/

点评：社交类网站免不了关注、收藏、点赞、用户动态等功能，这一个 app 全搞定。甚至用它实现一个朋友圈也不是不可能。

##django-easy-comment
GitHub 地址：https://github.com/r26zhao/django-easy-comment
文档地址：http://www.aaron-zhao.com/post/10/

##Markdown
教程地址：http://www.markdown.cn/