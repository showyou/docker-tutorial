from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

#db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/bbs?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', user),
        'password': os.getenv('DB_PASSWORD', password),
        'host': os.getenv('DB_HOST', host),
    })
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    name = db.Column(db.Text())
    article = db.Column(db.Text())


@app.route("/")
def bbs():
    text = Article.query.all()
    return render_template("index.html", lines=text)


@app.route("/result", methods=["POST"])
def result():
    date = datetime.now()
    article = request.form["article"]
    name = request.form["name"]
    admin = Article(pub_date=date, name=name, article=article)
    db.session.add(admin)
    db.session.commit()
    return render_template("bbs_result.html", article=article, name=name, now=date)


if __name__ == "__main__":
    app.run(debug=True)
