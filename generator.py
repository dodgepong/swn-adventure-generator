import argparse
import json
import random
import re
import sys

seed_regex = re.compile(r"\[(Thing|Things|Enemy|Enemies|Place|Places|Friend|Friends|Complication|Complications)\]")

def generate_seeds(seeds, planet, selected_tag=None, numseeds=10):
    if selected_tag:
        print('Selected tag ' + selected_tag)
    else:
        print('No tag specified, combining elements from all tags (' + ', '.join([tagname['name'] for tagname in planet['attributes']['tags']]) + ")")

    print('Generating ' + str(numseeds) + ' seeds:')
    for iteration in range(numseeds):
        seed = seeds[random.randrange(len(seeds))]
        seed_split = seed_regex.split(seed)

        rendered_seed = '> '
        for index in range(len(seed_split)):
            rendered_seed += seed_split[index]
            if index % 2 == 0:
                continue
            else:
                tag = select_tag(planet, selected_tag)
                rendered_seed += ' ('
                if seed_split[index] == "Thing" or seed_split[index] == "Things":
                    rendered_seed += tag['things'][random.randrange(len(tag['things']))]
                elif seed_split[index] == "Friend" or seed_split[index] == "Friends":
                    rendered_seed += tag['friends'][random.randrange(len(tag['friends']))]
                elif seed_split[index] == "Enemy" or seed_split[index] == "Enemies":
                    rendered_seed += tag['enemies'][random.randrange(len(tag['enemies']))]
                elif seed_split[index] == "Place" or seed_split[index] == "Places":
                    rendered_seed += tag['places'][random.randrange(len(tag['places']))]
                elif seed_split[index] == "Complication" or seed_split[index] == "Complications":
                    rendered_seed += tag['complications'][random.randrange(len(tag['complications']))]

                rendered_seed += ')'

        print(rendered_seed)


def select_tag(planet, tagname=None):
    tag = None
    if tagname:
        tag = next((t for t in planet['attributes']['tags'] if t['name'] == tagname), None)

    if not tag:
        tag = planet['attributes']['tags'][random.randrange(len(planet['attributes']['tags']))]

    return tag


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate adventure seeds from a Sectors Without Number sector")
    parser.add_argument('--seedfile', '-s', type=str, default='seeds.json', help="Path to json file containing list of fractal adventure seeds.")
    parser.add_argument('--sectorfile', '-S', type=str, default='sector.json', help="Path to json file containing Sectors Without Number sector json export.")
    parser.add_argument('--planet', '-p', type=str, help="Name of planet to generate seeds for.")
    parser.add_argument('--tag', '-t', type=str, help="Tag to generate seeds for. If no tag or an invalid tag is selected, seeds will be generated from a combination of all tags.")
    parser.add_argument('--numseeds', '-n', type=int, default=10, help="Number of seeds to generate.")
    args = parser.parse_args()

    seeds = None
    with open(args.seedfile) as f:
        seeds = json.load(f)

    if not seeds:
        sys.exit()

    sector = None
    with open(args.sectorfile) as f:
        sector = json.load(f)

    if not sector:
        sys.exit()

    print('Imported sector ' + list(sector['sector'].values())[0]['name'])

    planet_name = args.planet
    planet = next((p for p in list(sector['planet'].values()) if p['name'] == planet_name), None)

    if not planet:
        planet = list(sector['planet'].values())[random.randrange(len(sector['planet']))]
        print('No planet specified, choosing ' + planet['name'])
    else:
        print('Selecting planet ' + planet['name'])

    generate_seeds(seeds, planet, selected_tag=args.tag, numseeds=args.numseeds)
