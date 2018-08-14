from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    agent = Agent("../config/fund_domain.yml",
                  policies=[MemoizationPolicy(), KerasPolicy()])

    agent.visualize("../data/fund_stories.md",
                    output_file="fund_story_graph.png", max_history=2)
