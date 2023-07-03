import webbrowser  

artist = input("Hello, please input the name of the artist you want to listen to. ")
album = input("Please input the name of the album you would like to hear. Leave blank if you want to see the artist's discography. ")

artist = artist.lower()
album = album.lower()

srch = artist + " " + album #what will be searched

srch = srch.split(" ")

searchquery = ""

for i in range(len(srch)):
    if i < (len(srch)-1):
        searchquery += srch[i] + "+"
    else:
        searchquery += srch[i]

bandcampsrch = "https://bandcamp.com/search?q="+ searchquery + "&item_type=a&from=results"

webbrowser.open_new_tab(bandcampsrch)