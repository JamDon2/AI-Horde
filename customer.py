import datetime

from redis_om import (EmbeddedJsonModel, Field, JsonModel, Migrator, HashModel)
from pydantic import PositiveInt
from typing import Optional, List

class Customer(JsonModel):
    first_name: str
    last_name: str = Field(index=True)
    email: str
    join_date: datetime.date
    age: int = Field(index=True)
    bio: str
    liii: list[PositiveInt]
