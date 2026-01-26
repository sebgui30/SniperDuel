def find_unfollowers(old_list, new_list):
    unfollowers = old_list - new_list
    return unfollowers

def find_new_followers(old_list, new_list):
    new_followers = new_list - old_list
    return new_followers