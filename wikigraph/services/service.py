#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
from flask import Flask, request,jsonify
from wikigraph.config.Config import Config
from wikigraph.utils.validateArgz import validateArgz
from wikigraph.business.GraphAnalisysBusiness import GraphBusiness
from wikigraph.business.WikiBusiness import WikiBusiness

app = Flask(__name__)

log_level = Config().getLogLevel()
log = logging.getLogger(__name__)
log.setLevel(getattr(logging, log_level))


@app.route("/disambiguate", methods=['POST'])
def upload_bulk_outgoing_links():
    log.info("ip: {add} method: {meth}".format(add=request.remote_addr, meth=request.method))
    argz_data = request.get_json()
    validation = validateArgz()
    success = validation.run(argz_data)
    if not success.case:
        return success.message, 400

    bus = WikiBusiness()
    graph = GraphBusiness()
    aux = bus.bulkGetPages(argz_data["phrases"])
    result = graph.getMostRelatedSubGraph(aux)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')