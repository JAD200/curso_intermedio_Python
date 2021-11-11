from data_filtered import DATA

def run():
#   HIGH ORDER FUNCTIONS
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
#   FILTER & MAP
    # This filters the age of the worker
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    # This shows the name of THE WORKER FILTERED
    adults = list(map(lambda worker: worker['name'], adults))

#   HIGH ORDER FUNCTION
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    # for worker in all_python_devs:
    #     print(worker)

#   Challenges of the class
    #   FILTER & MAP
    print('\n* * * PYTHON DEVS * * *')
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python',DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    for worker in all_python_devs:
        print(worker)

    print('\n* * * Platzi WORKERS * * *')
    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))
    for worker in all_platzi_workers:
        print(worker)

    print('\n* * * ADULTS * * *')
    adults1 = [worker['name'] for worker in DATA if worker['age'] > 18]
    for worker in adults1:
        print(worker)

    print('\n* * * OLD PEOPLE * * *')
    #Python 3.8 sintaxis: z = {**x, **y}
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    #Python 3.9 sintaxis: z = x | y
    # old_people = [worker | {'old': worker['age'] > 70} for worker in DATA]
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()