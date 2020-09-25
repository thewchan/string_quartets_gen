# String Quartet Arrangement Generator
The is a prototype app that takes in a user uploaded midi file containing a melody, generates a string quartet arrangement of it, and outputs a PDF sheet music of that arrangement.

The model is powered by the [Magenta-Coconet counterpoint by convolution](https://github.com/magenta/magenta/tree/master/magenta/models/coconet) model developed by [Google Brain](https://research.google/teams/brain/). The midi melody file is parsed by [Music21](http://web.mit.edu/music21/) developed by the Cuthbert Lab at MIT. Conversion to PDF is via [Lilypond](https://lilypond.org/), the GNU music engraving package.

This app is currently under active development. License information in located in COPYING.
