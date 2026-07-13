import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="LafazAI — Sound Bridge", page_icon="🌉")

# The API key is read from Streamlit "Secrets" (set in app settings), never hardcoded here.
client = OpenAI(
    api_key=st.secrets["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/inference/v1",
)

MODEL_ID = "accounts/fireworks/models/minimax-m3"


def get_pronunciation_bridge(native_lang: str, target_lang: str, sound_or_word: str) -> str:
    system_prompt = (
        "You are a friendly, expert pronunciation coach who helps people "
        "learn sounds in a new language by comparing them to sounds they "
        "already know in their native language, using the International "
        "Phonetic Alphabet (IPA). Always structure your answer clearly as:\n"
        "1. IPA symbol for the target sound\n"
        "2. The closest equivalent sound in the learner's native language "
        "(explain clearly if there is NO close equivalent, since that's the "
        "hardest case for learners)\n"
        "3. Simple, concrete tongue/lips/mouth position instructions\n"
        "4. 2-3 example words in the target language using this sound\n"
        "5. One short, practical practice tip\n"
        "Respond only in English. Keep the tone warm and encouraging, and "
        "keep the whole answer concise."
    )
    user_prompt = (
        f"My native language is {native_lang}. "
        f"I am learning {target_lang}. "
        f"Please help me understand how to pronounce: {sound_or_word}"
    )

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=2000,
        temperature=0.6,
    )
    return response.choices[0].message.content


st.title("🌉 LafazAI")
st.caption("Bridging Pronunciation Across Languages")
st.write(
    "Struggling with an unfamiliar sound? LafazAI bridges the sound in the "
    "language you're learning with a sound you already know in your native "
    "language, using IPA notation and mouth-position guidance. Built on AMD "
    "Developer Cloud (ROCm 7.2, PyTorch 2.9) with inference via Fireworks AI "
    "(AMD-hosted)."
)

with st.form("bridge_form"):
    native_lang = st.text_input("Your Native Language", placeholder="e.g. Indonesian, Arabic")
    target_lang = st.text_input("Language You're Learning", placeholder="e.g. English")
    sound_or_word = st.text_input(
        "Sound / Letter / Word You Want to Learn",
        placeholder="e.g. the letter ث, or 'th' in the word think",
    )
    submitted = st.form_submit_button("Get Pronunciation Guide")

if submitted:
    if not sound_or_word.strip() or not native_lang.strip() or not target_lang.strip():
        st.warning("Please fill in all three fields first.")
    else:
        with st.spinner("Bridging the sound..."):
            result = get_pronunciation_bridge(native_lang, target_lang, sound_or_word)
        st.markdown(result)

st.divider()
st.caption("Built by Faris H — AMD Developer Hackathon: ACT II, Track 3")
