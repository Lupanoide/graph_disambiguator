#!/usr/bin/python3
# encoding=utf8

import gzip
import json
import csv
import argparse


class createRelationship:
    def __init__(self):

        self.writtenPossibleDuplicate = set()
        parser = argparse.ArgumentParser(description='Set input and output files for neo4j import process')
        parser.add_argument('input', type=str, help='Input path for elastic json.gz wikipedia dump')
        parser.add_argument('pagesoutput', type=str, help='Output path for the csv with neo4j db nodes - the titles of wikipedia pages')
        parser.add_argument('outlinksoutput', type=str, help='Output path for the csv with neo4j db edges - a realtionship between a wikipedia page and its outgoing links')
        parser.add_argument('lang', type=str, help='Language of wikipedia dump')
        self.args = parser.parse_args()

        with open(r"../resources/{}_duplicated_words.txt".format(self.args.lang), "r") as f:
            self.duplicate_set = frozenset([a.strip() for a in f.readlines()])

    def writeRedirect(self, redirect):
        for red in redirect:
            self.writePages(red['title'])

    def checkDuplicateWords(self, word):
        value = False
        if word in self.duplicate_set:
            value = True
        return value


    def writePages(self, title):
        if self.checkDuplicateWords(title):
            if title in self.writtenPossibleDuplicate:
                return title
            self.writtenPossibleDuplicate.add(title)
        with open(self.args.pagesoutput, "a") as csvfile:
            fieldnames = ['title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"title": title})
            return title


    def writeOutgoing(self, title, outgoing):
        with open(self.args.outlinksoutput, "a") as csvfile:
            fieldnames = ['title',"outgoing", "rel"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for out in outgoing:
                if not out:
                    continue
                if ":" in out:
                    continue
                writer.writerow({"title": title ,"outgoing": out.replace("_"," "),"rel":"HAS_LINK"})


    def run(self):
        with gzip.open(self.args.input, "rb") as f:
            for line in f:
                lineaDump = json.loads(line.encode("utf-8"))
                if "title" in lineaDump:
                    titolo = self.writePages(lineaDump['title'])
                if "redirect" in lineaDump:
                    self.writeRedirect(lineaDump['redirect'])
                    self.writeOutgoing(titolo, lineaDump['redirect'])
                if "outgoing_link" in lineaDump:
                    self.writeOutgoing(titolo , lineaDump['outgoing_link'])




if __name__ == '__main__':
    oo = createRelationship()
    oo.run()
    del oo
