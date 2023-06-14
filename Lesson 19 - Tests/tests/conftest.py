import pytest

from app import app, db, Article


@pytest.fixture(scope='session')
def test_app():
    # Create a test database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_blog.db'

    # Set SQLAlchemy to use the test database
    db.app = app
    db.create_all()

    # Populate the test database with data
    with app.app_context():
        create_test_data()
        yield app

    # Clean up and delete the test database
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope='function')
def client(test_app):
    # Create a test client using the Flask app
    with test_app.test_client() as client:
        # Establish an application context before running each test function
        with app.app_context():
            yield client


def create_test_data():
    # Create test blog posts
    post1 = Article(title='Post 1', body='This is the first blog post.')
    post2 = Article(title='Post 2', body='This is the second blog post.')

    # Add test data to the database
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
