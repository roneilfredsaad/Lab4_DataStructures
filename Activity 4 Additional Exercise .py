from collections import defaultdict, Counter

# --- Required Inputs ---
CONTROL_NUM = 9
STUDENT_MAJOR = "BSME"

# --- Logic: Initialize Stream ---
stream = [
    ("TUP MANILA", "BSECE"),
    ("TUP TAGUIG", f"BSME_V{CONTROL_NUM}"),
    ("TUP MANILA", f"BSME_V{CONTROL_NUM}"),
    ("TUP MANILA", "BSECE"),
    ("TUP VISAYAS", STUDENT_MAJOR),
    ("TUP TAGUIG", "BSECE"),
    ("TUP MANILA", "BSECE")
]

# --- Data Expansion ---
# Adding exactly (9 + 3) = 12 custom application tuples
custom_data = [
    ("TUP MANILA", "BSME"), ("TUP MANILA", "BSECE"),
    ("TUP MANILA", "BSME"), ("TUP MANILA", "BSME"),
    ("TUP TAGUIG", "BSECE"), ("TUP VISAYAS", "BSME"),
    ("TUP MANILA", "BSME"), ("TUP MANILA", "BSME"),
    ("TUP MANILA", "BSME"), ("TUP MANILA", "BSME"),
    ("TUP MANILA", "BSME"), ("TUP MANILA", "BSME")
]
[span_3](start_span)stream.extend(custom_data) #[span_3](end_span)

# --- Algorithm Phase 1: Aggregation ---
campus_aggregator = defaultdict(list)
for campus, program in stream:
    [span_4](start_span)campus_aggregator[campus].append(program) #[span_4](end_span)

# --- Algorithm Phase 2: Frequency Analysis ---
[span_5](start_span)manila_counter = Counter(campus_aggregator["TUP MANILA"]) #[span_5](end_span)
[span_6](start_span)top_program, frequency = manila_counter.most_common(1)[0] #[span_6](end_span)

# --- Required Outputs ---
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"STUDENT_MAJOR Used: {STUDENT_MAJOR}")
print(f"Expanded Stream Length: {len(stream)}")
print(f"Total Applications for TUP Manila: {len(campus_aggregator['TUP MANILA'])}")
print(f"Top Requested Program at TUP Manila: {top_program}")
print(f"Exact Frequency of Top Program: {frequency}")
