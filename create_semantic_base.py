# from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence
#
# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle
#
# sentences = LineSentence(path)# path为要训练的txt的路径
#
# # 对sentences表示的语料库进行训练
# model = Word2Vec(sentences, sg=0, size=50, window=5, min_count=3, hs=1)
# # model = Word2Vec(sentences, size=200, window=5, min_count=5)
#
# model.save(model_path) #model_path为模型路径。保存模型，通常采用pkl形式保存，以便下次直接加载即可
#
# # 加载模型
# model = Word2Vec.load(model_path)
