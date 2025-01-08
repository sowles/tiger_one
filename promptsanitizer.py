import json

def create_chatgpt_prompt(json_input):
    data = json.loads(json_input)

    full_name = data.get('fullName', 'User')
    gender = data.get('gender', 'Not specified')
    username = data.get('username', 'N/A')
    profile_picture = data.get('profile_picture', 'N/A')
    privacy_settings = data.get('privacySettings', {})
    test_results = data.get('testResults', {})
    tags = data.get('tags', [])

    mbti_result = test_results.get('MBTI', 'Not provided')
    enneagram_result = test_results.get('Enneagram', 'Not provided')
    ocean_result = test_results.get('Ocean', 'Not provided')


    mbti_privacy = privacy_settings.get('MBTI', 'Not specified')
    enneagram_privacy = privacy_settings.get('Enneagram', 'Not specified')
    ocean_privacy = privacy_settings.get('Ocean', 'Not specified')


    prompt1 = (
        f"Create a user profile prompt for a {gender} named '{full_name}' with the username '{username}'.\n"
        f"Profile Picture: {profile_picture}\n"
        f"Personality Test Results:\n"
        f"- MBTI: {mbti_result} (Privacy: {mbti_privacy})\n"
        f"- Enneagram: {enneagram_result} (Privacy: {enneagram_privacy})\n"
        f"- OCEAN: {ocean_result} (Privacy: {ocean_privacy})\n"
        f"Tags: {', '.join(tags) if tags else 'None'}"
    )
    prompt2 = (
        f"Compare two personalities with  {gender} named '{full_name}' with the username '{username}'.\n"
        f"Profile Picture: {profile_picture}\n"
        f"Personality Test Results:\n"
        f"- MBTI: {mbti_result} (Privacy: {mbti_privacy})\n"
        f"- Enneagram: {enneagram_result} (Privacy: {enneagram_privacy})\n"
        f"- OCEAN: {ocean_result} (Privacy: {ocean_privacy})\n"
        f"Tags: {', '.join(tags) if tags else 'None'}"
    )

    return prompt

# Example usage
json_input = "{\"__typename\": \"User\", \"_lastChangedAt\": 1720848523070.0, \"createdAt\": \"2024-07-13T05:09:02.172Z\", \"HomeContents\": {}, \"fullName\": \"Sarah a fake person\", \"gender\": \"Female\", \"groups\": [], \"privacySettings\": {\"Enneagram\": \"PUBLIC\", \"Ocean\": \"PUBLIC\", \"MBTI\": \"PUBLIC\"}, \"_version\": 7.0, \"profile_picture\": \"https://mynd-storage-7a45ba09203303-dev.s3.amazonaws.com/public/profile_pictures/bc6e78e7-ff95-4eb7-abb0-6559f62a295f.w\", \"searchableUsername\": \"i_am_real\", \"likedStories\": {}, \"testResults\": {\"Wing\": \"Two\", \"MBTIScore\": {\"P\": 2.0, \"S\": 0.0, \"T\": 2.0, \"E\": 0.0, \"F\": 0.0, \"I\": 2.0, \"J\": 0.0, \"N\": 2.0}, \"Enneagram\": \"One\", \"EnneagramScore\": {\"Eight\": 4.0, \"Five\": 2.0, \"Six\": 2.0, \"One\": 8.0, \"Four\": 3.0, \"Nine\": 4.0, \"Seven\": 5.0, \"Two\": 4.0, \"Three\": 4.0}, \"Ocean\": \"\", \"OceanScore\": {}, \"MBTI\": \"INTP\"}, \"updatedAt\": \"2024-07-13T05:28:43.052Z\", \"authId\": \"bc6e78e7-ff95-4eb7-abb0-6559f62a295f\", \"MBTI\": \"INTP\", \"username\": \"I_am_real\", \"Enneagram\": \"One\", \"id\": \"bc6e78e7-ff95-4eb7-abb0-6559f62a295f\", \"tags\": [\"Birthplace : Rural\", \"Favorite music genre : Electronic\", \"Birth Order : Triplet\"]}"

prompt = create_chatgpt_prompt(json_input)
print(prompt)
