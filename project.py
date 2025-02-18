import requests
from bs4 import BeautifulSoup
import ollama

url = input("Enter the url of the movie you wish to see the summary of: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1").text.replace(" - full transcript","")
content = soup.find("div", id="cue-app").text.replace("\n", " ")

MODEL = "llama3.2"

prompt = f"You will receive a title and whole transcript of a movie, you will need to summarize the whole plot of the movie in a few paragraphs:\nTitle of the movie: {title}\nTranscript of the movie: {content}"

message = [
    {
        "role": "user",
        "content": prompt
    }
]

response = ollama.chat(model=MODEL, messages=message)
print(response["message"]["content"])
