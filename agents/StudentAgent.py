# -*- coding: utf-8 -*-
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.template import Template

class StudentAgent(Agent):
    name = "unknown"
    priorities = []

    def set_agent_details(self, name, priorities):
        self.name = name
        self.priorities = priorities

    class RecvBehav(OneShotBehaviour):
        async def run(self):
            msg = await self.receive(timeout=50)
            if msg:
                print("\nMessage received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")
                await self.agent.stop()

    async def setup(self):
        print(f"\n Hi! I'm {self.name}, an SE4GD student")
        b = self.RecvBehav()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)