import os, glob,re
def change_font(text,tabs):
    enclose = ''
    
    colors = ['#9400D3','#4B0082','#0000FF','#00FF00','#FFFF00','#FF7F00','#FF0000']
    size = 7-tabs
    if tabs>6:
        tabs = 6
    color = colors[6-tabs]
    if size<4:
        size = 4
    
    return f"""{(tabs*8)*'&nbsp;'}<font style='background:{color+'30'}' size='{str(size)}'>{enclose+text+enclose}</font>"""
for filename in glob.glob('*.txt'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        md_text = ""
        # count = 0
        for line in f.readlines():
            # count += 1
            # if count>11:
            #     break
            if line.strip():
                text = line.rstrip()
                by_space = len(re.findall(r'\s\s\s\s',text))
                by_tab = len(re.findall(r'\t',text))
                tabs = by_space if by_space>by_tab else by_tab                
                md_line = text.strip() 
                md_line = change_font(md_line,tabs)
                md_text += md_line + "<br>"
        md_file = 'README.md'
        

        if not os.path.isdir(os.path.join(os.getcwd(), filename.split('.')[0])):
            os.makedirs(os.path.join(os.getcwd(), filename.split('.')[0]))
        with open(filename.split('.')[0]+'/' +md_file,'w') as f2:
            f2.write(md_text)


