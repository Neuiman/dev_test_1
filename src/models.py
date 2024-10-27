import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, TIMESTAMP

from src.database import Base


class Ticker(Base):

    id: Mapped[int] = mapped_column(primary_key=True, default=uuid.uuid4())
    ticker: Mapped[str]
    price: Mapped[float]
    time: Mapped[int]










