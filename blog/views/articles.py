from flask import render_template, Blueprint
from werkzeug.exceptions import NotFound

from ..views.users import USERS_LIST

articles_app = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES_LIST = {
    1: 
    {
        'title': 'Илон Макс: провидец или разведчик с Альфы Центавра?',
        'text': 'Маск родился и вырос в Претории, ЮАР. Некоторое время учился в Преторийском университете, а в 17 лет переехал в Канаду. \
                Поступил в Университет Куинс в Кингстоне и через два года перевёлся в Пенсильванский университет, \
                где получил степень бакалавра по экономике и физике. В 1995 году переехал в Калифорнию, чтобы учиться в Стэнфордском университете, \
                но вместо этого решил заняться бизнесом и вместе со своим братом Кимбалом  (англ.)рус. стал соучредителем компании Zip2, \
                занимавшейся разработкой программного обеспечения для интернета. В 1999 году компания была приобретена Compaq за 307 миллионов долларов. \
                В том же году Маск стал соучредителем онлайн-банка X.com, который в 2000 году конгломеративным путем консолидировался с Confinity и образовал PayPal...',
        'author': 1
    },
    2: 
    {
        'title': 'GTA по-американски…',
        'text': 'Курьезный случай произошел в США. Мужчина оставил на заправке свою машину, а собака, находившаяся в салоне авто, \
                 решила «порулить» и протаранила другой автомобиль. Как маленькому песику породы чихуахуа удалось управлять автомобилем Toyota не понятно.',
        'author': 2
    },
    
}


@articles_app.route('/')
def render_articles():
    return render_template('articles/articles_list.html', articles_list=ARTICLES_LIST)


@articles_app.route('/<int:pk>')
def render_article_by_pk(pk:int):
    if pk in ARTICLES_LIST:
        article = ARTICLES_LIST[pk]
        return render_template('articles/article_details.html', title=article['title'], text=article['text'], user_id=article['author'], user_name=USERS_LIST[article['author']])
    else:
        raise NotFound(f'Article with id: {pk} NOT FOUND')
