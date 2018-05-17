
from modules.tokenizer_module import Tokenizer

from modules.stopper_module import Stopper

from modules.stemmer_module import Stemmer

from modules.index import Index

from modules.query import Query

import _pickle as pickle

import operator


if __name__ == "__main__":


	
	querySTR = ""
	
	while querySTR == "" or querySTR == " ":

		querySTR = input( "Introduzca la consulta: " )


	tokenizer = Tokenizer( querySTR )

	tokenizer.tokenize()

	stopper = Stopper()

	stopper.stopping( tokenizer.tokens  )

	stemmer = Stemmer()

	stemmer.stemming( stopper.stoppedList )

	query = Query()

	query.add( querySTR, stemmer.stmDic )


	query.normalize()

	seriObject = open( "/home/anonymous/Desktop/serializable_object/index", "rb" )

	index = pickle.load( seriObject )

	seriObject.close()

	query.IDFs = index.IDFs

	query.weightsCalc()

	query.normCalc()

	query.normalizeWeightsCalc()

	query.normalizeNormCalc()
	index.normalizeNormCalc()

	###Cálculo de la Similitud
	sim = {}

	
	for inw, val in enumerate(index.normalizeWeights):

		summ = 0

		for iqnw in query.normalizeWeights:

			if iqnw in val:

				summ += query.normalizeWeights[iqnw] * val[iqnw]

		calc = summ / (index.norm[inw] * query.normalizeNorm)

		if calc != 0:

			sim[index.nameIndex[inw]] = calc


	
	

	result = sorted( sim.items(), key = operator.itemgetter(1) )

	result.reverse()

	#print( result )

	###Pseudorealimentación por relevancia (PRF)

	newWords = []	
	
	for i in range( 5 ):

		aux = index.index[ index.nameIndex.index( result[i][0] ) ]

		aux = sorted( aux.items(), key = operator.itemgetter(1) )
		
		aux.reverse()

		for j in range( 5 ):

			querySTR += " " + aux[j][0]



	tokenizer = Tokenizer( querySTR )

	tokenizer.tokenize()

	stopper = Stopper()

	stopper.stopping( tokenizer.tokens  )

	stemmer = Stemmer()

	stemmer.stemming( stopper.stoppedList )

	query = Query()

	query.add( querySTR, stemmer.stmDic )

	query.normalize()

	query.IDFs = index.IDFs

	query.weightsCalc()

	query.normCalc()

	query.normalizeWeightsCalc()

	query.normalizeNormCalc()
	index.normalizeNormCalc()

	###Cálculo de la Similitud
	sim = {}

	
	for inw, val in enumerate(index.normalizeWeights):

		summ = 0

		for iqnw in query.normalizeWeights:

			if iqnw in val:

				summ += query.normalizeWeights[iqnw] * val[iqnw]

		calc = summ / (index.norm[inw] * query.normalizeNorm)

		if calc != 0:

			sim[index.nameIndex[inw]] = calc


	
	

	result = sorted( sim.items(), key = operator.itemgetter(1) )

	result.reverse()

	print( "Los documentos más relevantes son (documento/similitud):" )

	for idn in range( 5 ):

		print( result[idn] )



