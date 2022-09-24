run = print


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgress.service")


def db_backup():
    run("pg_dump database")
