"""Clean Code in Python - Chapter 3: General Traits of Good Code
> Exceptions
"""

class InternalDataError(Exception):
    """An Exception with data of our domain problem"""

def process(data_dictionary: dict, record_id: int)->dict:
    try:
        return data_dictionary[record_id]
    except KeyError as e:
        raise InternalDataError("Record id: {} not present".format(record_id)) from e 