# Description
A simple python script that summarizes the plot a given movie using AI. The script works by using Meta's llama3.2 AI through Ollama. It scrapes the website of the provided url and returns the summary of the movie plot.<br>Make sure that the provided URL is from https://subslikescript.com/ database.

# Required Packages & Downloading Ollama
Download the Ollama through the link:<br>
https://ollama.com/download/OllamaSetup.exe

Run the following command on your command prompt once the Ollama is installed and running in the system tray:<br>
ollama run llama3.2

Open the terminal on your device and run the following command to download the needed python packages:<br>
pip install beautifulsoup4 requests


