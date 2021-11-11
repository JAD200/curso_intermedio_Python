from data_filtered import DATA

def run():
    # HIGH ORDER FUNCTIONS
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    # FILTER
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    # MAP
    adults = list(map(lambda worker: worker['name'], adults))
    # HIGH ORDER FUNCTION
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()