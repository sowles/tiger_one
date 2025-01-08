import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from promptsanitizer import create_chatgpt_prompt

load_dotenv()

json_input = "{\"__typename\": \"User\", \"_lastChangedAt\": 1720848523070.0, \"createdAt\": \"2024-07-13T05:09:02.172Z\", \"HomeContents\": {}, \"fullName\": \"Sarah a fake person\", \"gender\": \"Female\", \"groups\": [], \"privacySettings\": {\"Enneagram\": \"PUBLIC\", \"Ocean\": \"PUBLIC\", \"MBTI\": \"PUBLIC\"}, \"_version\": 7.0, \"profile_picture\": \"https://mynd-storage-7a45ba09203303-dev.s3.amazonaws.com/public/profile_pictures/bc6e78e7-ff95-4eb7-abb0-6559f62a295f.w\", \"searchableUsername\": \"i_am_real\", \"likedStories\": {}, \"testResults\": {\"Wing\": \"Two\", \"MBTIScore\": {\"P\": 2.0, \"S\": 0.0, \"T\": 2.0, \"E\": 0.0, \"F\": 0.0, \"I\": 2.0, \"J\": 0.0, \"N\": 2.0}, \"Enneagram\": \"One\", \"EnneagramScore\": {\"Eight\": 4.0, \"Five\": 2.0, \"Six\": 2.0, \"One\": 8.0, \"Four\": 3.0, \"Nine\": 4.0, \"Seven\": 5.0, \"Two\": 4.0, \"Three\": 4.0}, \"Ocean\": \"\", \"OceanScore\": {}, \"MBTI\": \"INTP\"}, \"updatedAt\": \"2024-07-13T05:28:43.052Z\", \"authId\": \"bc6e78e7-ff95-4eb7-abb0-6559f62a295f\", \"MBTI\": \"INTP\", \"username\": \"I_am_real\", \"Enneagram\": \"One\", \"id\": \"bc6e78e7-ff95-4eb7-abb0-6559f62a295f\", \"tags\": [\"Birthplace : Rural\", \"Favorite music genre : Electronic\", \"Birth Order : Triplet\"]}"
data = json.loads(json_input)
prompt = create_chatgpt_prompt(json_input)

full_name = data.get('fullName', 'User')
gender = data.get('gender', 'Not specified')
username = data.get('username', 'N/A')
profile_picture = data.get('profile_picture', 'N/A')
privacy_settings = data.get('privacySettings', {})
test_results = data.get('testResults', {})
tags = data.get('tags', [])


client = OpenAI(api_key = os.getenv("API_KEY"))
# user_input = input("Enter your prompt: ")

compatibility_interest = ['Romance', 'conflict', 'Friendship']

user_contents = [input("Enter your prompt: "),prompt]
system_contents = ["You are a happy assistant", "You are in a bad mood today", "you are a psychologist helping me out with personality insights"]

response_format = test
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": system_contents[0]},
        {"role": "user", "content": user_contents[1]}
    ]
    
)
print(completion.choices[0].message)