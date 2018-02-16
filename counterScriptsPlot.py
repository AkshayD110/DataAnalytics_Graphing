import PlotingGraph
import PrepareDataForPlotting
# path = "C:\Users\akshdesh.ORADEV\Documents\books\python\WorkingProjects\CoutersProject\Counters_ak_2nodeTest3_1000
# .09_32_37_18-Oct"

def main():
    fullMemoryDetails = {}
    readCouterFiles = PrepareDataForPlotting.PrepareDataForPlotting(r"C:\Users\akshdesh.ORADEV\Documents\books\python\WorkingProjects\CoutersProject\Counters_ak_2nodeTest3_1000.09_32_37_18-Oct")
    memoryResults = readCouterFiles.readTheProcessIDs(
        r"C:\Users\akshdesh.ORADEV\Documents\books\python\WorkingProjects\CoutersProject\Counters_ak_2nodeTest3_1000.09_32_37_18-Oct")
    machineMemory = readCouterFiles.machineMemory(
        r"C:\Users\akshdesh.ORADEV\Documents\books\python\WorkingProjects\CoutersProject\Counters_ak_2nodeTest3_1000"
        r".09_32_37_18-Oct")

    #print(obips_rss, '\n', obips_vsz, '\n', obis_rss, '\n', obis_vsz, '\n', obijh_rss, '\n', obijh_vsz, '\n',
     #     biresults_rss,
      #    '\n', biresults_vsz, '\n', machineMemory)

    fullMemoryDetails['obips_rss'] = memoryResults[0]
    fullMemoryDetails['obips_vsz'] = memoryResults[1]
    fullMemoryDetails['obis_rss'] = memoryResults[2]
    fullMemoryDetails['obis_vsz'] = memoryResults[3]
    fullMemoryDetails['obijh_rss'] = memoryResults[4]
    fullMemoryDetails['obijh_vsz'] = memoryResults[5]
    fullMemoryDetails['biresults_rss'] = memoryResults[6]
    fullMemoryDetails['biresults_vsz'] = memoryResults[7]
    fullMemoryDetails['machineMemory'] = machineMemory

    readCouterFiles.writeDataTocsvFile(fullMemoryDetails)

    plotingdifferentGraph = PlotingGraph.PlotingGraph()
    plotingdifferentGraph.matlibplot(fullMemoryDetails)
    #plotingdifferentGraph.panda_plot(r"C:\Users\akshdesh.ORADEV\PycharmProjects\dataAnalytics\dataFile.csv",
    # fullMemoryDetails)




if __name__ == '__main__':
    main()