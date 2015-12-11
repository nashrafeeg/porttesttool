# Port Test Tool

This is a tool i wrote because of hours and hours I have wasted using telnet client to check connectivity between servers on "Enterprise Envivroment". This especially painful when guys opening firewall ports are offshore.  
## Installation

copy the ptt.exe to the box from where you need to run the connectivity test from 

## Usage
ptt.exe [-h] [-o [OUTPUTFILE]] [-H] [portlist]

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

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits
FUCKING TCS with out you guys I would not have been motiviated enough to write this 

## Creators

**Nashath Rafeeq**

* <https://twitter.com/nashrafeeg>
* <https://github.com/nashrafeeg>
* <http://nashath.xyz>


## Copyright and license

Code and documentation copyright 2015 Unrealproductions, Inc. Code released under [the MIT license]. Docs released under [Creative Commons].




















# Port Test Tool
Port Test Tool
usage: 