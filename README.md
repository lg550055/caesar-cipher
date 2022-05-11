# LAB - Class 18

## Project: Caesar Cipher

### Author: Polo Gonzalez

### Functions

- **encrypt**
  - ***arguments***: text phrase, numeric shift
  - ***return:*** 'text phrase' shifted 'numeric shift' letters.
  - Examples
    - encrypt(‘abc’,1) returns ‘bcd’
    - encrypt(‘abc’, 10) returns ‘klm’
    - encrypt(‘abc’,27) returns ‘bcd’
    - encrypt(‘zzz’,1) returns ‘aaa’

- **decrypt**
  - ***arguments***: encrypted text, numeric shift
  - ***return:*** encrypted text back to its original form when correct key is supplied

- **crack**
  - ***arguments***: encrypted text
  - ***return:*** encrypted text back to its original form
  - decode the ciphers without access to the key
  - uses an english list of words to determine if its likely it has been able to identify the original message

### Tests

- encrypt a string with a given shift
- decrypt a previously encrypted string with the same shift
- encryption should handle upper and lower case letters
- encryption should allow non-alpha characters (including white space) but ignore them
- decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used

Use 'pytest' to run unit tests

---
