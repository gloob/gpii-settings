cd 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\'
#gci . -r | % { $_; (gp $_.pspath).psbase.properties } | ft name,value -a
gci . -r | epcsv -Path C:\vagrant\ATs.csv
