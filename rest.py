from eve import Eve
import platform
import psutil
import json

security={'MONGO HOST' : 'localhost', 'MONGO_PORT' : 27017, 'DOMAIN': {}}
app=Eve()

@app.route('/systemprop')
def systemprop(settings=security):
    dict={}
    dict['Processor']=platform.processor()
    dict['Platform']=platform.system()
    dict['Name']=platform.machine()
    dict['Cpu Percentage']=psutil.cpu_percent()
    dict['Physical Memory Use']=psutil.virtual_memory()
    return json.dumps(dict)

if __name__=='__main__':
    app.run()