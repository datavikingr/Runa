#!python3

import json

letter_swap = {
'ǫ': 'ᛅ',
'v': 'ᚢ',
'œ': 'ᚢ',
'ᚯ': 'ᚬ'
}
# Note: ᚯ is found in both medieval  and dalrune inventories, but not that of the younger futhark. ᚬ is the letter we're looking for. So that's fun.

with open('letterswap.json', 'w') as f:
    json.dump(letter_swap, f)
