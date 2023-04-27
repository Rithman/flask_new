import os
from dotenv import load_dotenv

from blog.app import create_app
from blog.models.database import db

load_dotenv()

app = create_app() 
app.run(
    host='0.0.0.0',
    debug=True,
)


@app.cli.command("create-admin")
def create_admin():
    """
    Run in terminal:
    flask create-admin
    """

    from blog.models import User
    admin =  User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("Users created:", admin)

