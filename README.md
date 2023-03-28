# Voice-Assistant-with-GPT-Dalle
We all know the capacity of ChatGPT to generate text based response for your commands and Dalle to bring your imagination in to pictorial representation. But, in this use-case I'm taking voice based commands as input and respond back visually and voice mode.

My voice assistant name is isha as tested <a href="https://www.instagram.com/reel/CZnG7Y0jRbc/">here</a>. I will be integrating same with powerful GPT & Dalle from OpenAI.

Typical process, 
1. PyAudio to play and record the audio
2. We have used google speech recognition library to process speech to text.
3. Python text to audio to convert response from GPT to voice.
4. OpenAI to connect with 2 & 3.
5. Save the request to analyze further using NLP like this <a href="https://github.com/iamBHK/Sentiment-Analysis-to-Dataframe">model</a>

To run this program, 
1. Just download and add new folder AllImages.
2. Create your own virtual assistant.
3. Install PyAudio, SpeechRecognition, pyttsx3, OpenAI, JSON.
4. Execute GPT_speech_recognition.py file to test this use-case.
