The `io_challenge.py` program prompts the user for their name and displays a greeting, as shown in the "Actual I/O" column below. Note that I/O stands for Input/Output.

| Expected I/O                                                                                 | Actual I/O                                   |
|----------------------------------------------------------------------------------------------|----------------------------------------------|
| What is your name: <b>Abel</b><br>Where do you live: <b>France</b><br>Hi Abel from France!   | What is your name: <b>Abel</b><br>Hi Abel!   |
| What is your name: <b>Jelay</b><br>Where do you live: <b>Canada</b><br>Hi Jelay from Canada! | What is your name: <b>Jelay</b><br>Hi Jelay! |

## Code Challenge

Your task is to update the program so that it matches the user interaction shown in the "Expected I/O" column.

### Steps:
1. In addition to asking for the name, modify the code to also prompt for the country and store the response in a separate variable.
2. Update the f-string in the print statement to include both the name and the country.