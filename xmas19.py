def main():
	sub_dict=dict()
	for line in open("input19.txt"):
		# print line
		(compound, _, sub)=line.split()
		if compound in sub_dict.keys():
			sub_dict[compound].append(sub)
		else:
			sub_dict[compound]=[sub]	
	input_data="ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
	array=[]
	print sub_dict
	for letter in range(len(input_data)-1):
			if input_data[letter].islower():
				if input_data[letter]=='e':
					string=input_data[:letter]+sub_dict[input_data[letter]][sub]+input_data[letter+1:]
					array.append(string)
					print string
			elif input_data[letter].isupper() and input_data[letter+1].islower() and not input_data[letter+1]=='e' and input_data[letter]+input_data[letter+1] in sub_dict.keys():
				for sub in sub_dict[input_data[letter]+input_data[letter+1]]:
					string=input_data[:letter]+sub+input_data[letter+2:]
					array.append(string)
					print string
			elif input_data[letter].isupper() and input_data[letter] in sub_dict.keys():
				for sub in sub_dict[input_data[letter]]:
					string=input_data[:letter]+sub+input_data[letter+1:]
					array.append(string)
					print string
				
	if input_data[-1] in sub_dict.keys():
		for sub in sub_dict[input_data[-1]]:
			string=input_data[0:-1]+sub
			array.append(string)
			print string					
						
	print len(set(array))		
main()


#{'Mg': ['BF', 'TiMg'], 'B': ['BCa', 'TiB', 'TiRnFAr'], 'e': ['HF', 'NAl', 'OMg'], 'F': ['CaF', 'PMg', 'SiAl'], 'H': ['CRnAlAr', 'CRnFYFYFAr', 'CRnFYMgAr', 'CRnMgYFAr', 'HCa', 'NRnFYFAr', 'NRnMgAr', 'NTh', 'OB', 'ORnFAr'], 'Ca': ['CaCa', 'PB', 'PRnFAr', 'SiRnFYFAr', 'SiRnMgAr', 'SiTh'], 'Al': ['ThF', 'ThRnFAr'], 'O': ['CRnFYFAr', 'CRnMgAr', 'HP', 'NRnFAr', 'OTi'], 'N': ['CRnFAr', 'HSi'], 'P': ['CaP', 'PTi', 'SiRnFAr'], 'Si': ['CaSi'], 'Th': ['ThCa'], 'Ti': ['BP', 'TiTi']}













