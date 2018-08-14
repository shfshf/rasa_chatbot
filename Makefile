help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run"
	@echo "        Spin up a server that serves as an endpoint to receive webchat user messages."

train-nlu:
	python -m rasa_nlu.train -c config/nlu/demo/fund_nlu.yml --fixed_model_name current --data data/nlu/demo/fund_nlu.md --path models/nlu/ --project demo
# 生成models文件，产生rasa_nlu模型

nlu-server:
	python -m rasa_nlu.server --path models/nlu/
	curl -v -XPOST localhost:5000/parse -d '{"q":"hi","project":"demo","model":"current"}'

evaluate-nlu:
	python -m rasa_nlu.evaluate  --model models/nlu/demo/current --data data/nlu/demo/fund_nlu.md

Visualization of Stories:
	python -m rasa_core.visualize -d config/dialogue/demo/fund_domain.yml -s data/dialogue/demo/fund_stories.md -o fund_story_graph.png -m 2
# 生成fund_story_graph.png

train-core:
	python -m rasa_core.train -s data/dialogue/demo/fund_stories.md -d config/dialogue/demo/fund_domain.yml -o models/dialogue/demo --epochs 500
# rasa_core.train

run-cmdline:
	python -m rasa_core.run -d models/dialogue/demo -u models/nlu/demo/current
#cmd学习

core-server:
	python -m rasa_core.server -d models/dialogue/demo -u models/nlu/demo/current -o out.log
# 输出log

run-webchat:
	python webchat.py

