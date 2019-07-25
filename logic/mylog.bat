@echo off
 
echo %date%
echo %time%
 
set yyyy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
 
set time2=%time: =0%
 
set hh=%time2:~0,2%
set mn=%time2:~3,2%
set ss=%time2:~6,2%
 
set filename=%yyyy%-%mm%%dd%-%hh%%mn%%ss%
 
echo test >> mylog_%filename%.txt
 
