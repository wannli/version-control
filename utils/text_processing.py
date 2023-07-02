```python
from typing import List, Tuple

def process_text(original_text: str, suggestions: List[Tuple[int, str]]) -> str:
    """
    Process the original text with the given suggestions.

    :param original_text: The original text.
    :param suggestions: A list of suggestions. Each suggestion is a tuple where the first element is the index at which the suggestion should be applied, and the second element is the suggestion text.
    :return: The processed text.
    """
    lines = original_text.split('\n')
    for index, suggestion in suggestions:
        if index < 0 or index >= len(lines):
            continue
        lines[index] = suggestion
    return '\n'.join(lines)
```