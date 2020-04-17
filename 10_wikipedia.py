#-----Wikipedia-------

import wikipedia

# for direct searching thru wikipedia
results = wikipedia.page("Python")
print(results.summary)

# for links
for link in results.links:
    print(link)
