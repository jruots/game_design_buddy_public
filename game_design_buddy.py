import streamlit as st
import pandas as pd
import numpy as np
import os
import openai
import time

def main():
    st.title('Game Design Buddy')
    st.write('I\'m your Game Design Buddy! \n Please tell me what kind of game design problem you are facing and I will try to help you out!')
    st.write('\nTry for example: \n- What are different ways to matchmake in PvP games? \n- What are different ranking algorithms used for PvP matchmaking? \n- How do you balance in-game economies?')
    prompt = st.text_input('How can I help?')
    if st.button('Generate'):
        st.write('Generating...')
        response = generate(prompt)
        st.write(response)

def generate(prompt):
    openai.api_key = os.environ.get("OPEN_AI_API_KEY")
    response = openai.Completion.create(
        engine=os.environ.get("GAME_DESIGN_BUDDY_MODEL"),
        prompt=prompt,
        temperature=float(os.environ.get("GAME_DESIGN_BUDDY_TEMP")),
        max_tokens=int(os.environ.get("GAME_DESIGN_BUDDY_MAX_TOKENS")),
        top_p=float(os.environ.get("GAME_DESIGN_BUDDY_TOP_P"))
    )
    return response.choices[0].text

if __name__ == "__main__":
    main()