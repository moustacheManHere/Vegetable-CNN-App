from application.models import *

def test_vegetable_database_empty(db):
    assert db.session.query(Vegetable).count() == 15
    new_vegetable = Vegetable(name='Test Vegetable', filename='test_filename.jpg', 
                              short='Short description', description='Description of the vegetable')
    db.session.add(new_vegetable)
    db.session.commit()
    assert db.session.query(Vegetable).count() == 16