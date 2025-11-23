from dataclasses import dataclass

@dataclass
class DeathRate:
    entity: str
    code: str | None
    year: int | None
    death_rate: float | None
    time: int | None
