#!/usr/bin/python
import sys, os
from optparse import *
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from infinite_medium_simulation_plot import plotExtractedInfiniteMediumSimulationData

if __name__ == "__main__":

    # Parse the command line arguments
    parser = OptionParser()
    parser.add_option("--wh_data_file", type="string", dest="wh_data_file",
                      help="the wh data file to load")
    parser.add_option("--ia_data_file", type="string", dest="ia_data_file",
                      help="the ia data file to load")
    options,args = parser.parse_args()

    if "s3" in options.wh_data_file:
        top_ylims = [0.0, 0.03]
        bottom_ylims = [0.90, 1.10]
        legend_pos = (0.99,1.05)
    elif "s6" in options.wh_data_file:
        top_ylims = [0.0, 0.03]
        bottom_ylims = [0.90, 1.10]
        legend_pos = (0.95,0.95)
    elif "s9" in options.wh_data_file:
        top_ylims = [0.0, 0.03]
        bottom_ylims = [0.95, 1.05]
        legend_pos = (0.95,0.95)
    elif "s12" in options.wh_data_file:
        top_ylims = [0.0, 0.03]
        bottom_ylims = [0.90, 1.10]
        legend_pos = (0.95,0.95)
    elif "s15" in options.wh_data_file:
        top_ylims = [0.0, 0.15]
        bottom_ylims = [0.90, 1.10]
        legend_pos = (0.95,0.95)
    elif "s1" in options.wh_data_file:
        top_ylims = [0.0, 0.07]
        bottom_ylims = [0.90, 1.10]
        legend_pos = (0.95,0.95)

    xlims = [0.0, 10.0]
            
    # Plot the spectrum
    plotExtractedInfiniteMediumSimulationData( options.wh_data_file,
                                               "FRENSIE-WH",
                                               "FF-WH",
                                               options.ia_data_file,
                                               "FRENSIE-IA",
                                               "FA-IA",
                                               top_ylims,
                                               bottom_ylims,
                                               xlims,
                                               legend_pos = legend_pos )

    