'python demo.py' to run

- demo.py runs flaskserver.py and jsonSDserver.py.
- flaskserver.py runs a Flask Server to communicate between SD on TT device and frontend on user device.
- jsonSDserver.py runs SD on user device using a JSON file as a prompt queue.
- isolatedSDserver.py runs SD on a user device with CLI inputs. It was isolated from the main demo.py for SD on Wormhole.