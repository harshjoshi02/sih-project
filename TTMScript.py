import openai
import ModelAccessManager
import ResultParser

prompt = "estimate using industry averages the amount of precious metals recovered from {ModelName} on recycling, DO NOT GIVE ANY EXTRA TEXT, calculate the rough estimate and write numerical values, calculate price in {unit}, calculate total possible earning as TPE."
openai.api_key = ModelAccessManager.returnvalidkey(None)

def query_openai(prompt):
  response =  openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[
    {
     "role": "user", 
     "content": prompt
     }
     ], 
  temperature=0
  )
  print('----------------')
  return response["choices"][0]["message"]["content"]


def run_query(model_name,unit):
  formatted_prompt = prompt.format(ModelName=model_name, unit=unit)
  result = query_openai(formatted_prompt)
  ParseValidation,jsondata=ResultParser.JSONParse(result)
  return result

