import array
from collections import deque, defaultdict

# PHASE 2: SYSTEM CONFIGURATION (Task 4)
sys_config = {
    "operator": "SAAD",
    "auth_id": "TUPM-25-0679",
    "base_seed": 9,
    "checksum": 29, 
    "vector_dim": 4, 
    "status": "INITIALIZED"
}

# PHASE 3: LISTS (Task 5 & 6)
base_val = sys_config["base_seed"]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]
number_sequence.append(base_val + 20)
# Sequential Operations
new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]
number_sequence.extend(new_numbers)
base_count = number_sequence.count(base_val)
number_sequence.sort()

# PHASE 4: TUPLES & DICTIONARIES (Task 7 & 8)
fixed_coordinates = (sys_config["vector_dim"], sys_config["base_seed"], 0)
data_payload = {
    "identifier": sys_config["auth_id"],
    "dimension": sys_config["vector_dim"],
    "status": "active"
}
data_payload["efficiency_rating"] = 98.5

# PHASE 5: SETS (Task 9 & 10)
raw_data = [base_val, base_val + 5, base_val, sys_config["vector_dim"], base_val + 5]
unique_data = set(raw_data)
reference_set = {base_val, base_val + 10, base_val + 20}
common_elements = unique_data.intersection(reference_set)
combined_elements = unique_data.union(reference_set)

# PHASE 6: ARRAYS & COMPREHENSIONS (Task 11 & 12)
# Task 11 will show error if string appended; code below skips error for table
number_array = array.array('i', [sys_config["base_seed"], sys_config["vector_dim"], 100])
generated_list = [(x * base_val) for x in range(1, 6)]
filtered_list = [x for x in generated_list if x > 15]

# PHASE 7: SPECIALIZED COLLECTIONS (Task 13 & 14)
data_queue = deque([sys_config["base_seed"], sys_config["vector_dim"]])
data_queue.append(100)
data_queue.appendleft(200)
default_data = defaultdict(int)
default_data['active_key'] = sys_config["vector_dim"]

# --- DISPLAYING OUTPUTS FOR TABLE ---
print(f"Part 1: Seed: {sys_config['base_seed']}, Checksum: {sys_config['checksum']}")
print(f"Part 2: Initial: {number_sequence[:3]}, After Append: {number_sequence[:4]}")
print(f"Part 3: Occurrences: {base_count}, Sorted: {number_sequence}")
print(f"Part 4: Unpacked: {fixed_coordinates}")
print(f"Part 5: Initial ID: {data_payload['identifier']}, Updated: {data_payload}")
print(f"Part 6: Raw: {raw_data}, Unique: {unique_data}")
print(f"Part 7: Intersection: {common_elements}, Union: {combined_elements}")
print(f"Part 8: Array: {number_array}")
print(f"Part 9: Generated: {generated_list}, Filtered: {filtered_list}")
print(f"Part 10: Deque after appends: {data_queue}")
print(f"Part 11: Missing Key Value: {default_data['unknown_key']}")
