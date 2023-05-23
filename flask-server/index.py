#########################
# Imports:
from analysis.ploting.ranking_normals import two_dimensional_grid, violinPlot, accuracyBarPlot,accVsCon

list_number = 2
kind = 'deletion'
#########################
# Running:
# two_dimensional_grid('scatter',1,'data/json/segmented_norms/L1_normal/')
# two_dimensional_grid('violin',1,'data/json/segmented_norms/L1_normal/')
# two_dimensional_grid('violin',1,'data/json/segmented_norms/L1_deletion/')

# accuracyBarPlot(list_number, 'data/json/segmented_norms/L{}_{}/'.format(list_number,kind))
# violinPlot(list_number, 'data/json/segmented_norms/L{}_{}/'.format(list_number,kind))
accVsCon(list_number, 'data/json/segmented_norms/L{}_{}/'.format(list_number,kind))
#########################