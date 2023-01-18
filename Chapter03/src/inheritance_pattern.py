"""
Inheritance and Composition
"""

from datetime import datetime
from unittest import TestCase, main


class TransactionalPolicy:

    def __init__(self, policy_data, **extra_data):
        self._data = {**policy_data, **extra_data}

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)

    def __getitem__(self, customer_id):
        return self._data[customer_id]

    def __len__(self):
        return len(self._data)

    def display(self):
        for k, v in self._data.items():
            print(k, v)


class TestPolicy(TestCase):
    def test_get_policy(self):
        policy = TransactionalPolicy({
            "client001": {
                "fee": 100.0,
                "expiration_date": datetime(2022, 1, 3)
            },
            "client002": {
                "fee": 403.23,
                "expiration_date": datetime(2022, 8, 5)
            }
        },
            extra_data={
            "client001": {
                "food": "eba"
            }
        }
        )
        policy.display()
        print(policy['client001'])
        print(policy['extra_data'])


if __name__ == "__main__":
    main()
