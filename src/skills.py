"""Step 3: skill extraction using a dictionary + aliases."""
import json
import re


def load_skill_config(path="data/skills.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def find_skills(clean, skill_list, aliases):
    found = []
    for skill in skill_list:
        names = [skill] + aliases.get(skill, [])
        for name in names:
            if re.search(r"(?<![a-z0-9])" + re.escape(name) + r"(?![a-z0-9])", clean):
                found.append(skill)
                break
    return found


def find_years_of_experience(clean):
    """Largest 'N years' number mentioned (simple heuristic)."""
    nums = [float(n) for n in re.findall(r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)", clean)]
    return max(nums) if nums else 0.0