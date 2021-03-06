A neat function to split up a string of contiguous words. Very handy for [breaking up domain names](http://ajcr.net/Words-nobody-wants/), among other things.

Run the script to read in a set of words and then pass a string to the `splitter()` function. The function will return a list of the possible ways the string can be broken into English words (or whatever words are found in the `word-list.txt` file). If a string can't be split cleanly an empty list is returned.

```python
>>> from splitter import splitter
>>> splitter('splitthisstring')
['split this string']
>>> splitter('dogsandcatsandrats')
['dog sand cat sand rats',
 'dog sand cats and rats',
 'dogs and cat sand rats',
 'dogs and cats and rats']
>>> splitter('trytosplitxyzabcohdear')
[]
```

The list of English words here, `word-list.txt`, is taken from [Curlew Communications](http://www.curlewcommunications.co.uk/wordlist.html). You can, of course, use *any* list of words in whatever language you like.
