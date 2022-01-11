# -*- coding: utf-8 -*-

from spade.behaviour import FSMBehaviour
import datetime

class VotingProcess(FSMBehaviour):
    async def on_start(self):
        print(f"\nMeeting begins with {self.current_state} at  {datetime.datetime.now()}")

    async def on_end(self):
        print(f"\nMeeting ends with {self.current_state} at {datetime.datetime.now()}")
