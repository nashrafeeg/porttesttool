# porttesttool
Port Test Tool
usage: Port Test Tool [-h] [-o [OUTPUTFILE]] [-H] [portlist]

                        Port Test Tool (Cause Fuck TCS)
                        -------------------------------
                                version: 1.11 (cause fuck TCS)
                                Author: Nash Rafeeq (@nashrafeeg)
                                RTFM: http://nashath.xyz/ptt/v1.11'

                        Input file
                        ----------
                                format: CSV
                                delimeter: ,
                                header: fqdn/ip,port,[protocol]
                                Eg: 8.8.8.8,53,TCP

                        Outputfile
                        ----------
                                format:CSV
                                delimeter: ,
                                header: fqdn/ip,port,protcol,status,[failed Reason]
                                Eg: 8.8.8.8,53,TCP


positional arguments:
  portlist              path to csv file containing list of ports to test

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUTFILE], --outputfile [OUTPUTFILE]
                        path to output results to
  -H, --header          set if the CSV file contains header row (igonore first
                        row)

                Please send any bugs or feature request to ptthelp@nashath.xyz
                Pull requests are welcome at https://github.com/nashrafeeg/porttesttool