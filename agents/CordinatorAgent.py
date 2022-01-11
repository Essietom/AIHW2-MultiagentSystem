# -*- coding: utf-8 -*-

from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from settings import STUDENT_AGENT_EMAIL, CORDINATOR_NAME


class CordinatorAgent(Agent):
    name = CORDINATOR_NAME
    proposal = ""
    vote_for = ""

    def set_agent_details(self, name, proposal):
        self.name = name
        self.proposal = proposal

    class InformBehav(OneShotBehaviour):
        async def run(self):
            print("Student Cordinator speaks: \n")

            msg = Message(to=STUDENT_AGENT_EMAIL)
            msg.set_metadata("performative", "inform")
            msg.body = (
                f"\n We shall be appointing : {self.agent.proposal}"
            )

            await self.send(msg)

    async def setup(self):
        print(f"\nHello! I'm {self.name} , the Student Cordinator for the SE4GD Cohort 1  ")
        b = self.InformBehav()
        self.add_behaviour(b)