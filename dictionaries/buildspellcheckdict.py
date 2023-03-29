 #!python3

import json

spell_check = {
'ᚢᚴ': 'ᛅᚢᚴ',
'ᛅᚴ': 'ᛁᚴ',
'ᚴᛅᚦ': 'ᚴᛁᚦ',
'ᚴᚬᛘᛦ': 'ᚴᚢᛘᛦ',
'ᚴᛁᚠᛁᛏᚱ': 'ᚴᛁᚠᛁᛏᛦ',
'ᚴᛁᛋᛏᚱ': 'ᚴᛁᛋᛏᛦ',
'ᛒᚱᛅᚦᚱ': 'ᛒᚱᛅᚦᛦ',
'ᛁᛏᚱᚦᛅᚴᚢ': 'ᛁᛏᛦᚦᛅᚴᚢ',
'ᚢᛁᚱᚦᚱ': 'ᚢᛁᚱᚦᛦ',
'ᛋᛁᛏᚱ': 'ᛋᛁᛏᛦ',
'ᛘᛅᚦᚱ': 'ᛘᛅᚦᛦ',
'ᚼᛁᛚᛏᚱ': 'ᚼᛁᛚᛏᛦ',
'ᚼᚢᛁᚱ': 'ᚼᚢᛁᛦ',
'ᚴᛁᛏᚱ': 'ᚴᛁᛏᛦ',
'ᛒᛅᛏᚱᛁ': 'ᛒᛅᛏᛦᛁ',
'ᛒᛁᛏᚱᛅ': 'ᛒᛁᛏᛦᛅ',
'ᚢᛁᚱᛅ': 'ᚢᛁᛦᛅ',
'ᚢᛁᚴᚱᛅ': 'ᚢᛁᚴᛦᛅ',
'ᚠᚢᚱᛅ': 'ᚠᛅᛦᛅ',
'ᚠᛚᛅᛁᚱ': 'ᚠᛚᛅᛁᛦᛅ',
'ᚠᛁᛅᛏᚱᛅᚦᚱ': 'ᚠᛁᛅᛏᚱᛅᚦᛦ',
'ᚴᛚᛅᚦᚱ': 'ᚴᛚᛅᚦᛦ',
'ᚴᛅᛁᚱᛅᚱ': 'ᚴᛅᛁᚱᛅᛦ',
'ᚴᛁᚱᛁ': 'ᚴᛅᛦᛁ',
'ᚠᚢᛦ': 'ᚠᚬᛦ',
'ᚦᛅ': 'ᚦᚬ',
'ᚾᛅᛏᚱ': 'ᚾᚬᛏᛦ',
'ᛘᚢᚦᚱ': 'ᛘᚢᚦᛦ',
'ᛋᚢᛘ': 'ᛋᛁᛘ',
'ᚠᚢᚱᛘᛅᛚᛁᛏᚱ': 'ᚠᚢᚱᛘᚬᛚᛁᛏᛦ',
'ᛘᛅᛚᛁ': 'ᛘᚬᛚᛁ',
'ᚠᚱᚢᚦᚱ': 'ᚠᚱᚢᚦᛦ',
'ᛘᛅᛚᛁᛦ': 'ᛘᚬᛚᛁᛦ',
'ᚼᚱᛅᚦᛘᛅᛚᛏ': 'ᚼᚱᛅᚦᛘᚬᛚᛏ',
'ᚼᛅᛚᛏᛁᛏᚱ': 'ᚼᛅᛚᛏᛁᛏᛦ',
'ᚠᛚᚢᛏᛅ': 'ᚠᛚᛅᛏᛅ',
'ᛁᚱᚢᛋᚴ': 'ᛁᛦᚢᛋᚴ',
'ᛚᛅᛏᚱ': 'ᛚᛅᛏᛦ',
'ᛚᛅᛁᚦᚱ': 'ᛚᛅᛁᚦᛦ',
'ᛏᚢᛅᚱ': 'ᛏᚢᛅᛦ',
'ᛘᛅᛚ': 'ᛘᚬᛚ',
'ᚠᚱᛅᛘᛅᚱ': 'ᚠᚱᛅᛘᛅᛦ',
'ᚾᛅᛦ': 'ᚾᚬᛦ',
'ᛘᛅᛏᛅᚱᚴᚢᚦᛅᚾ': 'ᛘᛅᛏᛅᛦ᛫ᚴᚢᚦᛅᚾ',
'ᛘᛅᛏᛅᚱ': 'ᛘᛅᛏᛅᛦ',
'ᚢᛅᚱᛁ': 'ᚢᛅᛦᛁ',
'ᛋᚢᚾᛋᚴ': 'ᛋᚢᚾᛋᛏ',
'ᚢᛁᚦᚱᚴᛁᚠᛁᛏᚱ': 'ᚢᛁᚦᛦᚴᛁᚠᛁᛏᛦ',
'ᛁᛏᚱᚴᛁᚠᛁᛏᚱ': 'ᛁᛏᛦᚴᛁᚠᛁᛏᛦ',
'ᛁᚱᚢᛋᚴ': 'ᛁᛦᚢᛋᚴ',
'ᛒᛁᚦᚱ': 'ᛒᛁᚦᛦ',
'ᚴᛅᚦᛁ': 'ᚴᛁᚦᛁ',
'ᚦᛁᚱ': 'ᚦᛁᛦ',
'ᛅᚴ': 'ᛁᚴ',
'ᛋᛏᛁᛏᚱ': 'ᛋᛏᛅᛏᛦ',
'ᚼᛚᚢᚱᛅᛏ': 'ᚼᛚᚢᛦ᛫ᛅᛏ',
'ᚠᚱᛁᚦᚱ': 'ᚠᚱᛁᚦᛦ',
'ᚬᚱᛚᛅᚴ': 'ᚢᛦᛚᛅᚴ',
'ᛋᚢᚱᚴᛅᛚᛅᚢᛋᛅᛋᛏᚱ': 'ᛋᚢᚱᚴᛅᛚᛅᚢᛋᛅᛋᛏᛦ',
'ᛒᚱᛅᚾ': 'ᛒᚱᛁᚾ',
'ᚢᚾᛋᛏ': 'ᚢᛏᛋ',
'ᚴᚢᚦᚱ': 'ᚴᚢᚦᛦ',
'ᚢᚱᚴᛁᛏᚱ': 'ᚢᚱᚴᛁᛅᛏᛦ',
'ᚾᛅᚠᚱᛅ': 'ᚾᚬᚠᛦᛅ',
'ᚼᛅᛋᛏᛋ': 'ᚼᛁᛋᛏᛋ',
'ᚠᚱᚢᚦᚱᛅ':'ᚠᚱᚢᚦᛦᛅ',
'ᚼᚢᛅᛏᛅᛋᛏᚱ': 'ᚼᚢᛅᛏᛅᛋᛏᛦ',
'ᛘᚢᛏᛁ': 'ᛘᚢᚾᛏᛁ',
'ᛘᛅᛚᚢᚴᛁ': 'ᛘᚬᛚᚢᚴᛁ',
'ᚼᛁᚴᛁ': 'ᚼᚾᚴᛁ',
'ᛁᛚᛏᚱ': 'ᛁᛚᛏᛦ',
'ᚾᛅᛁᛦ': 'ᚾᚬᛁᛦ',
'ᚠᚱᛅᛏᚢᛘ': 'ᚠᚱᚬᛏᚢᛘ',
'ᛁᛚᛁᚠᚦᚢᛘ': 'ᚢᛚᛁᚠᚦᚢᛘ',
'ᛒᚱᛅᚾᛅ': 'ᛒᚱᛁᚾᛅ',
'ᛏᛅᚢᚦᚱ': 'ᛏᛅᚢᚦᛦ',
'ᚼᛅᛚᛏᚱ': 'ᚼᛅᛚᛏᛦ',
'ᚱᛁᚦᚱ': 'ᚱᛁᚦᛦ',
'ᚼᛅᛏᛅᚱᚢᛅᚾᛦ': 'ᚼᛅᛏᛅᛦᚢᛅᚾᛦ',
'ᛒᛚᛁᛏᚱ': 'ᛒᛚᛁᛏᛦ',
'ᛒᚱᛁᚾᛏᚱ': 'ᛒᚱᛁᚾᛏᛦ',
'ᚾᛅᛋ': 'ᚾᚬᛋ',
'ᛁᛒᛏᛁᛦ': 'ᛅᚠᛏᛁᛦ',
'ᛒᛅᚢᛏᛅᚱᛋᛏᛅᛁᚾᛅᛦ': 'ᛒᛅᚢᛏᛅᛦᛋᛏᛅᛁᚾᛅᛦ',
'ᚾᛁᚦᚱ': 'ᚾᛁᚦᛦ',
'ᚼᛅᛏᛅᚱ': 'ᚼᛅᛏᛅᛦ',
'ᚢᛅᚾᛁ': 'ᚢᚬᚾᛁ',
'ᚾᚢᛏ': 'ᚾᚬᛏ',
'ᚼᚢᛅᚱᚠ': 'ᚼᚢᛁᚱᛒ',
'ᛘᛅᚾᛅᚦᛁ': 'ᛘᚬᚾᛅᚦᛁ',
'ᚠᚱᛅᛏᚱ': 'ᚠᚱᚬᛏᛦ',
'ᛅᛚᛏᚱᛅᛁ': 'ᛅᛚᛏᚱᛁ',
'ᚴᚱᛁᛏᚱ': 'ᚴᚱᛁᛏᛦ',
'ᚢᛅᚾᛅᛦ': 'ᚢᚬᚾᛅᛦ',
'ᛅᚢᚦᚱ': 'ᛅᚢᚦᛦ'
}

