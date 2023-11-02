class Instagram:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.following = 0
        self.followers = 0
        self.following_list = []
        self.followers_list = []
        self.posts = []

    def follow(self, user_obj):
        self.following += 1
        self.following_list.append(user_obj.username)
        user_obj.followers += 1
        user_obj.followers_list.append(self.username)

    def unfollow(self,user_obj):
        if user_obj.username in self.following_list:
            self.following_list.remove(user_obj.username)
            self.following-=1
            user_obj.followers_list.remove(self.username)
            user_obj.followers-=1

    def transfer_follower(self,receiver_user):
        if self.followers >= 1:
            self.followers -=1
            if receiver_user.username in self.followers_list:
                self.followers_list.remove(receiver_user.username)
                receiver_user.followers +=1
                receiver_user.followers_list.append(self.username)


    def post(self,text):
        self.posts.append(text)


    def self_view_post(self,username,database):
        return username in database and username in self.following_list

    def view_posts(self,username,database):
        if self.self_view_post(username,database):
            user_obj=database[username]
            posts = user_obj.posts
            if posts:
                print(f"posts by {user_obj.username}:")
                for i, post in enumerate(posts,1):
                    print(f"{i}.{post}")
            else:
                print(f"{user_obj.username}has no posts.")
        else:
            print(f"you are not following {username}.")










# oye = Instagram("Oye", "oyelove", "pass")
# muni = Instagram("Munirat", "mallow", "pass")
#
# print(f"Oye Followers: {oye.followers}, Oye Followers_list: {oye.followers_list}, Oye Following: {oye.following}, Oye Following_list: {oye.following_list}")
# print(f"muni Followers: {muni.followers}, muni Followers_list: {muni.followers_list}, muni Following: {muni.following}, muni Following_list: {muni.following_list}")
#
# oye.follow(muni)
#
# print(f"Oye Followers: {oye.followers}, Oye Followers_list: {oye.followers_list}, Oye Following: {oye.following}, Oye Following_list: {oye.following_list}")
# print(f"muni Followers: {muni.followers}, muni Followers_list: {muni.followers_list}, muni Following: {muni.following}, muni Following_list: {muni.following_list}")


database = {}

app_on = True

while app_on:
    todo = input("Todo (signup, login, close): ")
    if todo == 'signup':
        name = input("Name: ").upper()
        username = input("Username: ")
        passw = input("Password: ")
        while username in database:
            print(f"Username({username}) taken.")
        else:
            database[username] = Instagram (name, username, passw)
            print(username, " account created successfully.")

    elif todo == 'login':
        username = input("Username: ")
        passw = input("Password: ")
        if username in database and passw == database[username].password:
            current_user = database[username]
            print("Welcome ", current_user.name)
            user_in = True
            while user_in:
                user_command = input("Command (1. check followers, 2. check following, 3. follow, 4. unfollow, 5.transfer, 6.post, 7.selfview_post, 8.view_post, 9.logout ): ")
                if user_command == '1':
                    print(f"{current_user.followers} FOLLOWERS\nFOLLOWERS: {current_user.followers_list}")
                elif user_command == '2':
                    print(f"{current_user.following} FOLLOWS\nFOLLOWING: {current_user.following_list}")
                elif user_command == '3':
                    friends = [users for users in database if users != current_user.username and users not in current_user.following_list]
                    print(friends)
                    if friends:
                        username = input("Friend username: ")
                        if username in database:
                            current_user.follow(database[username])
                            print(f"You have successfully followed {username}.")
                        else:
                            print(f"{username} not recognized.")
                    else:
                        print("No registered user yet.")

                elif user_command=='4':
                    username_to_unfollow=input("username to unfollow:")
                    if username_to_unfollow in database:
                        current_user.unfollow(database[username_to_unfollow])
                        print(f"you have unfollowed {username_to_unfollow}.")
                    else:
                        print(f"{username_to_unfollow} not recognized")


                elif user_command=='5':
                    friends = [users for users in database if users != current_user.username and users not in current_user.following_list]
                    print(friends)
                    if friends:
                        username=input("friend username to transfer to:")
                        if username in database:
                            receiver_user = database[username]
                            current_user.transfer_follower(receiver_user)
                            print(f"You have sucessfully transfered a follower to {receiver_user.username}")


                    new_follower_username=input("Enter the username to transfer a follower to:")
                    if new_follower_username in current_user.followers_list:
                        current_user.transfer_follower(database[new_follower_username],new_follower_username)
                        print(f"You have transferred a follower to {new_follower_username}.")
                    else:
                        print(f"{new_follower_username} is not one of your followers")

                elif user_command=='6':
                    text= input("Enter your post:")
                    current_user.post(text)
                    print("Posted Successfully")

                elif user_command=='7':
                    if current_user.posts:
                        print("your posts:")
                        for i, post in enumerate(current_user.posts,1):
                            print(f"{i}.{post}")
                    else:
                        print("You have no posts yet")

                elif user_command=='8':
                    username = input("Username to view their posts:")
                    current_user.view_posts(username,database)



                elif user_command == '9':
                    user_in = False
                    print("Logout successful.")
                else:
                    print("Invalid command")




    elif todo == 'close':
        app_on =False
        print("Bye")
    else:
        print("Invalid command.")
