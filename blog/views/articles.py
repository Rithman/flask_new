from flask import render_template, Blueprint, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.models.database import db
from blog.models import Author, Article
from blog.forms.article import CreateArticleForm


articles_app = Blueprint('articles_app', __name__)



@articles_app.route('/', endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template('articles/list.html', articles=articles)


@articles_app.route('/<int:article_id>/', endpoint="details")
def article_details(article_id):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articles/details.html", article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    print(request.method)
    if request.method == "POST" and form.validate_on_submit():
        print("Form is valid!")
        article = Article(title=form.title.data.strip(), body=form.body.data)
        
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()
            article.author = current_user.author

        try:
            db.session.add(article)
            db.session.commit()
            print("Commit successful!")
        except IntegrityError:
            current_app.logger.exception("Could not create new article!")
            error = "Could not create new article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))
        
    return render_template("articles/create.html", form=form, error=error)