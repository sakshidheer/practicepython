def is_string_upper(feed):
    try:
        return feed.upper() == feed
    except AttributeError:
        print("The passed parameter is not of type string")