from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into subject(\"subject_title\") values (:new_subject)")
    db.execute(sql, new_subject = 'Skypro')
    sql = text("delete from subject where subject_title = 'Skypro'")
    db.execute(sql)


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
