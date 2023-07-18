#!/usr/bin/env python3


from langchain.llms import OpenAI

import os

OPENAI_API_KEY = os.environ.get('OPEN_API_KEY')
print(OPENAI_API_KEY)

# higher temperature = more creative
# lower temperature = more predictable
llm = OpenAI(openai_api_key=OPENAI_API_KEY,temperature=0.9)

# get predictions
print(llm.predict('The quick brown fox', max_tokens=5))
