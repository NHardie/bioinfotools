if __name__ == '__main__':
    import json

    with open('masters/BIO723P_Assignment.ipynb', 'r') as f:
        data = json.load(f)
        print(data['cells'])

        counter = 0
        for cell in data['cells']:
            if cell['cell_type'] == 'code':
                if not cell['source'][0].startswith('# Test code'):
                    with open(f'extracted/block_{counter}.py', 'w') as out:
                        out.write("".join(cell['source']) + '\n')
                    counter += 1
