import db_utils as dbu


class DBHandler:

    def __enter__(self):
        dbu.stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        dbu.start_database()


def main():
    with DBHandler():
        dbu.db_backup()


if __name__ == "__main__":
    main()