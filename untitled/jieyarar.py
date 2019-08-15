from unrar import rarfile
#rarfile.RarFile('')
file = rarfile.RarFile('C:/untitled/download/桭源鑫汇3号私募证券投资基金20190620.rar')
file.extractall(path='C:/untitled/un/')
rarfile.is_rarfile()