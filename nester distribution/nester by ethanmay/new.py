  movies = [
 "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
 ["Graham Chapman",
 ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
def print_lol(movies):
 for items in movies:
     """Even though this code has syntax errors, it is supposed to be a nester for
     longer lists, it works by checking deeper_items without calling upon them"""
if isinstance(items, movies):
print_lol(movies)
    """The print_lol function is a basic way to organize lists within python"""
else:
print(items)

