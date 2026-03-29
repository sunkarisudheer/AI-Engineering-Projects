import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Translate English to Telugu.

Example:
English: How are you?
Telugu: మీరు ఎలా ఉన్నారు?

Now translate:
English: I am learning AI.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)