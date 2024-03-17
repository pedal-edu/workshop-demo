from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Bird:
    name: str
    can_fly: bool
    region: str
    
def first_land_bird(birds: list[Bird]) -> str:
    land_birds = []
    for bird in birds:
        if not bird.can_fly:
            land_birds.append(bird)
    if not land_birds:
        return "Flew the coop"
    return land_birds[0].name


boids = [
    Bird("Zazu", True, "Africa"),
    Bird("Iago", True, "Agrabah"),
    Bird("Opus", False, "Antarctica"),
    Bird("Huey", False, "Duckberg"),
    Bird("Bess", True, "Ga'Hoole")
]

assert_equal(first_land_bird(boids), "Opus")
assert_equal(first_land_bird([boids[0], boids[3]]), "Huey")
assert_equal(first_land_bird([boids[0], boids[4]]), "Flew the coop")