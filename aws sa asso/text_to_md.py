import os, glob,re
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
                hashes = min(4,tabs) 
                if hashes == 0:
                    hashes = 1
                md_line = (hashes)*'#' + ' ' + (tabs*8)*'&nbsp;' + text.strip() + "\n"
                md_text += md_line
        md_file = 'README.md'
        

        if not os.path.isdir(os.path.join(os.getcwd(), filename.split('.')[0])):
            os.makedirs(os.path.join(os.getcwd(), filename.split('.')[0]))
        with open(filename.split('.')[0]+'/' +md_file,'w') as f2:
            f2.write(md_text)


