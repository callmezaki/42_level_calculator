class LevelCalculator:
    def __init__(self, levels_xp):
        self.levels_xp = levels_xp

    def calculate_xp_needed(self, current_level, desired_level):
        if current_level >= desired_level:
            return 0

        # Calculate current XP based on current_level
        current_level_down = int(current_level)
        current_level_up = current_level_down + 1
        current_level_xp_total = self.levels_xp[current_level_up] - self.levels_xp[current_level_down]
        current_xp = self.levels_xp[current_level_down] + (current_level_xp_total * (current_level - current_level_down))

        # Calculate the XP required to reach the desired level
        desired_level_down = int(desired_level)
        desired_level_up = desired_level_down + 1
        desired_level_xp_total = self.levels_xp[desired_level_up] - self.levels_xp[desired_level_down]
        desired_xp = self.levels_xp[desired_level_down] + (desired_level_xp_total * (desired_level - desired_level_down))

        xp_needed = desired_xp - current_xp
        return xp_needed

# Example usage:
levels_xp = [
    0, 462, 2688, 5885, 11777, 29217, 46255, 63559, 74340, 85483, 
    95000, 105630, 124446, 145782, 169932, 197316, 228354, 263508, 
    303366, 348516, 399672, 457632, 523320, 597786, 682164, 777756, 
    886074, 1008798, 1147902, 1305486, 1484070
]

calculator = LevelCalculator(levels_xp)
current_level = 11.23
desired_level = 14.13

xp_needed = calculator.calculate_xp_needed(current_level, desired_level)

print(f"XP needed to reach level {desired_level} from level {current_level}: {xp_needed}")
