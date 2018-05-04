
from math import sqrt

class Query:


	def __init__( self ):

		self.query = ""
		self.index = {}
		self.normalizeIndex = {}
		self.IDFs = {}
		self.weights = {}
		self.norm = 0
		self.normalizeNorm = 0
		self.normalizeWeights = {}


	def add( self, querySTR, stmDic ): # Añado la consulta y un diccionario resultante del stemmer( raíz / nº de veces que aparece)
		
		self.index = stmDic.copy()
		self.query = querySTR



	def normalize( self ): # Normaliza la consulta

		aux = max( self.index.values() ) # Obtengo el mayor de los valores del dicionario( el número de la paralabra
						 # qué más veces sale
		for di, vi in self.index.items():

			self.normalizeIndex[di] = vi/aux # Divido todos los valores del diccionario por el máximo



	def weightsCalc( self ): # Calula los pesos

		for dick, dicv in self.normalizeIndex.items(): # Itero en el TF normalizado

			if dick in self.IDFs:

				self.weights[dick] = dicv * self.IDFs[dick] # Multiplico los TFn por sus IDFs
		

	def normCalc( self ): # Calcula la norma para los pesos normalizados

		for wthsk, wthsv in self.weights.items(): # Itero en los pesos

			self.norm += pow( wthsv, 2 ) # Elevo al cuadrado los pesos y los voy acumulando

		self.norm = sqrt( self.norm ) # Finalmente hago la raíz cuadrada de la suma acumulada
	

	def normalizeWeightsCalc( self ): # Calcula los pesos normalizados

		for wthsk, wthsv in self.weights.items(): # Itero en los pesos

			self.normalizeWeights[wthsk] = wthsv / self.norm # Divido los pesos por la norma


	def normalizeNormCalc( self ):

		for wthsk, wthsv in self.normalizeWeights.items(): # Itero en los pesos normalizados

			self.normalizeNorm += pow( wthsv, 2 ) # Elevo al cuadrado los pesos y los voy acumulando

		self.normalizeNorm = sqrt( self.normalizeNorm ) # Finalmente hago la raíz cuadrada de la suma acumulada
		
			
