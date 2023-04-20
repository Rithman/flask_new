from blog.app import create_app
from blog.models.database import db



app = create_app() 
app.run(
    host='0.0.0.0',
    debug=True,
)


@app.cli.command("init-db")
def init_db():
    """
    Run in terminal:
    flask init-db
    """

    db.create_all()
    print("DB initialized!")


@app.cli.command("create-users")
def create_users():
    """
    Run in terminal:
    flask create-users
    """

    from blog.models import User
    admin =  User(username="admin", is_staff=True)
    james = User(username="james")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("Users created:", admin, james)