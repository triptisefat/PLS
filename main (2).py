name = "Sefat Ara"

# Concatenation
greeting = "Hello, " + name
print("Concatenation Result:", greeting)

# Substring extraction
substring = name[:5]  # Extracts 'Sefat'
print("Substring Extraction Result:", substring)

# Pattern matching using regex
import re
pattern = r'\bAra\b'
match = re.search(pattern, name)
print("Pattern Matching Result:", match.group() if match else "No match")

# String length
name_length = len(name)
print("String Length Result:", name_length)

# String comparison
other_name = "Sefat Ara"
comparison_result = "Equal" if name == other_name else "Not Equal"
print("Comparison Result:", comparison_result)
