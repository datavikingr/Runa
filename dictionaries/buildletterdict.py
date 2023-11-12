#!python3

import json

letter_swap = {
'v': 'ᚢ',
'z': 'ᛦ',
'ǫ': 'ᛅ',
'œ': 'ᚢ',
'ᚯ': 'ᚬ'
}
# Note: ᚯ is found in both medieval  and dalrune inventories, but not that of the younger futhark. ᚬ is the letter we're looking for. So that's fun.

with open('yf_letterswap.json', 'w') as f:
    json.dump(letter_swap, f)
