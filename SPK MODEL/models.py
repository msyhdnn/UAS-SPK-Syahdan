from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class BigBike(Base):
    __tablename__ = "bigbike"

    Nama : Mapped[str] = mapped_column(primary_key=True)
    Harga : Mapped[int]
    cc : Mapped[float]
    full_tank : Mapped[float]
    Daya_KW : Mapped[float]
    Torsi_Max : Mapped[float]

    def __repr__(self) -> str :
        return f"Nama={self.Nama}, Harga={self.Harga}, cc={self.cc}, full_tank={self.full_tank}, Daya_KW={self.Daya_KW}, Torsi_Max={self.Torsi_Max}"

