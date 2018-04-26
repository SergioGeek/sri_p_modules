
from modules.tokenizer_module import Tokenizer

from modules.stopper_module import Stopper

from modules.stemmer_module import Stemmer

from modules.index import Index

import _pickle as pickle

import operator


if __name__ == "__main__":



	consulta = "loco"

	tokenizer = Tokenizer( consulta )

	tokenizer.tokenize()

	stopper = Stopper()

	stopper.stopping( tokenizer.tokens  )

	stemmer = Stemmer()

	stemmer.stemming( stopper.stoppedList )

	indexQ = Index()

	indexQ.add( "loco", stemmer.stmDic )

	indexQ.normalize()

	seriObject = open( "/home/anonymous/Desktop/serializable_object/index", "rb" )

	index = pickle.load( seriObject )

	seriObject.close()

	indexQ.IDFs = index.IDFs

	indexQ.weightsCalc()

	indexQ.normCalc()

	indexQ.normalizeWeightsCalc()

	i = 0

	

	sim = {}
	
	for inw, val in enumerate(index.normalizeWeights):

		summ = 0

		for iqnw in indexQ.normalizeWeights[0]:

			if iqnw in val:

				summ += indexQ.normalizeWeights[0][iqnw] * val[iqnw]

		calc = summ / (index.norm[inw] * indexQ.norm[0])

		if calc != 0:
			sim[index.nameIndex[inw]] = calc


	
	

	result = sorted( sim.items(), key = operator.itemgetter(1) )

	result.reverse()

	print( result )
