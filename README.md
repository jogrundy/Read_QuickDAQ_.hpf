# Read_QuickDAQ_.hpf
reads QuickDAQ hpf files, returns 'filename_info.txt', 'filename_data.csv' files

File contains function 'write_info_and_csv_from_hpf' which takes a filename as input, and has optional output filename argument. This reads through the '.hpf' file and returns an info file as txt, has the name 'filename_info.txt' and the data  in double format as a csv file, called 'filename_data.csv' which has the data as a for each channel as a column, and the header is the channel number. This is now tested and working on .hpf files with two channel data, and should work with more channels.

This was originally written by translating the matlab code from https://www.datatranslation.de/Download/Demos/Hpf2Matlab_Rev2_0.m


