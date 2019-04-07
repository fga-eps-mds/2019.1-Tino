#!/bin/sh
python -m rasa_nlu.train -c nlu/nlu_config.yml --data nlu/nlu_data.md -o models --fixed_model_name nlu --project current --verbose
python -m rasa_core.train -d core/domain.yml -s core/stories.md -o models/current/dialogue
python -m rasa_core_sdk.endpoint --actions actions

