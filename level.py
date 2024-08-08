
def LevelCalculator(start_level, planned_xp, score, switch_value):
    levels_xp = [ 0, 462, 2688, 5885, 11777, 29217, 46255, 63559, 74340, 85483, 95000, 105630, 
        124446, 145782, 169932, 197316, 228354, 263508, 303366, 348516, 399672, 457632, 
        523320, 597786, 682164, 777756, 886074, 1008798, 1147902, 1305486, 1484070 ]
    
    xp = planned_xp * (score / 100)
    if switch_value == 'on':
        xp += xp * 0.042
    level_down = int(start_level)
    level_up = level_down + 1
    level_xp_total = levels_xp[level_up] - levels_xp[level_down]
    current_xp = levels_xp[level_down] + (level_xp_total * (start_level - level_down))

    final_xp = current_xp + xp

    for i, xp in enumerate(levels_xp):
        if xp > final_xp:
            break

    max_xp = levels_xp[i] - levels_xp[i - 1]
    final_xp -= levels_xp[i - 1]

    return i - 1 + (final_xp / max_xp)

