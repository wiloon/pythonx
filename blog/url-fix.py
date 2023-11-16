import os
import logging

logging.basicConfig(level=logging.DEBUG)
subTitleSet = set([])
articleIndex = 0
for root, dirs, files in os.walk("/home/wiloon/workspace/private/wiloon.com/content/post"):
    logging.debug("file list size: " + str(len(files)))
    for name in files:
        fullName = os.path.join(root, name)
        logging.debug("index: " + str(articleIndex))
        articleIndex = articleIndex + 1

        logging.debug("path: " + fullName)
        lines = []
        out_lines = []
        lineIndex = 0
        title = ''
        lineIndexFlag = 0
        with open(fullName, 'r', encoding='utf-8') as f:
            for line in f:
                lines.append(line)
        index = 0
        updated = False
        for line in lines:
            new_line = ''
            if '<http' in line:
                url_start_index = -1
                url_end_index = -1
                str_index = 0
                for c in line:
                    if c == '<':
                        url_start_index = str_index
                    elif c == '>':
                        url_end_index = str_index
                        url = line[url_start_index + 1:url_end_index]

                        if url_start_index > 0:
                            new_line = line[:url_start_index]

                        new_line = new_line + "[" + url + "](" + url + ")" + line[url_end_index + 1:]
                    str_index = str_index + 1
                updated = True
            else:
                new_line = line

            out_lines.append(new_line)
            index = index + 1

        if updated:
            with open(fullName, 'w') as m:
                content = ''.join(out_lines)
                m.write(content)
                logging.debug('file updated: ' + fullName)
