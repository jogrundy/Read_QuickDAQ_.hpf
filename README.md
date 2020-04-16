# Read_QuickDAQ_.hpf
reads QuickDAQ hpf files, returns 'filename_info.txt', 'filename_data.csv' files

file contains function 'write_info_and_csv_from_hpf' which takes a filename as input, and has optional output filename argument. This reads through the '.hpf' file and returns an info file as txt, has the name 'filename_info.txt' and the data  in double format as a csv file, called 'filename_data.csv' which has the data as a single column, and the header is the channel number. Unfortunately at present I only have single channel hpf data files, so I've not quite finished the coding for outputting as multichannel data. I will update if I get a multichannel '.hpf' file. 

This was originally written by translating the matlab code from https://www.datatranslation.de/Download/Demos/Hpf2Matlab_Rev2_0.m

However subsequent refactoring and testing have rendered it a somewhat different program. 
