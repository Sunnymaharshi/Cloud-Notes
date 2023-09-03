import os, glob,re
def change_font(text,size=3,tabs=1):
    enclose = ''
    # if size>=5:
    #     enclose = "**"
    if size<3:
        size = 3
    return f"<font size='{str(size)}'>{(tabs*8)*'&nbsp;' + enclose+text+enclose}</font>".replace('\"','**')
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
                size = 7-tabs
                md_line = text.strip() 
                md_line = change_font(md_line,size,tabs)
                md_text += md_line + "<br>"
        md_file = 'README.md'
        

        if not os.path.isdir(os.path.join(os.getcwd(), filename.split('.')[0])):
            os.makedirs(os.path.join(os.getcwd(), filename.split('.')[0]))
        with open(filename.split('.')[0]+'/' +md_file,'w') as f2:
            f2.write(md_text)


