from CerebrasHandler import CerebrasHandler
import os


class Spawn():
    def __init__(self, identity):
        api_keys=[
            os.environ.get("THOMAS_API_KEY") if os.environ.get("THOMAS_API_KEY") else "",
            os.environ.get("JET_API_KEY") if os.environ.get("JET_API_KEY") else ""
        ]
        self.cerebras_handler = CerebrasHandler("llama3.1-70b", api_keys=api_keys)
        self.backstory = self.generate_backstory(identity)
        
    def generate_backstory(self, identity):
        messages=[
            {
                "role": "system",
                "content": '''Create a human-like backstory emphasizing realism with fully fleshed out details, character and personality traits, based on the provided characteristics:''',
            },
            {
                "role": "user",
                "content": identity,
            }
        ]

        response = self.cerebras_handler.call_api(messages=messages)

        # response = client.chat.completions.create(
        #     messages=[
        #         {
        #             "role": "system",
        #             "content": '''Create a human-like backstory emphasizing realism with fully fleshed out details, character and personality traits, based on the provided characteristics:''',
        #         },
        #         {
        #             "role": "user",
        #             "content": identity,
        #         }
        #     ],
        #     model="llama3.1-70b",
        #     stream=False,
        # )
        return response['choices'][0]['message']['content']
    
person = Spawn("A blonde dude named Joe")

print(person.backstory)

