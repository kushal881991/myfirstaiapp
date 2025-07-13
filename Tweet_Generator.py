
#Using Google Gemini Models(Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

import os

os.environ['GOOGLE_API_KEY']="AIzaSyD289M10wE0rlJGqPpN7AcjvSRjeQ-WWAo";

#Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash");

response = gemini_model.invoke("Give me 3 tweets onWorld War 1");

print(response.content);


#from prompt template


#create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template,input_variables=['number','topic']);

tweet_template.format(number=7,topic="Submarine");


#from LLM Chains


#Create a LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

response = tweet_chain.invoke({"number" : 5 ,"topic" :"Wars in middle East"});

print(response.content)





