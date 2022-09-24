class InternalDataError(Exception):
    """An exception with the data of our main problem"""


def process(data_dictionary, record_id):
    try:
        return data_dictionary[record_id]
    except KeyError as e:
        raise InternalDataError("Record not present") from e


if __name__ == "__main__":
    process({"a": "f"}, "a")
    #  process({"a": "f"}, "b")
