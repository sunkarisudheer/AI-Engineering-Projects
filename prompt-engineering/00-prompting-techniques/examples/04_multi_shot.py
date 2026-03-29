import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Classify the category.

Example 1:
Text: The stock market is rising today.
Category: Finance

Example 2:
Text: The team won the cricket match.
Category: Sports

Example 3:
Text: New AI model released by OpenAI.
Category: Technology

Example 4:
Text: The government passed a new law.
Category: Politics

Now classify:
Text: Bitcoin price hits a new high.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)