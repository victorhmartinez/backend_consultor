
from unittest import result
import re
from flask import Flask
import json 
from flask_cors import CORS
from SPARQLWrapper import SPARQLWrapper, JSON
app=Flask(__name__)
dbpedia_sparq = "http://dbpedia.org/sparql"
dbpedia_idioma = "es"
if __name__=='__main__':
    @app.route("/")
    def hello_world():
        return "<p>Hello, World 2!</p>"
    ##Implementacion de cors
    cors = CORS(app)
    # Ruta de prueba inicial
    @app.route("/api/consultas",methods=['GET','POST'])
    def realizarConsulta():
        languaje="es"
        limit="20"
        sparql = SPARQLWrapper(dbpedia_sparq)
        sparql.setQuery("SELECT *"
                        +"WHERE{"+
                        "?resource rdf:type dbo:Ship."+
                        "?resource rdfs:label ?label."+
                        "?resource dbo:thumbnail ?image."+
                        "?resource rdfs:comment ?comment."+
                        "?resource dbo:abstract ?abstract."+
                        "?resource dbp:shipTonnage ?shipTonnage."+
                        "?resource dbp:shipOwner ?shipOwer."+
                        "?resource dbp:shipLaunched ?shipLaunched."+
                        "?resource dbp:shipCompleted ?shipComplete."+
                        "?resource dbp:shipClass ?shipClass."+
                        "FILTER(LANG(?abstract)='"+languaje+"')"+
                        "FILTER(LANG(?label)='"+languaje+"')"+
                        "FILTER(LANG(?comment)='"+languaje+"')"
                      
                        "}"+
                        "LIMIT "+limit  )
        sparql.setReturnFormat(JSON)
        qres = sparql.query().convert()
        lst = list(qres.values())
        print(languaje)
        results=qres["results"]
        res=qres["results"]["bindings"]
        jsonStrg=json.dumps(res);
 
        return jsonStrg
   # Ruta para consultar barcos en general
    @app.route("/api/consultas/languaje/<lan>/recurso/<recurso>/limite/<limit>",methods=['GET','POST'])
    def realizarConsultaParamen(lan,recurso,limit):
       
        sparql = SPARQLWrapper(dbpedia_sparq)
        sparql.setQuery("SELECT *"
                        +"WHERE{"+
                        "?resource rdf:type dbo:"+recurso+"."+
                        "?resource rdfs:label ?label."+
                        "?resource dbo:thumbnail ?image."+
                        "?resource rdfs:comment ?comment."+
                        "?resource dbo:abstract ?abstract."+
                        "?resource dbp:shipTonnage ?shipTonnage."+
                        "?resource dbp:shipOwner ?shipOwer."+
                        "?resource dbp:shipLaunched ?shipLaunched."+
                        "?resource dbp:shipCompleted ?shipComplete."+
                        "?resource dbo:length ?shiplength."+
                        "OPTIONAL{?resource dbp:shipClass ?shipClass.}"+
                        "OPTIONAL{?resource dbo:length ?shiplength.}"+
                        "FILTER(LANG(?abstract)='"+lan+"')"+
                        "FILTER(LANG(?label)='"+lan+"')"+
                        "FILTER(LANG(?comment)='"+lan+"')"
                      
                        "}"+
                        "LIMIT "+limit  )
        sparql.setReturnFormat(JSON)
        qres = sparql.query().convert()
        lst = list(qres.values())
       
        results=qres["results"]
        res=qres["results"]["bindings"]
        jsonStrg=json.dumps(res);
 
        return jsonStrg
   # Ruta para consultar un barco en especifico
    @app.route("/api/consultas/languaje/<lan>/nameR/<name>/recurso/<recurso>/limite/<limit>",methods=['GET','POST'])
    def realizarConsultaFiltor(lan,recurso,name,limit):
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(name)
        while m:
            name = m.group(1) + m.group(2)
            m = regEx.match(name)
         
        sparql = SPARQLWrapper(dbpedia_sparq)
        sparql.setQuery("SELECT *"
                        +"WHERE{"+
                        "?resource rdf:type dbo:"+recurso+"."+
                        "?resource rdfs:label ?label."+
                        "?resource dbo:thumbnail ?image."+
                        "?resource rdfs:comment ?comment."+
                        "?resource dbo:abstract ?abstract."+
                        "?resource dbp:shipTonnage ?shipTonnage."+
                        "?resource dbp:shipOwner ?shipOwer."+
                        "?resource dbp:shipLaunched ?shipLaunched."+
                        "?resource dbp:shipCompleted ?shipComplete."+
                        "OPTIONAL{?resource dbp:shipClass ?shipClass.}"+
                        "OPTIONAL{?resource dbo:length ?shiplength.}"+
                        "FILTER(REGEX(str(?label),'"+name+"','i'))"
                        "FILTER(LANG(?abstract)='"+lan+"')"+
                        "FILTER(LANG(?label)='"+lan+"')"+
                        "FILTER(LANG(?comment)='"+lan+"')"
                      
                        "}"+
                        "LIMIT "+limit  )
        sparql.setReturnFormat(JSON)
        qres = sparql.query().convert()
        lst = list(qres.values())
        
        results=qres["results"]
        res=qres["results"]["bindings"]
        jsonStrg=json.dumps(res);
 
        return jsonStrg 
  # Ruta para consultar libros en general
    @app.route("/api/consultasBooks/languaje/<lan>/recurso/<recurso>/limite/<limit>",methods=['GET','POST'])
    def realizarConsultaBooksParamen(lan,recurso,limit):
        sparql = SPARQLWrapper(dbpedia_sparq)
        sparql.setQuery("SELECT *"
                        +"WHERE{"+
                        "?resource rdf:type dbo:"+recurso+"."+
                        "?resource rdfs:label ?label."+
                        "?resource dbo:thumbnail ?image."+
                        "?resource rdfs:comment ?comment."+
                        "?resource dbo:abstract ?abstract."+
                        "?resource dbo:isbn ?isbn."+
                        "?resource dbo:numberOfPages ?numberPage."+
                        "?resource dbp:publisher ?publisher."+
                        "FILTER(LANG(?abstract)='"+lan+"')"+
                        "FILTER(LANG(?label)='"+lan+"')"+
                        "FILTER(LANG(?comment)='"+lan+"')"
                      
                        "}"+
                        "LIMIT "+limit  )
        sparql.setReturnFormat(JSON)
        qres = sparql.query().convert()
        lst = list(qres.values())
       
        results=qres["results"]
        res=qres["results"]["bindings"]
        jsonStrg=json.dumps(res);
 
        return jsonStrg
    # Ruta para flitar libros en especifico
    @app.route("/api/consultasBooks/languaje/<lan>/nameR/<name>/recurso/<recurso>/limite/<limit>",methods=['GET','POST'])
    def realizarConsultaBookFiltor(lan,recurso,name,limit):
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(name)
        while m:
            name = m.group(1) + m.group(2)
            m = regEx.match(name)
         
        sparql = SPARQLWrapper(dbpedia_sparq)
        sparql.setQuery("SELECT *"
                        +"WHERE{"+
                        "?resource rdf:type dbo:"+recurso+"."+
                        "?resource rdfs:label ?label."+
                        "?resource dbo:thumbnail ?image."+
                        "?resource rdfs:comment ?comment."+
                        "?resource dbo:abstract ?abstract."+
                        "?resource dbo:isbn ?isbn."+
                        "?resource dbo:numberOfPages ?numberPage."+
                        "?resource dbp:publisher ?publisher."+
                        "FILTER(REGEX(str(?label),'"+name+"','i'))"
                        "FILTER(LANG(?abstract)='"+lan+"')"+
                        "FILTER(LANG(?label)='"+lan+"')"+
                        "FILTER(LANG(?comment)='"+lan+"')"
                        "}"+
                        "LIMIT "+limit  )
        sparql.setReturnFormat(JSON)
        qres = sparql.query().convert()
        lst = list(qres.values())
        
        results=qres["results"]
        res=qres["results"]["bindings"]
        jsonStrg=json.dumps(res);
 
        return jsonStrg
    app.run()
    