import util
import chromesearchre

searchtext = "apple app"

title = util.get_longest_word(searchtext)
chromesearchre.google_search(title)