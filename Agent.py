from openai import OpenAI

class Agent:
    def __init__(self, task : str, identity: str, client : OpenAI):
        self.identity = identity
        self.task = task
        self.system_prompt = self._create_system_prompt()
        self.model_name = "llama3.1-70b"
        self.client = client
        self.context = self._init_context()
        

    def _create_system_prompt(self):
        sys_prompt = {
            "role": "system",
            "content": f'''
            You are going to be given a task and an identity.
            With this information, you will 
            This is your task: ###{self.task}###.
            This is your identity: ###{self.identity}###, 
            
            You should behave as your identity suggests, and you should follow the instructions specified by the task closely
            Do not go off topic from your task.
            '''
        }
        
        return sys_prompt
        
    def _init_context(self):
        return [self.system_prompt]
                    
    def talk(self):
        response = self.client.chat.completions.create(
            messages=self.context,
            model=self.model_name,
            stream=False
        )
        agent_reply = response.choices[0].message.content
        self.context.append({"role": "assistant", "content": agent_reply})
        return agent_reply