# Runa and the Visabok Project

The goal of this project, very simply, is to put Heathens (American) and Asatru (European) back in control of our own culture and lore. I think an appropriate place to start is rebuilding the stories we have left: we need to see them in our own letters at the absolute minimum.

So this project aims to convert Old Norse (ON), Old Icelandic (OI), and Old English (OE) ancient texts into their respective runic script. Younger Futhark (YF) for ON/OI texts, Anglo-Saxon Futhorc (ASF) for the OE texts. The desired end product is a multi-volume set containing ON-YF, ON-Latin alphabet (Lat), modern English (EN), and EN-ASF transliteration versions of our stories, myths, and lore for proper publishing. Or the applicable/appropriate languages, you get the idea.

Basically, I mean to do some of our proverbial 'homework' for us, the way I always wished we had 'em when I was still a neophyte. Personally, I feel it's time to stop playing in the dust. We need to consolidate what we have and start looking forward and building. Code, data, and writing are my primary skill sets, so this is what I'm bringing to the table.

# Technical Stuff

## Dependencies for the scripts

Python (Python3 if you're on Debian like I am), Chrome, Selenium. I'm running this on Debian, so use apt (and deb-get, or manually install Chrome from their website). The required Python libraries are as follows: BeautifulSoup, Selenium, webdriver_manager, and json. Grab them with pip. 

I can't help troubleshoot Selenium. My own grasp is tenuous, and this is held together by shoestrings already.

# Cultural Stuff

## Which Texts?

If it holds sacred or cultural significance for Heathens & Asatru of any geographical persuasion, it's going in eventually. I'm starting with the Eddic poetry and all three rune poems. Eventually, I'd like to make it through the Sagas and into the British Isles with Beowulf and the Nine Herbs Charm. Deep lore kinda stuff, with a very braod net. I figure we're all in this thing together, we should pool resources.

But what about that one Icelandic book of law written in runes already? That's going the opposite direction, but it's on my radar, not least because of its potential for an additional spell-check cross-reference.

## Original English Translation?

I'm relying on the public domain work of Bellows for the first edition, but plans are in place for proper English translations. I am currently using ChatGPT to help with some of this, and cross-referencing its output with three of other translations, and it seems to be pretty good. [It seems to match Bellows, but scrubs it of that out of place Victorian tone.](https://chat.openai.com/share/8826f738-0b8b-4450-9429-d4b947fbcba9). I will accept AI generated work. Please note that I will be running all submissions through plaigarism checkers as part of the submission review process. AI content will be double-checked for hallucinations, so please tag your PR as being AI generated/assisted.

## Spelling Methodology in a Dead Language?

The baseline for the Old Norse Texts I've processed so far is The Old Icelandic Text Society (Íslenzk fornrit/Hið íslenzka fornritafélag) standardized spelling via [the Humanities Department of the Univeristy of Oslo](https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=18). 

If there's a question between the aforementioned and the other sources listed throughout the README or the comments of the code itself, I cross-reference other editions of the text in question from publicly available and reputable sources. I try to use common sense and some amateur etymology, while keeping an eye out for paper towns/typos; the majority vote on the spelling takes it.

For the resulting runic versions, I run the dirty-data version through this codebase to polish down the rough edges. A couple letter-rune fixes, and then a spell checking proper, from the output of [runic.is]('https://runic.is/') (used with permission).

Further, I am cross-referencing the work of Dr. Jackson Crawford, via his YouTube series covering his estimation of the Havamal in YF. From that video/series, I'm building a runic spell-check dictionary (sc_dict.py), to perform ᚱ/ᛦ-swaps and other spelling considerations. Pro tip: if it's a s/z sound at the of the word in English, chances are pretty high it's ᛦ not ᚱ. You can check out the dictionary directry or Submissions Guidelines below for more details.

HOWEVER. Spelling, as a concept, didn't even exist when these documents were written, let alone as it does now. "Sound it out," and "Did you understand it or not?" are the only rules they had. So calls had to be made. See the comments in sc_dict.py further details. All of the possiible spellings are valid enough per the rules above, so some of the differences come down to simple preference. If you have an example of a better spelling, feel free to submit a pull request using the guidlines below.

# Submissions and pull requests are welcome

Whether it's an academic interest or spiritual devotion that brought you here, please feel free to submit changes to the work, to the code, anything. State your reasoning in as much detail as possible, and cite the applicable source(s). Bibliographic information is good, links are better. 

If you have new inscription databases to add to the cross-referencing function, code optimizations, or some other new feature: please, feel free to submit the PR. Any help will be greatly appreicated.

For the non-coders, search 'pull request tutorial for git/github beginners' in your preferred search engine, and that'll get you in the space you need to be and moving. 

## For Spelling-only corrections:
Add your entry to buildspellcheckdict.py in the format you see there. Save and run it to recompile spellcheck.json automatically.

See roadmap below for more details. 

## For New Texts:
Run `.newtext.sh`. Follow the directions on the screen.

## English Translations/Tranliterations:
Abide copyright law; make sure the translation is in the commons, or is otherwise licensed for republication. If you'd like to add additional English translates (eg, a Grimm translation) the files should be named in the following format: `EN-Lat-Name.txt` and `EN-ASF-Name.txt` 

Simple English-to-Futhorc transliteration is the name of the game here with ASF versions. We've all done it. Let's normalize it, but correctly - use the AS Futhorc. I use an app on my Chromebook for it. 

### No Elder Futhark tranliterations will be accepted. Here's why:
1. EF + Eng is wildly ahistorical and no one that I'm aware of knows enough Proto Old Norse outside of pure conjecture and few examples to be able to use them correctly. Part of the point of this project is accuracy, so this is the primary reason.
2. ASF + Eng is what actually happened. It was Old English, sure, but that was just English then. English runes are the Anglo-Saxon Furthorc. See also: Q. Part of the point is accuracy. If you write English in runic, it *should* be ASF.
3. The ASF contain all 24 EF already - The English Rune Poem is the reason we know about all 24 EF, in fact - the YF dropped letters, and both the Icelandic and Norwegian rune poems reflect that. Those dropped letters would still be a mystery to us today if it weren't for the English tradition.
5. ASF is the most recently updated runic repo circa 1951, if I recall correctly, courtesy of J.R.R. Tolkien himself. Feel free to use 'em in the transcripts, the man was an expert, and I accept his contribution. We let William Shakespeare coind whole words. Surely, we can grant Tolkien a few letters?
6. It's pretty quick to pick up after the EF. Honestly, it's just a few tweaks and a bonus aett. You're 3/4 of the way there if you know the EF already.

## Submission Review:
1. Plaigarism check via online tools for non-commons texts.
2. Double-checked for AI hallucinations and tone.
3. Checking the provided sources for veracity.
4. Asking follow up questions, if I have any.

# TODO/ROADMAP:
- ~Isolate spellcheck function for a 'spelling update' script that iterates through each directory in /texts/*/ON-YF.txt; presumably after updates to the json dictionary.~

- Get through 'normalizing the tone and floweriness of Bellow's English translations of the texts in a new translation.

- Add give a spellingupdate.py a bash wrapper that works like makespace.sh

- ~I should probably write my own code for the transliteration to ASF myself. I'm already doing heavier lifting in the spellchecker(s), and building other tools, so why not this one?~

- ~script batch file management to account/make space for additional translations.~