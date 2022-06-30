from instapy import InstaPy, smart_run
import config
def wordPressSession():
    comments = ["\U0001F60D","\U0001F63B","\U0001F4AF","\U0001F44C","\U0001F44F","\U0001F6B4","\U0001F6B5"]

    session = InstaPy(username=config.insta_username,
                      password=config.insta_password,
                      headless_browser=True)
    try:
        with smart_run(session):
            session.like_by_tags(["cyclingphotos", 'roadbike'], amount=10)
            session.set_do_comment(True, percentage=50)
            session.set_comments(comments)
    except:
        import traceback
        print(traceback.format_exc())
        pass
wordPressSession()