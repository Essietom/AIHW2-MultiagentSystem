# -*- coding: utf-8 -*-
from spade.agent import Agent
from behaviors import VotingProcess

class Voting(Agent):
    fsm = VotingProcess()

    async def setup(self):
        self.fsm