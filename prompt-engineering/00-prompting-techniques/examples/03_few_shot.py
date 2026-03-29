import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Correct the sentence.

Example 1:
Input: She go to office.
Output: She goes to the office.

Example 2:
Input: They is playing.
Output: They are playing.

Example 3:
Input: He eat food.
Output: He eats food.

Now correct:
Input: We was happy.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)