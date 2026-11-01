## Password strength analyzer

A simple python project that checks the strenght of the password etered by the user using a score based evaluation.
The analyzer takes in consideration the password length, the characteres used, the combination of letters and carachters and knows the most common passwords such as "password123".

## Features

- **Length analysis**
- **Uppercase letters**
- **Lowercase letters**
- **Numbers**
- **Special carachters**
- **Common and vastly used passwords**

## Technologies

- **Python 3.14.5**
- **string ('''python import string''')**
- **getpass ('''python import getpass''')**

## Installation

Clone the repository:

'''bash
git clone YOUR_REPOSITORY_URL'''

Navigate to the project directory:

'''bash
cd password-strength-analyzer'''

## Usage

Run the program using:

'''bash
python main.py'''

Enter a password and the analyzer will score it and give you tips to improve the password strength

## Scoring system

| Criteria | Points |
|:---|---:|
| At least 12 carachters | 2 |
| At least 8 carachters | 1 |
| Any uppercase letters | 1 |
| Any lowercase letters | 1 |
| Any numbers | 1 |
| Any special carachters | 1 |

## Ranking

| Ranking | Points |
|:---|---:|
| Weak | 0 - 2 |
| Medium | 2 - 4 |
| Strong | 4 - 6 |

## Limitations

- The project only checks 6 criterias so it isn't absolute
- A strong score doesnt mean an uncrackable password
- The scores and rankings don't estimate actual srength and immunity from attacks

## Future improvements

- Check for repeted carachters
- Have a more complete ranking 
- Give better tips to improve one's password security
- Have more criterias to check and an wider score range