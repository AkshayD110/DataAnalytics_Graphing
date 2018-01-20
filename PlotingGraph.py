import matplotlib.pyplot as plt
import numpy as np
import holoviews as hv
import pandas as pd
hv.extension('bokeh', 'matplotlib')

class PlotingGraph(object):

    def matlibplot(self, fullMemoryDetails):
        plt.xlabel("Time")
        plt.ylabel("Memory(MB)")
        plt.title("Counter graph")
        """you can do an assertion here to check lenght of the dict values"""
        for keys in fullMemoryDetails:
            #print("check this out", keys, ':\t', fullMemoryDetails[keys])
            plt.plot(fullMemoryDetails[keys])
            # plt.plot(x,[pt[i] for pt in fullMemoryDetails[keys]])

        plt.legend(list(fullMemoryDetails.keys()))
        plt.show()

    def panda_plot(self, datafile, fullmemorydetails):
        df = pd.read_csv(datafile)
        ds = hv.Dataset(df)
        tb = hv.Table(ds, kdims=['obis_rss', 'obips_rss'], vdims='obis_vsz')
        hv.HoloMap(tb.to.curve(kdim=['obis_rss'], vdims='obis_vsz'))