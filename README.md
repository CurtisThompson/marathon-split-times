# Marathon Split Times

A simple docker/flask server for predicting finishing times in a marathon race based on 5km split times.

The completed service takes in a list of 5km split times from a single athlete, and outputs their predicted finishing time. Any number of legitimate splits (between 1 and 8) can be entered to get an output. To run the service, see [Usage](#usage). To understand marathon finishing times and splits, see [Marathon Notes](#marathon-notes).

## Usage

1) Run ```docker build -t app-marathon-split .``` to build a Docker image using ```Dockerfile```.

2) Run ```docker run -p 80:80 app-marathon-split``` to run the Docker container produced in step one.

3) Use the following command to get a marathon finishing time prediction.  
```
curl -X POST localhost:80/predict -H "Content-Type: application/json" -d "['14:10', '14:10', '14:14']"
```
This command assumes that the docker container is running on localhost port 80. The data passed to the service is the split times for the prediction. In this example, our runner ran the first 5km in 14 minutes and 10 seconds (14:10). They ran the next 5km (5km-10km) in 14:10 as well. They ran the next 5km (10km-15km) in 14:14.

## Marathon Notes

A [marathon](https://en.wikipedia.org/wiki/Marathon) is a 42.195km road race. Famous marathon races include the London Marathon and Boston Marathon, which are run by elite athletes and regular people. A male elite athlete might be expected to run a marathon between 2 hours (written as 2:00:00) and 2 hours and 15 minutes (written as 2:15:00). More casual runners can have times ranging between 3 and 6 hours.

In organised races, runners can get their times broken into 5km chunks - known as splits. The first split will be the first 5km. The second split will be their time between 5km and 10kn. The third split will be their time between 10km and 15km. This continues all the way up to the end of the race. When watching an elite marathon you can usually see their splits in real-time, and this is a good indication of how fast they will complete the whole race.

When Kenyan marathon runner [Eliud Kipchoge ran the first marathon in under 2 hours](https://www.bbc.co.uk/sport/athletics/50025543) (although not in an official race), his split times were:
Split | Distance | Time | Cumulative Time
--- | --- | --- | ---
1 | 0km-5km | 14:10 | 14:10
2 | 5km-10km | 14:10 | 28:20
3 | 10km-15km | 14:14 | 42:34
4 | 15km-20km | 14:13 | 56:47
5 | 20km-25km | 14:12 | 1:10:59
6 | 25km-30km | 14:12 | 1:25:11
7 | 30km-35km | 14:12 | 1:39:23
8 | 35km-40km | 14:13 | 1:53:36
9 | 40km-Finish | 6:04 | 1:59:40

