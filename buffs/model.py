from dataclasses import dataclass

@dataclass
class Buff:
    name: str
    type: str
    stat: str
    value: float
    duration: int
