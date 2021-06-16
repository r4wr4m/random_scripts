import glob, os
#os.chdir("C:/path/")
for FileName in glob.glob("**/*.txt", recursive = True):
    print(FileName)

    with open(FileName, 'r',encoding='utf8') as f:
        newText=f.read()
        
    newText=newText.replace('Ä…','ą')
    newText=newText.replace('Ä‡','ć')
    newText=newText.replace('Ä™','ę')
    newText=newText.replace('Ĺ‚','ł')
    newText=newText.replace('Ĺ›','ś')
    newText=newText.replace('Ĺš','Ś')
    newText=newText.replace('Ĺ„','ń')
    newText=newText.replace('Ăł','ó')
    newText=newText.replace('Ĺş','ź')
    newText=newText.replace('ĹĽ','ż')
    newText=newText.replace('â€ž','\'')
    newText=newText.replace('â€ť','\'')
    newText=newText.replace('ď»ż','')

    with open(FileName, "w",encoding='utf8') as f:
        f.write(newText)
