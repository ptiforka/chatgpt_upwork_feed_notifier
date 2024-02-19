from openai import OpenAI

client = OpenAI(api_key='token')

# Your OpenAI API key

def generate_custom_message_for_job(upwork_jobs):
    base_prompt = """
    ChatGPT, you are now a score master of new jobs that I'm looking through on UpWork. The jobs are sent in JSON format. Rate each job from 1 to 10. If the country is the **United States, Canada, Israel, or the UK**, give it a higher score. If it's **$30 or more per hour**, give it a higher score; if it's less, give it a lower score. If the text is written in a poor manner, give it a lower score. If the text includes words such as "ASAP", "In a hurry", or similar meanings, give it a lower score. If the item contains these skills, give it a higher score: **"AWS Lambda", "Serverless", "DynamoDB".**

Provide me the output in this format:

Title: {Job_title}

Country: {Item_Country}

Job Description Summary: {Item_Summary}

Rate: {Houry_Rate}

Skills: {Item_Skills}

URL: {Item_URL}

Score: {Item_Score}

Here is the list, you need to parse and give the score:
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": base_prompt+str(upwork_jobs),
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Example usage with a special prompt
