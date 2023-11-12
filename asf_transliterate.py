#!python3
import time, string, subprocess, json

with open('dictionaries/asfdoubleswap.json') as ligaturerunes:
    ls_dict = json.load(ligaturerunes)
with open('EN-Lat.txt', 'r') as source:
    input_text = source.read()
modified_chars = [modify_characters(c, ls_dict) for c in input_text]
modified_s = ''.join(modified_chars)
with open('4-futhark_allrunes.txt', 'w') as f:
    f.write(modified_s)