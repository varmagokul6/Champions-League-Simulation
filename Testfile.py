#BRACKET GRAPHIC
from Teams import team

Team = team('Tottenham', 0, 0, 0, 0, 0,0, 20)


print(('%-30s %40s')% (Team.name, 'Juventus'))
print(('%-30s %40s')% ('------------', '------------'))
print(('%-30s %40s')% ('Barcelona', 'Dortmund'))

print('\n')
print(('%25s %19s')%('Tottenham', 'Dortmund'))
print(('%25s %25s')% ('------------', '------------'))
print(('%25s %16s')%('Milan', 'ManU'))
print('\n')
print(('%-30s %40s')% ('Milan', 'ManU'))
print(('%-30s %40s')% ('------------', '------------'))
print(('%-30s %40s')% ('Madrid', 'City'))

print(('\n%26s %21s ')% ('Tottenham', 'ManU'))
print(('%26s %21s ')% ('Chelsea', 'PSG'))


print('\n')
print(('%-30s %40s')% ('Napoli', 'Liverpool'))
print(('%-30s %40s')% ('------------', '------------'))
print(('%-30s %40s')% ('Ajax', 'PSG'))

print('\n')
print(('%25s %16s')%('Napoli', 'PSG'))
print(('%25s %25s')% ('------------', '------------'))
print(('%25s %16s')%('Chelsea', 'PSV'))
print('\n')
print(('%-30s %40s')% ('Chelsea', 'Munich'))
print(('%-30s %40s')% ('------------', '------------'))
print(('%-30s %40s')% ('Inter', 'PSV'))

