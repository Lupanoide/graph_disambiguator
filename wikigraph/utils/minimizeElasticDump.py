#!/usr/bin/python3

import json
import gzip
import argparse


class Import:
    def __init__(self):
        self.keys = frozenset(["title", "incoming_links", "outgoing_link", "redirect", "category"])
        parser = argparse.ArgumentParser(description='Set input and output files for Elasticsearch import process.')
        parser.add_argument('input', type=str, help='Input path for elastic json.gz wikipedia dump')
        parser.add_argument('output', type=str, help='Output path for our minimized wikipedia dump')
        self.args = parser.parse_args()

    def cutEdges(self, word):
        value = False
        if ":" in word:
            value = True

        return value

    def run(self):
        with open(self.args.output, "wb") as g:
            with gzip.open(self.args.input, "rb") as f:
                for line in f:
                    lineaDump = json.loads(line.decode("ascii"))
                    if "index" in lineaDump:
                        g.write("{} \n".format( json.dumps( {"index": {"_id": lineaDump["index"]["_id"]}} ) ))
                    elif "title" in lineaDump:
                        recordPage = {key: lineaDump[key] for key in lineaDump if key in self.keys}
                        if "outgoing_link" in recordPage:
                            recordPage["outgoing_link"] = [a.replace("_", " ") for a in recordPage["outgoing_link"] if not self.cutEdges(a)]

                        g.write('{} \n'.format(  json.dumps(recordPage)   ) )


if __name__ == '__main__':
    oo = Import()
    oo.run()
    del oo
