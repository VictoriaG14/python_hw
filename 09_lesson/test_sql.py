from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pytest


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"


@pytest.fixture(scope="module")
def db():
    engine = create_engine(db_connection_string)
    yield engine
    engine.dispose()


def test_insert(db):
    # Добавление
    sql = text("insert into subject(subject_title) values (:new_subject) returning subject_id")
    result = db.execute(sql, new_subject='Skypro')
    new_id = result.fetchone()[0]
    db.commit()
    # Проверка, что запись есть
    row = db.execute(text("select subject_title from subject where subject_id = :id"), {"id": new_id}).fetchone()
    assert row is not None
    assert row[0] == "Skypro"
    # Очистка
    db.execute(text("delete from subject where subject_id = :id"), {"id": new_id})
    db.commit()

def test_update():
    db = create_engine(db_connection_string)
    sql = text("insert into subject(\"subject_title\") values (:new_subject)")
    db.execute(sql, new_subject='Skypro')
    sql = text("update subject set subject_id = 30 where subject_id is NULL")
    db.execute(sql)
    sql = text("delete from subject where subject_id = 30")
    db.execute(sql)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("insert into subject(\"subject_title\") values (:new_subject)")
    db.execute(sql, new_subject='sql')
    sql = text("delete from subject where subject_title = 'sql'")
    db.execute(sql)
