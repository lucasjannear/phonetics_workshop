Title: Tools, Strategies, and Resources in Corpus Phonetics 
Authors: Luke Annear and Emily Bagan 
Presented at: Workshop in General Linguistics 2025

This repository contains files and subdirectories for generating all data presented in the workshop.

If you are starting from the .wav files and generating .txt files via whisper, you can start with the files in `phonetics_workshop/long_files/` to create `.txt` files from scratch for forced alignment.

If you want to force align the files to create Praat textgrids by skipping transcription with Whisper, you can copy the `.txt` files for each .wav file out of `phonetics_workshop/whisper_transcriptions/` and into `phonetics_workshop/long_files/` for each speaker subdirectory. From there you can use documentation at https://montreal-forced-aligner.readthedocs.io/en/latest/index.html to force align the audio files and then use the `.Rmd` document for data processing in R.

If you are wanting to follow along with the data processing in R and not yet do the forced alignment, the same textgrid data is provided as a `.csv` in `phonetics_workshop/workshop_data.csv`.
