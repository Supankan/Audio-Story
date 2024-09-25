<<<<<<< HEAD
import requests
from dotenv import find_dotenv, load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the API key from environment variables
HF_API_KEY = os.getenv("HF_API_KEY")

API_URL_img2text = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers_img2text = {"Authorization": f"Bearer {HF_API_KEY}"}

API_URL_llm = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers_llm = {"Authorization": f"Bearer {HF_API_KEY}"}

API_URL_audiogen = "https://api-inference.huggingface.co/models/myshell-ai/MeloTTS-English"
headers_audiogen = {"Authorization": f"Bearer {HF_API_KEY}"}

API_URL_summarize = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers_summarize = {"Authorization": f"Bearer {HF_API_KEY}"}

API_URL_sentiment = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers_sentiment = {"Authorization": f"Bearer {HF_API_KEY}"}

# Using Image-to-Text to create a description of the image.
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL_img2text, headers=headers_img2text, data=data)
    return response.json()

# Using LLM to create a story from the description.
def generate_story(payload):
    response = requests.post(API_URL_llm, headers=headers_llm, json=payload)
    return response.json()

# Using a Text-to-Speech model to create an audio story.
def audiogen(message):
    payloads = {"inputs": message}
    response = requests.post(API_URL_audiogen, headers=headers_audiogen, json=payloads)
    with open("audio.flac", "wb") as file:
        file.write(response.content)

def summarize(payload):
    payloads = {
        "inputs": payload,
        "parameters": {"max_length": 35}
        }
    response = requests.post(API_URL_summarize, headers=headers_summarize, json=payloads)
    return response.json()

def sentiment(payload):
    payloads = {"inputs": payload}
    response = requests.post(API_URL_sentiment, headers=headers_sentiment, json=payloads)
    return response.json()

def main():
    st.set_page_config(page_title="HF Image to Audio Story", page_icon="HF")
    st.header("Image to Audio Story and Sentiment Analysis")
    uploaded_file = st.file_uploader("Choose an Image: ", type="jpg")

    if uploaded_file is not None:
        temporary_file_path = uploaded_file.name  # Save the file path for cleanup

        bytes_data = uploaded_file.getvalue()
        with open(temporary_file_path, "wb") as file:
            file.write(bytes_data)

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        scenario = query(temporary_file_path)

        # Debug print to check the response
        st.write("Scenario Response:", scenario)

        if isinstance(scenario, list) and len(scenario) > 0 and 'generated_text' in scenario[0]:
            story = generate_story({"inputs": str(scenario[0]['generated_text'])})

            # Debug print to check the story response
            st.write("Story Response:", story)

            if isinstance(story, list) and len(story) > 0 and 'generated_text' in story[0]:
                story_summary = summarize(story[0]['generated_text'])

                # Debug print to check the summary response
                st.write("Summary Response:", story_summary)

                if isinstance(story_summary, list) and len(story_summary) > 0 and 'summary_text' in story_summary[0]:
                    story_sentiment = sentiment(story_summary[0]['summary_text'])

                    # Debug print to check the sentiment response
                    st.write("Sentiment Response:", story_sentiment)

                    audiogen(story_summary[0]['summary_text'])

                    with st.expander("Scenario"):
                        st.write(scenario[0]['generated_text'])
                    with st.expander("Story"):
                        st.write(story_summary[0]['summary_text'])
                    with st.expander("Sentiment of the story"):
                        for elem in story_sentiment[0]:
                            st.write(f"{elem['label']}: {elem['score']:.3f}")

                    st.audio("audio.flac")
                else:
                    st.error("Error in summarizing the story.")
            else:
                st.error("Error in generating the story.")
        else:
            st.error("Error in generating the scenario.")

        # Cleanup: Remove the temporary image file and audio file
        os.remove(temporary_file_path)
        os.remove("audio.flac")

if __name__ == "__main__":
    main()
=======
import requests
from dotenv import find_dotenv, load_dotenv
import streamlit as st
import os

load_dotenv(find_dotenv())

API_URL_img2text = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers_img2text = {"Authorization": "Bearer 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"}

API_URL_llm = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers_llm = {"Authorization": "Bearer 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"}

API_URL_audiogen = "https://api-inference.huggingface.co/models/myshell-ai/MeloTTS-English"
headers_audiogen = {"Authorization": "Bearer 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"}

API_URL_summarize = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers_summarize = {"Authorization": "Bearer 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"}

API_URL_sentiment = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers_sentiment = {"Authorization": "Bearer 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"}

# Using Image-to-Text to create a description of the image.
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL_img2text, headers=headers_img2text, data=data)
    return response.json()

# Using LLM to create a story from the description.
def generate_story(payload):
    response = requests.post(API_URL_llm, headers=headers_llm, json=payload)
    return response.json()

# Using a Text-to-Speech model to create an audio story.
def audiogen(message):
    payloads = {"inputs": message}
    response = requests.post(API_URL_audiogen, headers=headers_audiogen, json=payloads)
    with open("audio.flac", "wb") as file:
        file.write(response.content)

def summarize(payload):
    payloads = {
        "inputs": payload,
        "parameters": {"max_length": 35}
        }
    response = requests.post(API_URL_summarize, headers=headers_summarize, json=payloads)
    return response.json()

def sentiment(payload):
    payloads = {"inputs": payload}
    response = requests.post(API_URL_sentiment, headers=headers_sentiment, json=payloads)
    return response.json()

def main():
    st.set_page_config(page_title="HF Image to Audio Story", page_icon="HF")
    st.header("Image to Audio Story and Sentiment Analysis")
    uploaded_file = st.file_uploader("Choose an Image: ", type="jpg")

    if uploaded_file is not None:
        temporary_file_path = uploaded_file.name  # Save the file path for cleanup

        bytes_data = uploaded_file.getvalue()
        with open(temporary_file_path, "wb") as file:
            file.write(bytes_data)

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        scenario = query(temporary_file_path)

        # Debug print to check the response
        st.write("Scenario Response:", scenario)

        if isinstance(scenario, list) and len(scenario) > 0 and 'generated_text' in scenario[0]:
            story = generate_story({"inputs": str(scenario[0]['generated_text'])})

            # Debug print to check the story response
            st.write("Story Response:", story)

            if isinstance(story, list) and len(story) > 0 and 'generated_text' in story[0]:
                story_summary = summarize(story[0]['generated_text'])

                # Debug print to check the summary response
                st.write("Summary Response:", story_summary)

                if isinstance(story_summary, list) and len(story_summary) > 0 and 'summary_text' in story_summary[0]:
                    story_sentiment = sentiment(story_summary[0]['summary_text'])

                    # Debug print to check the sentiment response
                    st.write("Sentiment Response:", story_sentiment)

                    audiogen(story_summary[0]['summary_text'])

                    with st.expander("Scenario"):
                        st.write(scenario[0]['generated_text'])
                    with st.expander("Story"):
                        st.write(story_summary[0]['summary_text'])
                    with st.expander("Sentiment of the story"):
                        for elem in story_sentiment[0]:
                            st.write(f"{elem['label']}: {elem['score']:.3f}")

                    st.audio("audio.flac")
                else:
                    st.error("Error in summarizing the story.")
            else:
                st.error("Error in generating the story.")
        else:
            st.error("Error in generating the scenario.")

        # Cleanup: Remove the temporary image file and audio file
        os.remove(temporary_file_path)
        os.remove("audio.flac")

if __name__ == "__main__":
    main()
>>>>>>> 98a24151ace2df7fc0545f75f9fe152e16499e62
