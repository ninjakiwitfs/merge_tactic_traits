# Clash Royale Merge Tactics — Best Team Composition Finder

This Python script calculates the **best team compositions** in *Clash Royale: Merge Tactics* based on origin-role synergies and tier bonuses. It evaluates all 6-character combinations to find the ones that yield the **highest synergy score**.

---

## 🧩 Overview

The script systematically goes through every possible team of 6 characters, evaluates their synergy score using defined tier thresholds, and writes the best combinations to a text file.

It uses the synergy logic between **Origins** and **Roles**, assigning scores to teams that meet specific thresholds (tier levels).

---

## ⚙️ How It Works

### 1. **Scoring System**

Each team is scored based on how many synergies they activate.
The following constants define how scoring works:

```python
TIER_SCORES = [1, 4, 9]  # Score weights for tier 1, tier 2, and tier 3
NUM_CHARACTERS = 6        # Team size
```

For example:

* `[1, 1, X]` → only tier 1 synergies are possible.
* `[1, 3, X]` → allows mixed tier 1 and tier 2 synergies.
* `[1, 4, X]` → emphasizes tier 2 synergies.

### 2. **Origins and Roles**

Each character has two attributes: an *Origin* and a *Role*.
When enough team members share the same attribute, a synergy tier is activated.

Example:

```python
"knight": [NOBLE, JUGGERNAUT]
"archer": [CLAN, RANGER]
```

---

## 📊 Output Files

The script writes results to one of three precomputed text files depending on the scoring configuration:

| File                   | Description                       |
| ---------------------- | --------------------------------- |
| `mergeTactic1.txt`     | Only Tier 1 synergies             |
| `mergeTactic2.txt`     | Tier 2 + Tier 1 synergies         |
| `mergeTacticMixed.txt` | Mixed Tier 1 and Tier 2 synergies |

Each line in these files lists:

```
[team of 6 characters] ,->, [synergies activated]
```

Example:

```
      knight,      archer,  barbarians,   musketeer,      prince,    princess,->,     noble 2,    ranger 1,      clan 1,   brawler 1
```

---

## 🚀 How to Run

1. **Install Python 3.10+**
2. **Run the script:**

   ```bash
   python mergeTactic.py
   ```
3. The program prints:

   * The **best synergy score**
   * A **ranking of most frequently used characters** in top teams
4. The full list of top-scoring teams is saved to the output file defined in:

   ```python
   OUTPUT_FILE_NAME = "./mergeTactic2.txt"
   ```

---

## 🧠 Example Console Output

```
test team: score=7
 giant_skele,      prince,    princess, dart_goblin,  skele_drag,      archer,->,    ranger 2,    undead 1,     noble 1,   brawler 1
======================================================================================================================================================
best score: 7
  skele_king: 80
  skele_drag: 80
    princess: 80
      knight: 80
 gold_knight: 79
 giant_skele: 79
 royal_ghost: 76
      prince: 76
...
finished
```

---

## 🛠️ Customize

You can adjust:

* `TIER_SCORES` to weigh tier bonuses differently.
* `NUM_CHARACTERS` for other team sizes.
* `OUTPUT_FILE_NAME` to direct results to another file.
* `CHARACTERS` or `LEVELS` dictionaries to reflect new balance updates.

---

## 📁 File Structure

```
mergeTactic.py          # Main script
mergeTactic1.txt        # Precomputed Tier 1-only results
mergeTactic2.txt        # Precomputed Tier 2 + Tier 1 results
mergeTacticMixed.txt    # Precomputed mixed-tier results
```

---

## 🧩 Notes

* The script uses **combinatorial search** (`itertools.combinations`) to test every possible 6-character team.
* Depending on your hardware, execution time can vary, since there are thousands of combinations.
* Output files can be large if many teams tie for top score.

---
