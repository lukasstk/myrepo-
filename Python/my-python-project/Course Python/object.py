from user import *
from post import *

app_user_one = User("nn@nn.com", "Lukas Stank", "123", "Student")
app_user_one.get_user_info()

app_user_one.change_job_title("Student 2")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James", "345", "Homeless")
app_user_two.get_user_info()

new_post = Post("fuck you!", app_user_one.name)
new_post.get_post_info()
