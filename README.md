Function to tokenise a string of contiguous words. Very handy for breaking up domain names, among other things.

Run the script to read in a set of words and then pass a string to the `splitter()` function. The function will output a list of the possible ways the string can be broken into English words (or whatever words are in the `word-list.txt` file.) If a string can't be split cleanly, then an empty list is returned.

```python
>>> splitter('splitthisstring')
['split this string']
>>> splitter('dogsandcatsandrats')
['dog sand cat sand rats',
 'dog sand cats and rats',
 'dogs and cat sand rats',
 'dogs and cats and rats']
>>> splitter('trytosplitxyziasfja')
[]
```

The list of English words here, `word-list.txt`, is taken from http://www.curlewcommunications.co.uk/wordlist.html
