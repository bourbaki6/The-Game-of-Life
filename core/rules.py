#---canonical rules---#

class Rules:

    @staticmethod
    def life_rule(cell: int, neighbour: int) -> int:

        if cell == 1 and neighbour in (2, 3):
            return 1

        if cell == 0 and neighbour == 3:
            return 1

        return 0

