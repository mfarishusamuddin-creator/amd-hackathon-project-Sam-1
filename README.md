LafazAI — Bridging Pronunciation Across Languages

AMD Developer Hackathon: ACT II — Track 3 (Unicorn / Open Innovation)

LafazAI is an AI-powered pronunciation coach that helps language learners understand why a sound is hard for them — and how to say it — by bridging it to the sounds they already know in their native language, using the International Phonetic Alphabet (IPA).

Problem

Many sounds in a target language simply don't exist in a learner's native language. For example, the Arabic letter ث represents the sound /θ/ — the same sound as English "th" in think — which has no equivalent in Indonesian. Learners often substitute /t/ or /s/, making "think" sound like "tink" or "sink."

How It Works


Input: the user provides their native language, the language they're learning, and the specific sound, letter, or word they struggle with.
AI Bridge: an LLM (via Fireworks AI, running on AMD-hosted inference) analyzes the sound, maps it to its IPA symbol, and explains how it relates — or doesn't — to a sound the learner already knows.
Output: a clear, structured explanation covering the IPA symbol, the closest native-language equivalent (or an explicit note that none exists), mouth/tongue positioning, example words, and one practice tip.


Example Output

Input: native = Indonesian, target = English, sound = the letter ث

IPA Symbol: /θ/ — voiceless dental fricative
Native-Language Bridge: No close equivalent in Indonesian — learners often
  substitute /t/ or /s/
Mouth Position: Tongue tip between the teeth, steady airflow, no vocal cord
  vibration
Example Words: think · three · thank · thumb · bath
Practice Tip: "sssss" → slide tongue forward → "thhhh"

Built On AMD

This project runs end-to-end inside an AMD Developer Cloud Jupyter notebook:


Environment: ROCm 7.2 + PyTorch 2.9 (AMD Developer Cloud notebook instance)
Inference: Fireworks AI API (minimax-m3), served on AMD-hosted infrastructure
Interface: Python function, callable directly or via a simple UI


Tech Stack

ComponentTechnologyComputeAMD Developer Cloud (ROCm 7.2, PyTorch 2.9)InferenceFireworks AI API — minimax-m3LanguagePython 3

Setup & Usage


Open a notebook on notebooks.amd.com/hackathon (or any environment with Python 3).
Install dependencies:


bash   pip install openai gradio


Set your Fireworks AI API key (get one at app.fireworks.ai):


python   import os
   os.environ["FIREWORKS_API_KEY"] = "your-api-key-here"


Run lafazai_starter.py (or copy its cells into a notebook, one section per cell).
Call the core function directly:


python   print(get_pronunciation_bridge("Indonesian", "English", "the letter ث"))

Project Structure

.
├── lafazai_starter.py   # Core pipeline: Fireworks client, prompt logic, optional Gradio UI
└── README.md

Who It's For


Language learners practicing sounds their native language doesn't have
Immigrants & expats building confidence to be understood in a new country
Students preparing for English or Arabic proficiency exams
Travelers learning to say key phrases correctly, fast


Future Directions


Audio input with real-time pronunciation scoring
Expanded language pair coverage
Classroom / group learning mode


Team

Solo submission — AMD Developer Hackathon: ACT II, Track 3.

License

MIT
