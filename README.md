# Password Strength Calculator

Script asks you to enter a password and then proceeds to rate strength of the password on a scale from 1 to 10.

## Usage example
```
> python password_strength.py
Enter a password: hello
Password strength: 1

> python password_strength.py
Enter a password: asdHU^9806sd
Password strength: 10
```

## Strength estimation

Script estimates password strength based on it's length and the characters it contains.

### Password length

Long password get more points than short ones:
- less than 7 characters - 1 point,
- 7-10 characters - 2 points,
- more than 10 characters - 4 points.

### Requirements

Passwords get additional 2 points for meeting each of the following requirements:
- password contains both uppercase and lowercase characters,
- contains both letters and digits,
- contains any of special characters !@#$%^&*

### Prohibited passwords

If password looks like a date of car licence plate it gets 1 point.

Additionally, you can pass to script a textfile with a list of common passwords. Every password from this list will get 1 point:
```
> python password_strength.py blacklist.txt
Enter a password: password
Password strength: 1
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
