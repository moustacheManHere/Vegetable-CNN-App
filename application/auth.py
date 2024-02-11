from application import login_manager, db
from application.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))