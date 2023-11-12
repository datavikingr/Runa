#!python3

import json

letter_swap = {
'sh': 'ᛲ',
'Sh': 'ᛲ',
'SH': 'ᛲ',
'oo': 'ᛳ',
'Oo': 'ᛳ',
'OO': 'ᛳ',
'st': 'ᛥ',
'St': 'ᛥ',
'ST': 'ᛥ',
'ea': 'ᛠ',
'Ea': 'ᛠ',
'EA': 'ᛠ',
'ae': 'ᚫ',
'Ae': 'ᚫ',
'AE': 'ᚫ',
'æ': 'ᚫ',
'Æ': 'ᚫ',
'oe': 'ᛟ',
'Oe': 'ᛟ',
'OE': 'ᛟ',
'œ': 'ᛟ',
'Œ': 'ᛟ',
'ng': 'ᛝ',
'Ng': 'ᛝ',
'NG': 'ᛝ',
'th': 'ᚦ',
'Th': 'ᚦ',
'TH': 'ᚦ'
}
# Note: ᚯ is found in both medieval  and dalrune inventories, but not that of the younger futhark. ᚬ is the letter we're looking for. So that's fun.

with open('asfdoubleswap.json', 'w') as f:
    json.dump(letter_swap, f)
