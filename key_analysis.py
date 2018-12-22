from music21 import midi, converter, environment, tempo
from music21 import note as note21, stream as stream21, analysis, graph
from mido import MidiFile
import mido
import pandas as pd

import numpy as np
import pandas as pd
import matplotlib
import sys


stream = converter.parse('/Users/elliottevers/Downloads/ella_dream_chords.mid')

p = graph.plot.WindowedKey(stream.parts[0])

p.processorClass = analysis.discrete.BellmanBudge

p.doneAction = 'show'
# p.run()

bbAnalyzer = analysis.discrete.BellmanBudge()

wa = analysis.windowed.WindowedAnalysis(stream.parts[0], bbAnalyzer)


solutions, colors, meta = wa.process(
    minWindow=4,
    maxWindow=8,
    windowStepSize=4,
    windowType='adjacentAverage',
    includeTotalWindow=False
)

print(p.processor.solutionsFound)

