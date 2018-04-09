
postsRequest = [ 
	"buscar merchant na falcon",
	"buscar merchant id pelo cnpj no backoffice",
	"pegar o merchat id do cnpj 19516471000176",
]

postsResponse = [ 
	"select * from falcon.merchant",
	"select merchat id from backoffice.merchant where cnpj = @cnpj",
	"select merchat id from merchant where cnpj = '19516471000176'"
]