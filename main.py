class Ricecooker:
  jumlah = 0
  def __init__(self,nama_merk,tuas,mode): 
    self.nama_merk = nama_merk
    self.tuas = tuas 
    self.mode = mode
    Ricecooker.jumlah += 1
    print('jumlah mode ricecooker :' + self.mode)

class TypeRicecooker:
  def __init__(self,temperature):
    self.temperature = temperature
    self.temperaturesekarang = self.temperature + 50
    print('Temperature Ricecooker sekarang = ', self.temperaturesekarang)

class ModernRicecooker: 
  def __init__(self,nama_merk,tuas,mode,temperature):
    Ricecooker.__init__(self,nama_merk,tuas,mode)
    TypeRicecooker.__init__(self, temperature)

YoungMa= ModernRicecooker('YoungMa', 'ON', 'Cook',100)
print(YoungMa.nama_merk)
print(YoungMa.tuas)
print(YoungMa.mode)
print(YoungMa.temperature)
print(Ricecooker.jumlah)

print('______________________________________________')
Cosmo= ModernRicecooker('Cosmo', 'OFF', 'Warm', 70)
print(Cosmo.nama_merk)
print(Cosmo.tuas)
print(Cosmo.mode)
print(Cosmo.temperature)
print(Ricecooker.jumlah)
print('______________________________________________')



