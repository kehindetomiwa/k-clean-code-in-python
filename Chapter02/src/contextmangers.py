import contextlib
import db_utils as dbu


@contextlib.contextmanager
def db_handler():
    dbu.stop_database()
    yield
    dbu.start_database()


class dbhandler_decorator(contextlib.ContextDecorator):

    def __enter__(self):
        dbu.stop_database()

    def __exit__(self, ext_type, ex_value, ex_traceback):
        dbu.start_database()


@dbhandler_decorator()
def offline_backup():
    dbu.db_backup()


def main():
    with db_handler():
        dbu.db_backup()

    offline_backup()


if __name__ == "__main__":
    main()