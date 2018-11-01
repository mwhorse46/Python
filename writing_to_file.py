text = "Sample Text to save\n New Line!"

saveFile = open("../../example.txt",'w')
saveFile.write(text)
saveFile.close()
