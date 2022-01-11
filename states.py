# -*- coding: utf-8 -*-
import json,time
from spade.behaviour import State
from spade.message import Message
from settings import *
import utility

class StateDiscussion(State):
    async def run(self):
        print("\nWe shall all vote for the student representative of choice in order of preference.\n")
        self.set_next_state(STATE_TWO)
        utility.print_agent_preferences(AGENTS)

        time.sleep(PAUSE)


class StateVoting(State):
    async def run(self):
        print("\nAll students have voted.")
        votes = utility.RunoffVoting.give_votes(self,PRIORITIES)

        msg = Message(to=str(self.agent.jid))
        msg.body = f"{votes}"
        await self.send(msg)
        self.set_next_state(STATE_THREE)

        time.sleep(PAUSE)


class StateVotingEnd(State):
    async def run(self):
        print("\nVoting is over.")
        msg = await self.receive(timeout=5)
        votes = json.loads(msg.body.replace("'", '"'))
        utility.RunoffVoting.calculate_votes(self, votes, AGENTS)

        time.sleep(PAUSE)
