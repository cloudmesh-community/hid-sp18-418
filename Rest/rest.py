from eve import Eve
import platform
import psutil


app=Eve()
@app.route('/system_properties')
def system_properties():
    det=[]
    det.append("Processor:\t"+platform.processor())
    det.append("uname:\t"+str(platform.uname()))
    det.append("Platform:\t"+platform.system())
    det.append("Name:\t"+platform.machine())
    det.append("Cpu Percentage :\t"+str(psutil.cpu_percent()))
    det.append("Physical Memory Use :\t"+str(psutil.virtual_memory()))
    det.append("Physical Memory Use :\t"+str(platform.uname()))
    return "<br />".join(det)

if __name__=='__main__':
    app.run()