#### **INSTALLATION**

**1.** Download the latest version of wikipedia dump from this server _https://dumps.wikimedia.org/other/cirrussearch/current/_
  the version should be `{lang}wiki-content` which is the one with the encyclopedic voices. the general version is the one with user discussions

**2.** create a sample with only the title, the outgoing_links and the categories of the whole wikipedia using the script in `./wikigraph/utils/minimizeElasticDump.py` .
 The output json is our database which will be included in elasticsearch

**3.** create csv for massive import on neo4j with the script `./wikigraph/utils/dumpXGraph.py` The two output csv 
 will constitute our database for neo4j

**4.** install GNU-parallel, utility for parallel task execution: _https://www.gnu.org/software/parallel/_

**5.** build the docker image of python microservices launching from the path where Dockerfile is
  `docker build -t graph_disambiguator:1.0 .`

**6.** run the containers with docker compose
   `docker-compose up`

**7.** from kibana `http://localhost:5601` click on the dev_tools tab and declare the wikigraph index mapping used by our services
   to do that write `PUT wikigraph` and paste in the next line the json inside
    the file `./wikigraph/resources/mapping.json` and make the PUT call to the elastic server

**8.** enter the data in the created index with the command:
  `cat <path_to_the_json_created_in_section_two> | parallel --pipe -L 2 -N 2000 -j3 'curl -s -H "Content-Type: application/x-ndjson" http://localhost:9200/wikigraph/_doc/_bulk --data-binary @- > /dev/null'
`
**9.** enter in the neo4j browser on `http://127.0.0.1:7474` and create a constraint
 `CREATE CONSTRAINT ON (r:Record) ASSERT r.title IS UNIQUE`

**10.** copy outside the docker container th file `docker-entrypoint.sh` from the container root `docker cp <containerId>:/docker-entrypoint.sh /host/path/target`

**11.** stop the active neo4j container: `docker-compose down neo4j`

**12.** copy this command inside the docker-entrypoint.sh `bin/neo4j-admin import --nodes:Record /import/pages-headers.csv,/import/pages.csv --relationships=/import/outgoing-headers.csv,/import/outgoing.csv --ignore-missing-nodes
`
**13.** copy the csv files created in section three inside the folder to be mounted in in `/import` folder indicated in neo4j service in the docker-compose file
        In the same folder copy also `./wikigraph/resources/pages-headers.csv` and `./wikigraph/resources/pages-headers.csv`
        
**14.** In the docker-compose allow to mount `docker-entrypoint.sh` inside the neo4j service. Then you can run the neo4j container: `docker-compose up neo4j`

**15.** At the next start of the neo4j container remember to comment out or remove from volumes `docker-entrypoint.sh` 

#### **USAGE OF THE SERVICE**

To inquiry the disambiguation service

`import requests`

`splitted_phrase = "a python is eating a mouse".split()`

`r = requests.post("http://localhost:8000/disambiguate", json={"phrases": splitted_phrase})`

An example to make a call could be found here `./wikigraph/utils/GraphManager.py`