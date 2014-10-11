########################################
# This file illustrates how to download
# files to the disk from the web using
# Python. Please feel free to use this
# code in your extorter worm.
########################################

# The necessary header files
import urllib
import urllib.request

# Create an instance of the URL downloader class
#testfile = urllib.URLopen()

# Use the instance to fetch a file from the 
# web at the given URL. The first argument
# is the URL from which to fetch the file. 
# The second argument tells the function
# what to name of the file once download 
# completes.
urllib.request.urlretrieve("http://ecs.fullerton.edu/index.html", "meow.html")


