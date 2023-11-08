# Runa and the Visabok Project

The goal of this project, very simply, is to put Heathens (American) and Asatru (European) back in control of our own culture and lore. It starts from the rebuilding the stories we have left: we need to see them in our own letters at the absolute minimum. 

So this project aims to convert Old Norse (ON), Old Icelandic (OI), and Old English (OE) ancient texts into their respective runic script. Younger Futhark (YF) for ON/OI texts, Anglo-Saxon Futhorc (ASF) for the OE texts. The desired end product is a multi-volume set containing ON-YF, ON-Latin alphabet (Lat), modern English (EN), and EN-ASF transliteration versions of our stories, myths, and lore for proper publishing. Or the applicable/appropriate languages, you get the idea.

Basically, I mean to do some of our 'homework' for us, the way I always wished we had 'em when I was still a neophyte. Personally, I feel it's time to stop playing in the dust. We need to consolidate what we have and start looking forward and building. Code, data, and writing are my primary skill sets, so this is what I'm bringing to the table.

# Technical Stuff

## Dependencies for the scripts

Python (Python3 if you're on Debian like I am), Chrome, Selenium. I'm running this on Debian, so use apt (and deb-get, or manually install Chrome from their website). The required Python libraries are as follows: BeautifulSoup, Selenium, webdriver_manager, and json. Just grab 'em with pip.

# Cultural Stuff

## Which Texts?

If it holds sacred or cultural significance for Heathens & Asatru of any geographical persuasion, it's going in eventually. I'm starting with the Eddic poetry and all three rune poems. Eventually, I'd like to make it through the Sagas and into the British Isles with Beowulf and the Nine Herbs Charm. 

But what about that one Icelandic book of law written in runes already? That's going the opposite direction, but it's on my radar, not least because of its potential for an additional spell-check cross-reference.

## Original English Translation?

I'm relying on the public domain work of Bellows, Thorpe, Grimm, et al. for the first edition, but plans are in place for proper English translations. 

## Spelling Methodology in a Dead Language?

The baseline for the Old Norse Texts I've played with so far is The Old Icelandic Text Society (Íslenzk fornrit/Hið íslenzka fornritafélag) standardized spelling via [the Humanities Department of the Univeristy of Oslo](https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=18). 

If there's a question between that and the other sources listed throughout the README or the comments of the code itself, I cross-reference other editions of the text in question from publicly available and reputable sources. I try to use common sense and some amateur etymology, while keeping an eye out for paper towns/typos; the majority vote on the spelling takes it. Because, of course, even our definitive sources disagree with each other. Neat.

For the resulting runic versions, I run the dirty-data version through this codebase to polish down the rough edges. A couple letter-rune fixes, and then a spell checking proper, on the output of runic.is.

HOWEVER. Spelling, as a concept, didn't even exist when these documents were written, let alone as it does now. "Sound it out" and "Did you understand it or not?" are the only rules they had. So should we then ignore the inscription corpus and just wing it? Nope! Hence, this project. 

Further, I am cross-referencing the work of Dr. Jackson Crawford, via his YouTube series covering his estimation of the Havamal in YF. From that video/series, I'm building a runic spell-check dictionary (sc_dict.py), to perform ᚱ/ᛦ-swaps and other spelling considerations. Pro tip: if it's a s/z sound at the of the word in English, chances are pretty high it's ᛦ not ᚱ. 

Notes in the very bottom of sc_dict.py clarify any calls I had to make during this process. All of the possiible spellings are valid enough per the rules above, so some of the differences come down to simple preference. And that's okay.

## English Transliteration into Runes?

C'mon. We *all* do it and its **__looooong__** past time that we normalize the behavior, in no small part because culture and language are descriptive, rather than prescriptive. So **__WE__** get to make choices ourselves as we're working with the tools. 

Why then use the Anglo-Saxon Futhorc (ASF), rather than the Elder Futhark (EF)? Three reasons:

1. ASF contains the EF in its entirety, with maybe 3 differences between overlapping runes.
2. ASF has the letter Q, which is kind of a big deal for writing English.
3. ASF is the most recently updated runic repository (circa 1951, I believe), courtesy of J.R.R. Tolkien (yes, -that- Tolkien; & that half-joke about the repo update only lands if you're also coder). 

NOTE: Tolkien's SH and OO runes will be used in the ASF portions of the project, as they're also kind of a big deal in transliterating English words. 'Fish' and 'book' are a lot easier, to say the very least. The man was an expert, and I, for one, accept his contributions. 

# Submissions and pull requests are welcome

Whether it's an academic interest or spiritual devotion that brought you here, please feel free to submit changes to the work, to the code, anything. State your reasoning in as much detail as possible, and cite the applicable source(s). Bibliographic information is good, links are better (within the bounds of applicable copyright law). 

If you have new inscription databases to cross-reference, or code optimizations, or some other new feature; please, feel free. I'm a lifelong coder, but that doesn't make me the best coder by a long shot. Any help would be greatly appreicated.

If you have spelling adjustments or typo corrections, cite your sources and argue your case as best as you're able. I'll reiterate spelling didn't exist as an idea when these alphabets and languages were living, but obviously there's still plenty of room for improvement. Prioirtize 'that's all the way wrong' over 'that's okay, but could be better'. 

For the code-literate, simply submit a pull request, you already know the drill. If you need a new branch or something, go nuts. Try to use best practices, to push me into the same (I'm a 'did it work? then it's not stupid' kind of coder, bear with me).

For the non-coders, search 'pull request tutorial for git beginners' in your preferred search engine, and that'll get you in the space you need to be and moving. Terminal use is *not* required, you can do everything via VS Code or similar 'normal' GUI-based program.