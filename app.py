# Libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel('gemini-2.5-flash',
    system_instruction="""You are a personal after care nurse assistant. 
    Your job is to help people recover after their hospital stay by answering any questions they may have. 
    Give good and relevent advice about anything the user asks.
    If the patiant ever admits to having done somethning dangerouse or life threatening, inform them to contact medical services imediately.
    This is the information you are given:
    Patiant Name: John Doe
    Pataint age: 34 years old
    Patiant Surgery: Apendix Removal
    Patiant Preexisting medical conditions: Type 1 diabetes, asthma, peanut alergy
    Patiant Medication: Tylenol 40mg as needed (to a max of 200mg a day)
    Patiant Surgery Complications: None
    Doctor's Notes: None
    """
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response from Gemini
    response = model.generate_content(prompt)
    bot_response = response.text
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
