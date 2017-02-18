# Let's only show the 20 newest
limit = 20;

# Load the feeds we are going to retrieve
rssfile = open("rss-feeds.txt");
rssFeedList = []
for url in rssfile:
	rssFeedList.append([url.strip()])

#for rssURL in rssFeedList:


print("----------------------------------------------------------------------")
print(rssFeedList)

