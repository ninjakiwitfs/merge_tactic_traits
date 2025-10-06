import itertools
from collections import defaultdict

OUTPUT_FILE_NAME = "./mergeTacticMixed.txt"
# tier scoring system
# setting tiers to [1,1,X] gives only 6 tier 1s
# setting tiers to [1,3,X] gives mix of 6 tier 1s and tier 2 + 3 tier 1s
# setting tiers to [1,4,X] gives only tier 2 + 3 tier 1s
TIER_SCORES = [1, 3, 9]  # 1st, 2nd, 3rd
NUM_CHARACTERS = 6

# Origin
NOBLE, GOBLIN, CLAN, UNDEAD, FIRE, ACE, ELECTRIC = (
    "noble",
    "goblin",
    "clan",
    "undead",
    "fire",
    "ace",
    "electric",
)

# Roles
JUGGERNAUT, ASSASSIN, RANGER, BLASTER, BRAWLER, MAGE, AVENGER = (
    "juggernaut",
    "assassin",
    "ranger",
    "blaster",
    "brawler",
    "mage",
    "avenger",
)

LEVELS = {
    ELECTRIC: [2],
    FIRE: [2],
    MAGE: [2],
    BLASTER: [2, 4],
    ACE: [2, 4],
    ASSASSIN: [2, 4],
    AVENGER: [2, 4],
    BRAWLER: [2, 4],
    CLAN: [2, 4],
    JUGGERNAUT: [2, 4],
    NOBLE: [2, 4, 6],
    RANGER: [2, 4],
    UNDEAD: [2, 4, 6],
    GOBLIN: [2, 4],
}

CHARACTERS = {
    "knight": [NOBLE, JUGGERNAUT],
    "archer": [CLAN, RANGER],
    "goblins": [GOBLIN, ASSASSIN],
    "spear_gobs": [GOBLIN, BLASTER],
    "barbarians": [CLAN, BRAWLER],
    "skele_drag": [UNDEAD, RANGER],
    "wizard": [FIRE, MAGE],
    "musketeer": [NOBLE, BLASTER],
    "valkyrie": [CLAN, JUGGERNAUT],
    "pekka": [ACE, AVENGER],
    "prince": [NOBLE, BRAWLER],
    "giant_skele": [UNDEAD, BRAWLER],
    "dart_goblin": [GOBLIN, RANGER],
    "elec_giant": [ELECTRIC, AVENGER],
    "executioner": [ACE, BLASTER],
    "witch": [UNDEAD, AVENGER],
    "baby_dragon": [FIRE, BLASTER],
    "princess": [NOBLE, RANGER],
    "e_wizard": [ELECTRIC, MAGE],
    "mega_knight": [ACE, BRAWLER],
    "royal_ghost": [UNDEAD, ASSASSIN],
    "bandit": [ACE, ASSASSIN],
    "gob_machine": [GOBLIN, JUGGERNAUT],
    "skele_king": [UNDEAD, JUGGERNAUT],
    "gold_knight": [NOBLE, ASSASSIN],
    "archr_queen": [CLAN, AVENGER],
}


def score_team(team, CHARACTERS, LEVELS) -> tuple[int, list[str]]:
    counts = {}
    for char in team:
        for trait in CHARACTERS[char]:
            counts[trait] = counts.get(trait, 0) + 1

    score = 0
    fulfilled = []

    for trait, cnt in counts.items():
        thresholds = LEVELS[trait]
        tiers = 0
        for threshold in thresholds:
            if cnt >= threshold:
                tiers += 1

        if tiers > 0:
            # add weighted score
            score += TIER_SCORES[tiers - 1]
            # record fulfilled tiers for printing
            if len(thresholds) == 1:
                fulfilled.append((1, trait))
            else:
                fulfilled.append((tiers, f"{trait} {tiers}"))
    fulfilled.sort(reverse=True)
    fulfilled = [f[1] for f in fulfilled]
    return score, fulfilled


# Example: test one team
team = ("giant_skele", "prince", "princess", "dart_goblin", "skele_drag", "archer")
score, fulfilled = score_team(team, CHARACTERS, LEVELS)
team = ",".join(f"{char:>12}" for char in team)
fulfilled = ",".join(f"{trait:>12}" for trait in fulfilled)
print(f"test team: {score=}")
print(f"{team},->,{fulfilled}")
print("=" * 150)


all_chars = list(CHARACTERS.keys())
best_teams = []
curr_score = 0
num_traits = 0
counter = defaultdict(int)

for combo in itertools.combinations(all_chars, NUM_CHARACTERS):
    s, fulfilled = score_team(combo, CHARACTERS, LEVELS)
    if s > curr_score:
        best_teams.clear()
        curr_score = s
        best_teams.append((s, combo, fulfilled))
        num_traits = len(fulfilled)
    elif s == curr_score:
        num_traits = max(num_traits, len(fulfilled))
        best_teams.append((s, combo, fulfilled))

# Print all tied top teams
with open(OUTPUT_FILE_NAME, "w") as f:
    header_left = [f"{"troop" + str(i+1):>12}" for i in range(NUM_CHARACTERS)]
    header_right = [f"{"trait" + str(i+1):>12}" for i in range(num_traits)]
    header = f"{",".join(header_left)},->,{",".join(header_right)}"
    f.write(header + "\n")
    for score, team, fulfilled in best_teams:
        for char in team:
            counter[char] += 1
        while len(fulfilled)<num_traits:
            fulfilled.append("NULL")
        team = ",".join(f"{char:>12}" for char in team)
        fulfilled = ",".join(f"{trait:>12}" for trait in fulfilled)
        f.write(f"{team},->,{fulfilled}\n")
    print(f"best score: {score}")
    ranking = sorted([(counter[char], char) for char in counter], reverse=True)
    for score, char in ranking:
        print(f"{char:>12}: {score}")
    print("finished")
