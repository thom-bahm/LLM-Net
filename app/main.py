from Network import Network

task = '''Breaking News! Donald Trump will launch his own cryptocurrency.'''
agent_network = Network(task, "Texas", 5)
agent_network.group_chat("round_robin", 1)