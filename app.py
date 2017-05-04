from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

#This Function prints all tcp connections grouped by pid,status.
def print_connections():

        """This Function gets tcp connections and prints status, pid by sorting on the basis of connection status.  """
        connection_array = psutil.net_connections('tcp')
        #Defining socket_conn as namedTuple
        socket_conn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr',
                             'status', 'pid'])
        #Sorting connections on the basis of PID
        sorted_connections = sorted(connection_array, key=attrgetter('pid'))
        grouped_map = {}
        pid_count_map={}
        #grouping connections on pid and counting number of connections per pid
        for key, group in groupby(sorted_connections, key=attrgetter('pid')):
            grouped_map[key] = [e for e in group]
            pid_count_map[key]=len(grouped_map[key])



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
