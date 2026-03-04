def parse_list(s: str):
    try:
        return [float(x.strip()) for x in s.split(",") if x.strip() != ""]
    except:
        return []

def weighted_average(grades, weights=None):
    if not grades:
        return None
    if weights and len(weights) == len(grades):
        tot = sum(weights)
        if tot == 0:
            return None
        return sum(g * w for g, w in zip(grades, weights)) / tot
    return sum(grades) / len(grades)

def grade_label(avg):
    if avg is None:
        return ""
    if avg >= 5.5:
        return "Sehr gut"
    if avg >= 5.0:
        return "Gut"
    if avg >= 4.5:
        return "Befriedigend"
    if avg >= 4.0:
        return "Genügend (Bestanden)"
    return "Ungenügend (Nicht bestanden)"