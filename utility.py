# -*- coding: utf-8 -*-

from settings import *
from agents.CordinatorAgent import CordinatorAgent
from agents.StudentAgent import StudentAgent
from agents.VotingAgent import Voting
from states import StateDiscussion, StateVoting, StateVotingEnd
import random


def create_cordinator_agent(account_info):
    agent = CordinatorAgent(account_info[0], account_info[1])
    agent.set_agent_details(CORDINATOR_NAME, PROPOSAL)
    CORDINATOR.append(agent)
    future = agent.start()
    future.result()


def create_student_agent(account_info, i):
    agent = StudentAgent(account_info[0], account_info[1])
    new_priorities = random.sample(PRIORITIES, len(PRIORITIES))
    agent.set_agent_details("ST00" + str(i), new_priorities)
    AGENTS.append(agent)
    future = agent.start()
    future.result()


def create_voting_agent(account_info):
    voting = Voting(account_info[0], account_info[1])
    VOTING.append(voting)
    future = voting.start()
    voting.fsm.add_state(name=STATE_ONE, state=StateDiscussion(), initial=True)
    voting.fsm.add_state(name=STATE_TWO, state=StateVoting())
    voting.fsm.add_state(name=STATE_THREE, state=StateVotingEnd())
    voting.fsm.add_transition(source=STATE_ONE, dest=STATE_TWO)
    voting.fsm.add_transition(source=STATE_TWO, dest=STATE_THREE)
    voting.add_behaviour(voting.fsm)
    future.result()


def print_agent_preferences(agents):
    for agent in agents:
        print(f"({agent.name}) : My choice candidates in order of preference are: \n")
        for candidate in agent.priorities:
            print("\t"+ candidate + "\n")
        
        
class RunoffVoting:
    def give_votes(self, priorities):
        choices = []
        votes = {}

        for priority in priorities:
            choices.append(priority)

        for choice in choices:
            votes[choice] = 0

        return votes

    def calculate_votes(self, votes, agents):
        votes_first_circle = first_circle_runoff(votes, agents)

        print(
            f"\nThe second round of voting includes {votes_first_circle[0][0]} and {votes_first_circle[1][0]} "
        )

        votes_first_circle = dict((x, y) for x, y in votes_first_circle)
        votes_first_circle = dict(list(votes_first_circle.items())[0:2])

        return second_circle(votes_first_circle, agents)


def first_circle_runoff(votes, agents):
    for agent in agents:
        votes[agent.priorities[0]] += 1
        agent.vote_for = agent.priorities[0]

    votes = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)

    print(f"\nWinner of the first round is: {votes[0][0]} with {votes[0][1]} votes")

    return votes


def second_circle(votes, agents):
    votes = {x: 0 for x in votes}
    for agent in agents:
        if agent.priorities[0] in votes:
            votes[agent.priorities[0]] += 1
            agent.vote_for = agent.priorities[0]
            continue
        if agent.priorities[1] in votes:
            votes[agent.priorities[1]] += 1
            agent.vote_for = agent.priorities[1]
            continue
        if agent.priorities[2] in votes:
            votes[agent.priorities[2]] += 1
            agent.vote_for = agent.priorities[2]

    votes = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)
    print(f"\nThe Winner is: {votes[0][0]} with {votes[0][1]} votes\n")

    return votes
