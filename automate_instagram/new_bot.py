from instapy import InstaPy
insta_username = '*******'
insta_password = '*****'
session = InstaPy(username=insta_username, password=insta_password)
session.login()
session.set_do_comment(True, percentage=10)
session.set_comments(['Super !', 'Génial !', 'Incroyable !'])
session.set_dont_like(['pizza', 'fille']) 
session.like_by_tags(['roadbike', 'cyclinglife'], amount=100)
session.end()
