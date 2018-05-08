

import configparser

import os

from os import listdir

from modules.filter_module import Filter

from modules.tokenizer_module import Tokenizer

from modules.stopper_module import Stopper

from modules.stemmer_module import Stemmer

from modules.index import Index

import _pickle as pickle

from time import time




if __name__ == "__main__":
		


	stt_t = time()
	# Lectura de archivo de configuración
	confg_file = configparser.ConfigParser()
	confg_file.read(os.path.dirname(os.path.abspath(__file__)) + "/config.cfg")

	
	if "coleccionESuja2018cleaned" not in listdir(confg_file["PATHS"]["WritingPath"]): # Si ya está, el directorio no se crea
		os.mkdir(confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018cleaned")

	if "coleccionESuja2018stopper" not in listdir(confg_file["PATHS"]["WritingPath"]):
		os.mkdir(confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018stopper")

	if "coleccionESuja2018stemmer" not in listdir(confg_file["PATHS"]["WritingPath"]):
		os.mkdir(confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018stemmer")

	if "serializable_object" not in listdir(confg_file["PATHS"]["WritingPath"]):
		os.mkdir(confg_file["PATHS"]["WritingPath"] + "serializable_object")

	n_ficheros = 0

	n_tokens = 0

	n_tokens_stp = 0

	minimo = 10000000000
	maximo = 0
	minimo_stp = 100000000
	maximo_stp = 0

	stopper = Stopper()
	stemmer = Stemmer()

	index = Index()
	

	for arch in listdir(confg_file["PATHS"]["ReadingPath"]):
		
		n_ficheros += 1

		arch_cleaned = confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018cleaned/" + arch[0:8] + ".txt"
		arch_stopped = confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018stopper/" + arch[0:8] + ".txt"
		arch_stemmed = confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018stemmer/" + arch[0:8] + ".txt"

		fich = open( confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018/" + arch, "r" )
		filtro = Filter( fich )
		fich.close()
		filtro.filter()

		tokenizer = Tokenizer( filtro.text )
		tokenizer.tokenize()
		n_tokens += len( tokenizer.tokens )
		if len( tokenizer.tokens ) < minimo : minimo = len( tokenizer.tokens )
		if len( tokenizer.tokens ) > maximo : maximo = len( tokenizer.tokens )

		fich_cleaned = open( arch_cleaned, "w" )
		for tk in tokenizer.tokens:
			fich_cleaned.write( tk + "\n" )
		fich_cleaned.close()
		
		stopper.stopping( tokenizer.tokens )
		n_tokens_stp += len( stopper.stoppedList )
		if len(stopper.stoppedList) < minimo_stp : minimo_stp = len( stopper.stoppedList )
		if len(stopper.stoppedList) > maximo_stp : maximo_stp = len( stopper.stoppedList )

		fich_stopped = open( arch_stopped, "w" )
		for tk in stopper.stoppedList:
			fich_stopped.write( tk + "\n" )
			
		fich_stopped.close()
	
		stemmer.stemming (stopper.stoppedList )
		
		fich_stemmed = open( arch_stemmed, "w" )
		for stmW in stemmer.stmDic:
			fich_stemmed.write( stmW + "\n" )
			
		fich_stemmed.close()

		index.add( arch[0:8], stemmer.stmDic, filtro )
		
		stopper.stoppedList.clear()
		stemmer.stmDic.clear()



	
	index.normalize()

	index.wordInDocCalc()

	index.idfCalc()

	index.weightsCalc()

	index.normCalc()

	index.normalizeWeightsCalc()


	seObject = open( confg_file["PATHS"]["WritingPath"] + "serializable_object/index", "wb" )

	pickle.dump( index, seObject )

	seObject.close()

	tt_t = time() - stt_t 

		

	print("He seleccionado el Título, Cuerpo, Ruta(Dentro de la página), Tags, Fecha y Autor")
	print("Número de ficheros procesados: " + str(n_ficheros))
	print("Número de tokens totales: Antes(" + str(n_tokens) + ") Después(" + str(n_tokens_stp) + ")" ) 
	print("Número máximo tokens: Antes(" + str(maximo) + ") Después(" + str(maximo_stp) + ")" )
	print("Número mínimo tokens: Antes(" + str(minimo) + ") Después(" + str(minimo_stp) + ")" )
	print("Tokens/Fichero: Antes(" + str(n_tokens/n_ficheros) + ") Después(" + str(n_tokens_stp/n_ficheros) + ")" )
	print("Tiempo: " + str(tt_t))
	

