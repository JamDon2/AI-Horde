import datetime

from redis_om import JsonModel


class Customer(JsonModel):
    first_name: str
    last_name: str
    email: str
    join_date: datetime.date
    age: int
    bio: str
    # liii: list


andrew = Customer(
    first_name="Andrew",
    last_name="Brookins",
    email="andrew.brookins@example.com",
    join_date=datetime.date.today(),
    age=38,
    bio="Python developer, works at Redis, Inc.",
    # liii=[1,2,3,4,5]
)

bob = Customer(
    first_name="Bob",
    last_name="Brookins",
    email="bob.brookins@example.com",
    join_date=datetime.date.today(),
    age=32,
    bio="Python PR, works at Redis, Inc.",
    # liii=[1,2,3,4,5]
)

andrew.save()
bob.save()
print(andrew.key())


assert Customer.get(andrew.pk) == andrew