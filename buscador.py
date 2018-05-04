
from modules.tokenizer_module import Tokenizer

from modules.stopper_module import Stopper

from modules.stemmer_module import Stemmer

from modules.index import Index

from modules.query import Query

import _pickle as pickle

import operator


if __name__ == "__main__":



	consulta = "La Asociación Española Contra el Cáncer con sede en Linares, organiza la 3ª edición de NOCHE MÁGICA DORADA,que será el próximo 22 de Octubre a las 8 de la tarde en el Teatro Cervanters de Linares,dónde actuarán grandes artistas, como la gran pianista Marisa Montiel, las sopranos Mº Eugenia Boix,Cecilia Gallego, Susana Jannes y los tenores Joaquín Robles y Francisco Heredia, como pianista acompañante Mariano Hernández. Posteriormente se realizará una cena-cóctel en el Hotel Anibal en dónde habrá un espectáculo flamenco a cargo del Ballet de Mª del Mar Ramírez y Raquel Parrilla."


	tokenizer = Tokenizer( consulta )

	tokenizer.tokenize()

	stopper = Stopper()

	stopper.stopping( tokenizer.tokens  )

	stemmer = Stemmer()

	stemmer.stemming( stopper.stoppedList )

	query = Query()

	query.add( consulta, stemmer.stmDic )

	#print( query.index )

	query.normalize()

	#print( query.normalizeIndex )

	seriObject = open( "/home/anonymous/Desktop/serializable_object/index", "rb" )

	index = pickle.load( seriObject )

	seriObject.close()

	query.IDFs = index.IDFs

	#print( indexQ.IDFs)

	query.weightsCalc()

	#print( query.weights )

	#print( max(query.weights.values()) )

	query.normCalc()

	#print( query.norm )

	query.normalizeWeightsCalc()

	#print( query.normalizeWeights )

	sim = {}
	
	for inw, val in enumerate(index.normalizeWeights):

		summ = 0

		for iqnw in query.normalizeWeights:

			if iqnw in val:

				summ += query.normalizeWeights[iqnw] * val[iqnw]

		calc = summ / (index.norm[inw] * query.norm)

		if calc != 0:

			sim[index.nameIndex[inw]] = calc


	
	

	result = sorted( sim.items(), key = operator.itemgetter(1) )

	result.reverse()

	print( result )
