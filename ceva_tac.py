import re

# Expresia regulată pentru limbajul din punctul 1.2
regex = r"([a-z]+|[+\-]?([0-9]+|0[bB][01]+|0[xX][0-9a-fA-F]+)|[ \t\r\n]|\/\/[^\r\n\0]*|\(|\)|;|\0)"

# Șir de intrare pentru testare
input_text = """
a1 = 5;
x = (3 + 4) * 10;
0b1010
0x1f
"""

# Căutare a tuturor simbolurilor identificate de expresia regulată
matches = re.findall(regex, input_text)

# Afișarea fiecărei potriviri găsite
for match in matches:
    print(match[0])  # Match-ul principal este în primul element
