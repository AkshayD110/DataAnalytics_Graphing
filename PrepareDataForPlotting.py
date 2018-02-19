import os

class PrepareDataForPlotting:
    """below method will fetch all the process id's"""

    def __init__(self, path):
        self.path = path

    'details on __repr__ and __str__ implementation in DanBrader tutorial'
    def __repr__(self):
        return f'{self.__class__.__name__} Class - Preparing data from {self._path}'

    'if there are mutiple instance variables, then it is ok to set them all separately. Link below.'
    'https://stackoverflow.com/questions/21918561/python-multiple-property-statements-in-class-definition'
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def readTheProcessIDs(self):  # if you miss out on the "self" part you will get this error
        # :https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
        allProcessesList = ['OBIPS', 'OBIS', 'OBIJH', 'bi_server1']
        allProcessesDict = {}
        processMemRestults = []
        newPath = os.path.join(self._path, 'processIDs')
        file = open(newPath)
        allLines = file.readlines()
        for lines in allLines:
            allWords = lines.split()
            allProcessesDict[allWords[0]] = allWords[1]
            # print(allProcessesDict)
        for processes in allProcessesList:
            list1, list2 = self.memoryDetails(allProcessesDict[processes], processes)
            processMemRestults.append(list1)  # because it is easy to take the results of all the processes in a single
            #  list
            processMemRestults.append(list2)
        return processMemRestults

    def memoryDetails(self, processID, whichProcess):
        memFilePath = os.path.join(self._path, 'mem_usage_' + processID + '.log')
        file = open(memFilePath)
        allLines = file.readlines()
        process_rss = []
        process_vsz = []
        for i in range(1, len(allLines)):
            allWords = allLines[i].split()
            process_vsz.append(int(allWords[7]) / 1024)
            process_rss.append(int(allWords[8]) / 1024)
        return process_rss, process_vsz


    def machineMemory(self):
        machineCPUValue = []
        machineCPUValuesinMB = []
        machineCPUPath = os.path.join(self._path, 'free_memory_stats.log')
        file = open(machineCPUPath)
        allLines = file.readlines()
        for lines in allLines:
            allValues = lines.split()
            machineCPUValue.append(allValues[1])
        del machineCPUValue[0]
        machineCPUValue = list(map(int, machineCPUValue))
        for values in machineCPUValue:
            machineCPUValuesinMB.append(values / 1024)
        return machineCPUValuesinMB
        """machineCPUValuesinMB hold the data required"""

    def writeDataTocsvFile(self, contentForCSV):
        import csv
        from itertools import zip_longest
        #implemented using https://docs.python.org/3/library/functions.html#zip
        #https://www.reddit.com/r/learnpython/comments/7qb1t0/help_writing_a_dictionary_of_lists_to_csv_file/?st=jcf3a6mr&sh=4fc6b7a0

        transpose_data = list(zip_longest(*contentForCSV.values()))
        with open('dataFile.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(contentForCSV.keys())
            for items in transpose_data:
                writer.writerow(items)
