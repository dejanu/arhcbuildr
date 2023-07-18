#!/usr/bin/env python3

import openai
import os

openai.api_key = os.getenv("OPEN_API_KEY")

# get the models names from the list
available_models = openai.Model.list()
model_names = [model['id'] for model in available_models['data']]
print(f"{model_names} \n Prompt: ")

# read the prompt string from STDIN
iprompt = input()

# set the temperature high for more creative results
# set the max_tokens low for faster results
response = openai.Completion.create(
            model="text-davinci-003",
            prompt=iprompt,
            temperature=0.5,
            max_tokens=100,
            echo=True,
        )

print(response.choices[0].text)

