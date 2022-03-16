texto =str(input())
inicialNombre = texto.find("'name'>")
finalNombre = texto.find("</div><")

inicioApellido = texto.find("lastname'>")
finalApellido = texto.rfind("</div>")

textoFinal1 = texto[inicialNombre+7:finalNombre]
textoFinal2 = texto[inicioApellido+10:finalApellido]
print(textoFinal1+textoFinal2)