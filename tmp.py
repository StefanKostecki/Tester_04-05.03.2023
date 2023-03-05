import datetime

teraz = datetime.datetime.now()
print(teraz)
print(type(teraz))

print(teraz.strftime('Godzian = %H, a minuta  %M  %S  %Y'))