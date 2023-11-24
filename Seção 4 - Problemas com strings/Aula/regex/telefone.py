a = 'Os nossos telefones de contato são: (98) 555-5555 ou (99)5555-5555 - os telefones são fictícios!'
print(re.findall("\(\d{2}\)\s*\d{3,4}-\d{4}",a))

