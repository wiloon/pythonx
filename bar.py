import os
import logging

logging.basicConfig(level=logging.DEBUG)
subTitleSet = set([])
for root, dirs, files in os.walk("/home/wiloon/workspace/my-projects/wiloon.com/content/post"):
    logging.debug("file list size: " + str(len(files)))
    for name in files:
        fullName = os.path.join(root, name)
        logging.debug("path: " + fullName)
        lines = []
        lineIndex = 0
        title = ''
        lineIndexFlag = 0
        with open(fullName, 'r', encoding='utf-8') as f:
            for line in f:
                lines.append(line)
        index = 0
        for line in lines:
            if line.startswith('---') and lineIndexFlag < 2:
                lineIndex = index
                lineIndexFlag = lineIndexFlag + 1
            if line.startswith('title:'):
                titleList = line.split('title:')
                title = titleList[1].strip()
                logging.debug('title: ' + title)

            if line.startswith('#'):
                strList = line.split('#')
                for item in strList:
                    if item != '#':
                        subTitleSet.add(item.strip())
            index = index + 1

        if title not in subTitleSet:
            lines.insert(lineIndex + 1, '# {}\n'.format(title))
            with open(fullName, 'w') as m:
                content = ''.join(lines)
                m.write(content)
                logging.debug('insert title')

        # input("next...")
        # os._exit(0)
