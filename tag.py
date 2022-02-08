import os
import logging

logging.basicConfig(level=logging.DEBUG)
subTitleSet = set([])
articleIndex = 0
for root, dirs, files in os.walk("/home/wiloon/workspace/my-projects/wiloon.com/content/post"):
    logging.debug("file list size: " + str(len(files)))
    for name in files:
        fullName = os.path.join(root, name)
        logging.debug("index: " + str(articleIndex))
        articleIndex = articleIndex + 1

        logging.debug("path: " + fullName)
        lines = []
        articleStartIndex = 0
        title = ''
        lineIndexFlag = 0
        categoriesExist = 0
        tagExist = 0
        changed = 0
        with open(fullName, 'r', encoding='utf-8') as f:
            for line in f:
                lines.append(line)
        index = 0
        for line in lines:
            if line.startswith('---') and lineIndexFlag < 2:
                articleStartIndex = index
                lineIndexFlag = lineIndexFlag + 1
            # title
            if line.startswith('title:'):
                titleList = line.split('title:')
                title = titleList[1].strip()
                logging.debug('title: ' + title)

            # subtitle
            if line.startswith('#'):
                strList = line.split('#')
                for item in strList:
                    if item != '#':
                        subTitleSet.add(item.strip())

            # categories
            if line.startswith('categories:'):
                categoriesExist = 1

            # tag
            if line.startswith('tags:'):
                tagExist = 1

            index = index + 1

        if title not in subTitleSet:
            lines.insert(articleStartIndex + 1, '## {}\n'.format(title))
            changed = 1
            logging.debug('insert subtitle')

        if categoriesExist == 0:
            lines.insert(articleStartIndex, 'categories:\n')
            articleStartIndex = articleStartIndex + 1
            lines.insert(articleStartIndex, '  - inbox\n')
            articleStartIndex = articleStartIndex + 1
            changed = 1
            logging.debug('insert categories')

        if tagExist == 0:
            lines.insert(articleStartIndex, 'tags:\n')
            articleStartIndex = articleStartIndex + 1
            lines.insert(articleStartIndex, '  - reprint\n')
            articleStartIndex = articleStartIndex + 1
            changed = 1
            logging.debug('insert tags')

        if changed == 1:
            with open(fullName, 'w') as m:
                content = ''.join(lines)
                m.write(content)
                logging.debug('save')
