#---canonical rules + alt rules ---#

class Rules:

    @staticmethod
    def conway(cell: int, n: int) -> int:
        return int((cell and n in (2,3)) or (not cell and n == 3))

    @staticmethod
    def highlife(cell: int, n: int) -> int:
        return int((cell and n in (2,3)) or (not cell and n in (3,6)))

    @staticmethod
    def day_and_night(cell: int, n: int) -> int:
        return int((cell and n in (3,4,6,7,8)) or (not cell and n in (3,6,7,8)))

    @staticmethod
    def morley(cell: int, n: int) -> int:
        return int((cell and n in (2, 4, 5)) or (not cell and n in (3, 6, 8)))
