import os
import json

def JSONParse(response):
    dataobj,start_location=None,None
    partial_parse_flag=False
    improper_parse_flag=False
    if response.find('|')!=-1:
        start_location=response.find('|')
        end_location=response.find('|', start_location+1)
        if end_location==-1:
            end_location=len(response)
            partial_parse_flag=True
        jsontext=response[start_location:end_location]
        try:
            dataobj=json.loads(jsontext)
        except Exception as e:
            print(e)
            improper_parse_flag=True
    else:
        improper_parse_flag=True
    if dataobj!=None and improper_parse_flag==False:
        return (True,dataobj)
    else:
        if start_location !=None:
            return (False,response[:start_location])
        else:
            return (False,None)

    