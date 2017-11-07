import os
import json
import logging

VALID_EXTENSIONS = [".JSON"]

class CfgFile(object):

	# > Constructor
	def __init__(self, cfg_file_name):

		self.cfg_file_name = cfg_file_name
		self.file_extension = os.path.splitext(cfg_file_name)[1].upper()

		if self.__validate(cfg_file_name) == False:
			self.content = None
		else:
			self.content = self.__slurp_cfg_file()

	# > PUBLIC ------------------------------------------------------

	#def update_configuration(self):


	# > PRIVATE -----------------------------------------------------

	# > Group of cfg file basic validatons
	def __validate(self, file_name):
		validation_list = [
			self.__file_exists(file_name),
			self.__valid_extension()
		]

		if False in validation_list:
			return False
		else:
			return True

	# > File extension validation function
	def __valid_extension(self):

		if self.file_extension in VALID_EXTENSIONS:
			return True
		else:
			return False

	# > File existence validation function
	def __file_exists(self, file):
		if os.path.isfile(file) == True or os.path.islink(file) == True:
			return True
		else:
			return False

	# > Load all file on one string
	def __slurp_cfg_file(self):
		try:
			with open(self.cfg_file_name) as cfg_content:
				if self.file_extension == ".JSON":
					return json.load(cfg_content)
		except:
			return None
