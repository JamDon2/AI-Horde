import datetime

from redis_om import (EmbeddedJsonModel, Field, JsonModel, Migrator, HashModel)
from pydantic import PositiveInt
from typing import Optional, List
from customer import Customer

# Migrator().run()

# andrew = Customer(
#     first_name="Andrew",
#     last_name="Brookins",
#     email="andrew.brookins@example.com",
#     join_date=datetime.date.today(),
#     age=38,
#     bio="Python developer, works at Redis, Inc.",
#     liii=[1,2,3,4,5]
# )

# bob = Customer(
#     first_name="Bob",
#     last_name="Boob",
#     email="bob.brookins@example.com",
#     join_date=datetime.date.today(),
#     age=32,
#     bio="Python PR, works at Redis, Inc.",
#     liii=[1,2,3,4,5]
# )

# andrew.save()
# bob.save()
# print(andrew)
# Customer.find(Customer.last_name == "Brookins").all()[0] == andrew
# print(Customer.find(Customer.age == 32).all())
andrew = Customer.find(Customer.last_name == "Brookins").all()[0]
# print([andrew, type(andrew)])
assert Customer.find(Customer.last_name == "Brookins").all()[0] == andrew