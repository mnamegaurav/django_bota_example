import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import UbuntuCorpusTrainer
from django.conf import settings

# Creating ChatBot Instance
bota = ChatBot(**settings.CHATTERBOT)

logging.basicConfig(level=logging.INFO)

training_data_que_ans = open(f'{settings.BASE_DIR}/bot/static/bota/que_ans.txt').read().splitlines()
training_data_personal = open(f'{settings.BASE_DIR}/bot/static/bota/training_data.txt').read().splitlines()

training_data = training_data_que_ans + training_data_personal

trainer = ListTrainer(bota)
trainer.train(training_data)

trainer_corpus = ChatterBotCorpusTrainer(bota)
trainer_corpus.train('chatterbot.corpus.english') 

# ubuntu_corpus_trainer = UbuntuCorpusTrainer(bota)
# ubuntu_corpus_trainer.train()
