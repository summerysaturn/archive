# Archive

## Table of contents

[Midi-to-VirtualPiano](#Midi-to-VirtualPiano)
[BMP-Corruptor](#BMP-Corruptor)

### Midi-to-VirtualPiano

[Link to Original Readme](Midi-to-VirtualPiano/README.me)

This project is a python script that attempts to convert a Midi file into a playable (depending on the source) VirtualPiano sheet. This is done by interpreting the Midi file byte by byte, using a reference for the format to work properly.

This is considered a failed project as the output doesn't end up sounding right. It does end up working somewhat well, however the notes are off. This might be worth tinkering with, throwing in a midi library, working out a (more correct) lookup table, etc.

### BMP-Corruptor

[Link to Original Readme](BMP-Corruptor/README.md)

Simple-ish python script designed to corrupt bitmap images due to their relatively easily accessible pixel data. This works by moving bytes around, which messes with the colours (24bpp) and positioning of elements. This implementation SUCKS, with lots of randomness. Maybe worth reimplementing as the effect is interesting? Up to you. This is definitely more functional than Midi-to-VirtualPiano.
