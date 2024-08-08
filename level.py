class LevelCalculator:
    def __init__(self, start_level, blocks, levels_xp):
        self.start_level = start_level
        self.blocks = blocks
        self.levels_xp = levels_xp

    def get_level(self):
        return self.start_level

    def get_planned_level(self):
        start_level = self.get_level()
        planned_xp = sum(block.get('planned_xp', 0) for block in self.blocks)

        level_down = int(start_level)
        level_up = level_down + 1
        level_xp_total = self.levels_xp[level_up] - self.levels_xp[level_down]
        current_xp = self.levels_xp[level_down] + (level_xp_total * (start_level - level_down))

        final_xp = current_xp + planned_xp

        for i, xp in enumerate(self.levels_xp):
            if xp > final_xp:
                break

        max_xp = self.levels_xp[i] - self.levels_xp[i - 1]
        final_xp -= self.levels_xp[i - 1]

        return i - 1 + (final_xp / max_xp)

# Example usage:
exp = 42000
exp = exp * 1.25  # 25% bonus
# exp = 52500
exp += exp * 0.042  # 4.2% bonus
blocks = [{f'planned_xp': exp}]
levels_xp = [ 0, 462, 2688, 5885, 11777, 29217, 46255, 63559, 74340, 85483, 95000, 105630, 
	        124446, 145782, 169932, 197316, 228354, 263508, 303366, 348516, 399672, 457632, 
	        523320, 597786, 682164, 777756, 886074, 1008798, 1147902, 1305486, 1484070 ]
start_level = 11.28

calculator = LevelCalculator(start_level, blocks, levels_xp)
planned_level = calculator.get_planned_level()

print(f"XP is : {exp}")
print(f"Current Level: {start_level}")
print(f"Planned Level: {planned_level}")
