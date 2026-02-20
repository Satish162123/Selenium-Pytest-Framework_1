import pytest
from utils.db_client import DBClient

@pytest.mark.db_validation
def test_user_exists_in_db():

    db = DBClient()

    query = "SELECT * FROM users WHERE username = %s"
    result = db.execute_query(query, ("satish",))

    assert len(result) > 0
    assert result[0]["username"] == "satish"

    db.close()

@pytest.mark.db_validation
def test_insert_and_validate_user():

    db = DBClient()

    insert_query = """
        INSERT INTO users (username, email)
        VALUES (%s, %s)
        RETURNING id;
    """

    result = db.execute_query(
        insert_query,
        ("api_user2", "api_user2@test.com")
    )

    user_id = result[0]["id"]

    select_query = "SELECT * FROM users WHERE id = %s"
    user = db.execute_query(select_query, (user_id,))

    assert user[0]["username"] == "api_user2"

    db.close()
