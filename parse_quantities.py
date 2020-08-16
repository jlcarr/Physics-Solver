import spacy
nlp = spacy.load("en_core_web_sm")

def parse_quantities(question_text):
	"""
	Parse numerical quantities and their units from text.

	Parameters
	----------
	question_text : str
		English text describing a physics problem with quantities specified.

	Returns
	-------
	>>> parse_quantities("An emu runs at 50 km/hr, how long does it take it to run 1 kilometer east?")
	
	"""
	doc = nlp(question_text)
	found_quantities = []
	for token in doc:
		if token.pos_ == 'NUM':
			value = token.text
			units = None
			if token.dep_ == 'nummod':
				units = token.head.text
				units_token = token.head
				while units_token.dep_ == 'nmod':
					units_token = units_token.head
					units += ' ' + units_token.text
			found_quantities.append({'value': token.text, 'units': units})
	return found_quantities

if __name__=="__main__":
	print(parse_quantities("An emu runs at 50 km/hr, how long does it take it to run 1 kilometer east?"))
