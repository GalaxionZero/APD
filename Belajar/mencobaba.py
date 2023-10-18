prodi = {
    'prodi1' : 'Informatika',
    'prodi2' : 'Arsitektur',
    'prodi3' : 'Sistem Informasi'
}


prodi['prodi4'] = 'Kedokteran'

prodi.update({'prodi2' : 'Kedokteran Gigi'})

del prodi['prodi3']

print(prodi.keys())

print(prodi.values())