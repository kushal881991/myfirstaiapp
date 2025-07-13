import streamlit as st
import Tweet_Generator as backend

st.header("Tweet Generator")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of Tweets",1,10);

if st.button("Generate"):
    response = backend.tweet_chain.invoke({"topic" : topic ,"number" :number});
    st.write(response.content);