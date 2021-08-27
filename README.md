# swn-adventure-generator
Adventure generator for Stars Without Number using tags imported from Sectors Without Number

## Usage

```
python generator.py [-h] [--seedfile SEEDFILE] [--sectorfile SECTORFILE] [--planet PLANET] [--tag TAG] [--numseeds NUMSEEDS]

optional arguments:
  -h, --help            show this help message and exit
  --seedfile SEEDFILE, -s SEEDFILE
                        Path to json file containing list of fractal adventure seeds.
  --sectorfile SECTORFILE, -S SECTORFILE
                        Path to json file containing Sectors Without Number sector json export.
  --planet PLANET, -p PLANET
                        Name of planet to generate seeds for.
  --tag TAG, -t TAG     Tag to generate seeds for. If no tag or an invalid tag is selected, seeds will be generated from a combination of all tags.
  --numseeds NUMSEEDS, -n NUMSEEDS
                        Number of seeds to generate.
```
