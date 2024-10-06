import openai
import os

# Function to summarize text
def summarize_text(text):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Completion.create(
        model='gpt-4',
        prompt=f'Summarize the following text:\n\n{text}\n',
        max_tokens=100,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    text = 'OpenAI provides access to language models like GPT-4 that can perform a wide range of tasks, including summarizing text.'
    print(summarize_text(text))