with open('spellcheck.json', 'w') as f:
    json.dump(spell_check, f)

#################################################
# IGNORE : ᚢᚢᛁᛋᛏ - unless he has a specific inscription that I'm not aware of, he should know better then doubles
# IGNORE : ᛒᛁᛏᚱᛅ / ᛒᛅᛏᚱᛅ; I'd go with ᛁ here, personally, both appear valid
# IGNORE : ᛁᚱ / ᛁᛋ; it's what the text says
# IGNORE : ᚢᛒ
# IGNORE : ᚢᛒᛏ / ᚢᚠᛏ; P's are commonly shown in both B's and F's; maybe dialectal issue?
# IGNORE : ᚴᛚᛁᚦᛁᛅᛋᚴ / ᚴᛚᛅᚦᛁᛅᛋᚴ; I'd go with ᛁ here, personally, both appear valid
# IGNORE : ᚢᛅᚱᛅ / ᚢᛁᛋᛅ; same as ᛁᚱ above
# IGNORE : ᛘᛅᚱᚴᛏ / ᛘᛅᚱᛏ; some versions include the g; and I'm gonna match my text
# IGNORE : ᚬᛦ / ᛅᚱ; both valid, both contained in the inscription corpus
# IGNORE : ᚠᛁᛅᛦ / ᚠᛁᛅᚱ; gonna keep the former for flavor
# IGNORE : ᛋᛁᚠᛦ / ᛋᚢᚠᛦ; 'sefr' I like ᛁ for this
# IGNORE : ᚦᚱᛁᛦ᛫ᚱᚢ / ᚦᚱᛁᛦᚢ; both my other spellings space those the same. Majority takes it. runic.is doesn't recognize Dr. Crawford's, but it jumps at the other spelling. I'm not the expert, he probably literally knows the exception that I'm totally ignorant to. 
# IGNORE: ᛁᛚᛏ / ᛅᛚᛏ; I like the 'e' = ᛁ better. Dr. Crawford's probably right here, though. Other words also use the 'ᛁᛚᛏ' spelling as well, so consistency is nice.
# IGNORE: ᛏᚢᛅᛁᛦ᛫ᚱᚢ / ᛏᚢᛅᛁᛦᚢ; can't do anything on that side of the switch, due to the nature of split delimiter used. Manual TODO.
# IGNORE: ᛋᚴᛅᛘᛅᛦ᛫ᚱᚢ / ᛋᚴᛅᛘᛅᛦᚢ; ; can't do anything on that side of the switch, due to the nature of split delimiter used. Manual TODO.
# IGNORE: ᛅᚾᛅᛦ / ᛅᚾᛅᚱ; still emphasizing ᛦ & ᚬ over their alternatives. I like the flavor.
# IGNORE: ᛒᛅᚱᛅ / ᛒᛁᚱᛅ: I dunno. long A sound as an ᛁ? Really? That's the 'e rune', sure, but like 'sound it out'.
# IGNORE

#################################################
# Stanza 57, line 5 Consensus issue: "af" appears to actually be "at"; Dunno how to fix this programmatically, I think this is is gonna be a manual fix afterwards.
# Stanza 64, top 3 lines; it seems my two sources are the same, or rather one used the other for its source. Vote still counts, though? It's 2 out of 3. Also, I do know Háv Íslenzk fornrit is a valid/authoritative standard to cite. Like, that's a fact. I'll carry on.
# Stanza 70, line 2: Confirmed my three sources are three, unlike my suspicion in the previous commment. Dr. Crawford & Oslo disagree on the spelling of illlifðum/ólifðum. The third source I suspected just matching Oslo on this, in fact matches Dr. Crawford. 2/3, 'ólifðum' takes it. 
