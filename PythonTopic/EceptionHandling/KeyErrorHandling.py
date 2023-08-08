facebook_posts=[{'likes':23,'Comment':45},
                {'likes':12,'Comment':8,'Shares':5},
                {'likes':21,'Comment':12,'Shares':7},
                {'Comments':2,'shares':5},
                {'Comments':3,'Shares':4},
                {'likes':5,'Comment':9},
                {'likes':10,'Comment':13}
]
total_likes=0
for post in facebook_posts:
    try:
        total_likes=total_likes+post["likes"]
    except KeyError:
        pass
print(total_likes)