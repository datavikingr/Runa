# Runa and the Visabok Project

The goal of this project, very simply, is to put Heathens (American) and Asatru (European) back in control of our own culture and lore. 

It starts from the rebuilding the stories we have left. We need to see them in our own letters, at the very least. 

So this project aims to convert Old Norse (ON), Old Icelandic (OI), and Old English (OE) ancient texts into their respective runic script. Younger Futhark (YF) for ON/OI texts, Anglo-Saxon Futhorc (ASF) for the OE texts. The desired end product is a multi-volume book containing ON-YF, ON-Latin alphabet (LA), modern English (EN), and EN-ASF transliteration versions of our stories, myths, and lore for proper publishing. Or the applicable languages, you get the idea.

Basically, I mean to do some of our 'homework' for the new folks and the curious non-heathens and asssembling it all, the way I always wished we had 'em when I was still a neophyte. Personally, I feel it's time to stop playing in the dust. We need to consolidate what we have and start looking forward and building. Coding and writing are my primary skill sets, so this is what I'm bringing to the table.

# Technical Stuff

## Dependencies

Python (Python3 if you're on Debian like I am), Chrome, Selenium, . I'm running this on Debian, so use apt (and deb-get, or manually install Chrome from their website). The required Python libraries are as follows: BeautifulSoup, Selenium, webdriver_manager, and json. Just grab 'em with pip.

# Cultural Stuff

## Which Texts?

If it holds sacred or cultural significance for Heathens & Asatru of any geographical persuasion, it's going in eventually. I'm starting with the Codex Regius and the Eddic poetry. Eventually, I'd like to make it through the Sagas and into the Isles with Beowulf and the Nine Herbs Charm. 

But what about that one Icelandic book of law written in runes already? That's going the opposite direction, but it's  on my radar.

## Original English Translation?

I'll probably rely on the public domain work of Bellows, Grimm, et al., but I wouldn't discount the possibility of 'some' tweaks in the final edition. Maybe 

## Spelling Methodology in a Dead Language?

The baseline for the Old Norse Texts I've played with so far is The Old Icelandic Text Society (Íslenzk fornrit/Hið íslenzka fornritafélag) standardized spelling via the Humanities Department of the Univeristy of Oslo (https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=18). 

If there's a question between that and the other sources listed throughout the README or the code itself, I cross-reference other editions of the text in question from publicly available and reputable sources. I try to use common sense and some amateur etymology, while keeping an eye out for paper towns; the majority vote on the spelling takes it. Because, of course, even our definitive sources disagree with each other. Neat.

For the resulting runic versions, I run the dirty-data version through this codebase to polish down the rough edges. A couple letter-rune fixes, and then spell checking proper, on the output of runic.is.

HOWEVER. Spelling, as a concept, didn't even exist when these documents were written, let alone as it does now. "Sound it out" and "Did you understand it or not?" are the only rules they had. So should we then ignore the inscription corpus and just wing it? Nope! Hence, this project. 

Further, I'm cross-referencing the work of Dr. Jackson Crawford, via his YouTube series covering his estimation of the Havamal in YF. From that video/series, I'm building a runic spell-check dictionary (sc_dict.py), to perform ᚱ/ᛦ-swaps and other spelling considerations. Pro tip: if it's a s/z sound at the of the word in English, chances are pretty high it's ᛦ not ᚱ. 

Notes in the very bottom of sc_dict.py clarify any calls I had to make during this process. All of the possiible spellings are valid enough per the rules above, so some of the differences come down to simple preference. And that's okay.

## English Transliteration into Runes?

C'mon. We all do it and its looooong past high time we normalize the behavior, in no small part because culture and language are descriptive, rather than prescriptive. So -WE- get to make choices ourselves as we're working with the tools. 

Why then use the Anglo-Saxon Futhorc (ASF), rather than the Elder Futhark (EF)? Three reasons:

1. ASF contains the EF in its entirety, with maybe 2 differences between overlapping runes.
2. ASF has the letter Q, which is kind of a big deal for writing English.
3. ASF is the most recently updated runic repository, courtesy of J.R.R. Tolkien (yes, -that- Tolkien; & that half-joke about the repo update only lands if you're a coder). 

NOTE: Tolkien's SH and OO runes will be used in this project, as they're also a big deal in transliterating English words.

If you don't like my methods or choices, feel free to build your own - and let's compare notes afterwards!
