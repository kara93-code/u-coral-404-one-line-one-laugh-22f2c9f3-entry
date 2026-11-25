# One Line, One Laugh

Entry for the make.fun contest `u-coral-404-one-line-one-laugh-22f2c9f3`
(https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3).

## The entry

> I asked my password manager for a joke — it said ‘incorrect, try again in 30 seconds.’

One original line, 86 characters. The setup promises a joke from a password
manager; the punchline is the password manager answering with its own
error message instead.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It validates the line is
a single line of 1–200 characters before writing, and sets the output file
to mode 0644 so the grader can read it.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
