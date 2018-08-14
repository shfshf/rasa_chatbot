from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_nlu.model import Metadata, Interpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def run_concertbot_online(input_channel, interpreter,version):
    domain_file = f"./config/dialogue/{version}/fund_domain.yml"
    training_data_file = f'./data/dialogue/{version}/fund_stories.md'
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy()],
                  interpreter=interpreter)

    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=input_channel,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


if __name__ == '__main__':
    import sys
    version = sys.argv[1]
    Interpreter_choice = sys.argv[2] 
    utils.configure_colored_logging(loglevel="INFO")
    run_concertbot_online(ConsoleInputChannel(), RegexInterpreter(
    ) if Interpreter_choice == 0 else Interpreter.load(f'./models/nlu/{version}/current'), version)
