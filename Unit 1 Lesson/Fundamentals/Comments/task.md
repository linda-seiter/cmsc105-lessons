Comments are placed in code for several reasons:

1. **Improve Readability**: Helps others (and yourself) understand the code quickly.
2. **Explain Complex Logic**: Clarifies difficult parts of the code.
3. **Document Code**: Provides code context, purpose, or usage.
4. **Aide in Debugging**: Allows temporarily disabling parts of code without deleting them.
5. **Facilitate Collaboration**: Makes it easier for team members to understand each other's work.
6. **Track TODOs and Fixes**: Notes areas that need improvement or further work. 

## Single-line comments

Single-line comments start with the hash character (#) and are usually followed by a single space, 
and they extend to the end of the physical line. Comments should be complete sentences and the first word should 
be capitalized. 

```python
print('Hello, World!')    # The print function is called, but everything after # is ignored.
```




## CHALLENGE:

Run the code in `comments.py`.  The print function is called twice,
producing two lines of output.

```text
This should appear in the output.
This should not appear in the output.
```

Click the "Check" button below, which will test the output produced by the code.
Note the test fail because only one line of output is expected.

1. Comment out the print statement on line 5 (don't delete it) by adding a hash character `#` and space at the beginning of the line.
2. Click the  "Check" button again to confirm the code is correct