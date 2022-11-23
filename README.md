# 🖥 Discord-members-scapper
 A Python program to scrap members of a server.
 
# 🔗 Usage

<p> So basically discord doesn't allows to scrap all the members of a discord server, but there are workaround, there are 2 methods in this repo to scrap the members </p>

<h3> Method 1 </h3>

So in this method we'll use `fetch_user_1.py` to scrap the members, this script will basically scrap the members that are visible in the sidebar i.e. online members, it will scrap all the members in a small server because even the offline members are visible in the sidebar, but in a big server the offline members are not visible so it won't be able to scrap those members, this method is pretty fast.

<h4> Usage </h4>

Open the `fetch_users_1.py` in a text editor of your choice and put your token in the `token` variable in line 4 and server id in `guild_id` variable in line 5, make sure the token is in the server.
<br> <br>
Like below:
<br>
![image](https://user-images.githubusercontent.com/109065518/203467198-e3e72ffc-be57-47dc-a1fe-9b8ece959cfd.png)
<br>
<h3> Method 2 </h3>

So this method might be more efficient but more slow, in this method the bot will go through every message in a channel and return the id of the person who sent that message, this method might be better because it'll scrap active members and more members if a server is big, but it can be very slow because the channels can have millions of messages so it might even break while scrapping.

<h4> Usage </h4>

Open the `fetch_users_2.py` in a text editor of your choice and put your token in the `token` variable in line 4 and channel id in `channel_id` variable in line 5, make sure the token is in the server of that channel and have access to view and read message history of that channel.
<br> <br>
Like below:
<br>
![image](https://user-images.githubusercontent.com/109065518/203468476-ca7423d3-206d-459b-b5b0-9a5e75e38523.png)

# 📝 Footnotes
 If your token/main account gets disabled I am not responsible for it, Use these scripts at your own risk, this project was just made for learning purposes.
