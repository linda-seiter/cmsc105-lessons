#from bakery import assert_equal
from unittest import TestCase as tc


def take_until_trees(beds: list[str]) -> list[str]:
    taking = True
    result = []
    for bed in beds:
        if '🌳' in bed:
            # Inverted True/False
            taking = False
        elif taking:
            result.append(bed)
    return result

# Test the method
bed1 = "🌹🌹"
my_garden=["🌹🌹", "🌷🌷", "🌳", "🌻🌻🌻"]
print(my_garden[0])
rose=my_garden[0][0]
print(type(rose))
tc().assertEqual(take_until_trees(my_garden), my_garden[0:2], "Tree is 3rd element in list")


def remove_seedlings(beds: list[str]) -> list[str]:
    result = []
    for bed in beds:
        # Inverted not
        if '🌱' not in bed:
            result.append(bed)
    return result

# assert_equal(remove_seedlings(["🌹", "🌱🌱", "🌷","🌼🌼","🌱🌱🌱","🌳","🌻🌻🌻"]), ["🌹", "🌷","🌼🌼","🌳","🌻🌻🌻"])
# assert_equal(remove_seedlings(["🌱🌱,🌱🌱🌱","🌳","🌸","🌺🌺🌺🌺"]), ["🌳","🌸","🌺🌺🌺🌺"])
# assert_equal(remove_seedlings([]), [])
# assert_equal(remove_seedlings(["🌱🌱"]), [])

def max_bed(beds: list[str]) -> str:
    most_popular = beds[0]
    for bed in beds:
        # Getting minimum instead of maximum
        if len(bed) > len(most_popular):
            most_popular = bed
    return most_popular

# assert_equal(max_bed(["🌹🌹","🌷🌷","🌻🌻🌻","🌸"]), "🌻🌻🌻")
# assert_equal(max_bed(["🌹🌹","🌷🌷","🌼🌼🌼","🌸","🌺🌺🌺🌺","🌻🌻🌻"]), "🌺🌺🌺🌺")
# assert_equal(max_bed(["🌹🌹","🌷🌷","🌼🌼🌼","🌱🌱🌱🌱🌱","🌳","🌸","🌺🌺🌺🌺","🌻🌻🌻"]), "🌱🌱🌱🌱🌱")
# assert_equal(max_bed(["🌺🌺🌺🌺", "🌱🌱","🌱🌱🌱","🌳","🌸"]), "🌺🌺🌺🌺")
# assert_equal(max_bed(["🌱🌱"]), "🌱🌱")

def biggest_bed(garden: str) -> str:
    # Wrong guard
    if not garden:
        return "no flowers"
    flower_beds = garden.split(',')
    flower_beds = take_until_trees(flower_beds)
    flower_beds = remove_seedlings(flower_beds)
    if not flower_beds:
        return 'no flowers'
    return max_bed(flower_beds)

# assert_equal(biggest_bed("🌹🌹,🌷🌷,🌻🌻🌻,🌸"), "🌻🌻🌻")
# assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌺🌺🌺🌺")
# assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌱🌱🌱🌱🌱,🌳,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌼🌼🌼")
# assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌳,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌼🌼🌼")
# assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌱🌱🌱🌱🌱,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌺🌺🌺🌺")
# assert_equal(biggest_bed("🌱🌱,🌱🌱🌱,🌳,🌸,🌺🌺🌺🌺"), "no flowers")
# assert_equal(biggest_bed("🌳,🌸,🌺🌺🌺🌺"), "no flowers")
# assert_equal(biggest_bed(""), "no flowers")
# assert_equal(biggest_bed("🌳🌳🌳"), "no flowers")
# assert_equal(biggest_bed("🌱🌱"), "no flowers")