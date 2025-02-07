Comments are included in code to improve readability, explain complex logic, document design decisions, and serve other purposes.

Single-line comments begin with the hash symbol (#) and are typically followed by a single space. They extend to the end of the line.

The file `comments.py` shows examples of single-line comments on lines 1 and 4:
- Line 1 provides a brief description of the code's purpose.
- Line 4 is commented out to prevent 'banana' from being displayed in the output.

```python
# This program displays various fruit as output.

print('apple')
# print('banana')
print('orange')
print('strawberry')
```

### Code Challenge

Click the "Check" button. The test fails because the output excludes 'banana' and includes 'strawberry'.

1. Remove the comment character `# ` on line 4 so that 'banana' is printed.
2. Comment out line 6 (don't delete it) to prevent 'strawberry' from being printed.
3. Click the "Check" button to confirm the code is correct.