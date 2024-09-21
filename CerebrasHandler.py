import requests
import os
import openai

class CerebrasHandler:
    '''
    Handler for interacting with the Cerebras API
    '''
        
    def __init__(self, model_name):
        """
        """
        self.CEREBRAS_URL = 'https://api.cerebras.ai/v1'
        self.model_name = model_name
        self.api_keys = [
            os.environ.get("THOMAS_API_KEY")
        ]
        self.current_key_index = 0
        self.current_client = openai.OpenAI(
            base_url=self.CEREBRAS_URL,
            api_key=self.api_keys[self.current_key_index]
        )

    def _rotate_api_key(self):
        """Cycle to the next API key in the list."""
        self.current_client.close()
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        self.current_client = openai.OpenAI(
            base_url=self.CEREBRAS_URL,
            api_key=self.api_keys[self.current_key_index]
        )

        print("_get_next_api_key called")
        return self.api_keys[self.current_key_index]

    def _make_api_call(self, messages, params=None):
        '''
        Internal function to make a chat completion call to Cerebras
        '''
        # Try to make a request to the Cerebras chat completion API
        try:
            response = self.current_client.chat.completions.create(messages=messages, model=self.model_name)
            return response.choices[0].message.content
        except requests.exceptions.RequestException as e:
            print(f"Error making API call: {e}")
            return None

    def call_api(self, messages, params=None):
        '''
        Public function to make a call to Cerebras API.
        This function will rotate to the next key if the currently active
        api key has reached its limit.
        '''
        attempts = 0
        while attempts < len(self.api_keys):
            result = self._make_api_call(messages=messages, params=params)
            if result is not None:
                return result
            self._rotate_api_key()
            attempts += 1
        print("NO API CALLS MADE")
        return None
