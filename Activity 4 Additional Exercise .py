from collections import defaultdict, Counter, deque

# --- GLOBAL INPUTS ---
CONTROL_NUM = 9
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "BEN&BEN"
LOCAL_HAZARD = "FLOOD"

# ==========================================
# EXERCISE 1: UNIVERSITY ADMISSIONS
# ==========================================
print("\n--- EXERCISE 1 OUTPUT ---")
stream = [
    ("TUP MANILA", "BSECE"),
    ("TUP TAGUIG", f"BSME_V{CONTROL_NUM}"),
    ("TUP MANILA", f"BSME_V{CONTROL_NUM}"),
    ("TUP MANILA", "BSECE"),
    ("TUP VISAYAS", STUDENT_MAJOR),
    ("TUP TAGUIG", "BSECE"),
    ("TUP MANILA", "BSECE")
]

# Data Expansion: Add 12 (9+3) custom tuples
for i in range(12):
    stream.append(("TUP MANILA", "BSME" if i % 2 == 0 else "BSECE"))

campus_aggregator = defaultdict(list)
for campus, program in stream:
    campus_aggregator[campus].append(program)

manila_counter = Counter(campus_aggregator["TUP MANILA"])
top_program, freq = manila_counter.most_common(1)[0]

print(f"Total Stream Length: {len(stream)}")
print(f"Top Program (Manila): {top_program} (Freq: {freq})")


# ==========================================
# EXERCISE 2: JACCARD SIMILARITY
# ==========================================
print("\n--- EXERCISE 2 OUTPUT ---")
festival = {"BEN&BEN", "SB19", "BINI", "ERASERHEADS", FAVORITE_ARTIST, "ZILD", f"INDIE ARTIST {CONTROL_NUM}"}
user_a = {"BEN&BEN", "BINI", "MAKI", "DIONELA", FAVORITE_ARTIST}

# Data Expansion: Add 9 new artists
festival.update({f"OPM_STAR_{i}" for i in range(CONTROL_NUM)})

intersection = user_a.intersection(festival)
union = user_a.union(festival)
jaccard = (len(intersection) / len(union)) * 100
dealbreakers = user_a.difference(festival)

print(f"Jaccard Similarity: {jaccard:.2f}%")
print(f"User A Dealbreakers: {dealbreakers}")


# ==========================================
# EXERCISE 3: SLIDING WINDOW FILTER
# ==========================================
print("\n--- EXERCISE 3 OUTPUT ---")
rolling_buffer = deque(maxlen=5)
burst = [(CONTROL_NUM + i, "WEATHER" if i % 2 == 0 else "TRAFFIC") for i in range(7)]
burst[4] = (CONTROL_NUM + 4, LOCAL_HAZARD)

# Data Expansion: Add 11 (9+2) custom alerts
for i in range(7, 18):
    burst.append((CONTROL_NUM + i, "SYSTEM"))

for timestamp, category in burst:
    current_categories = [item[1] for item in rolling_buffer]
    counts = Counter(current_categories)
    
    if counts[category] < 2:
        rolling_buffer.append((timestamp, category))

final_sum = sum(item[0] for item in rolling_buffer)
print(f"Final Sum of Timestamps: {final_sum}")
print(f"Final Deque: {list(rolling_buffer)}")
