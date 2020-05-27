**1. What are the differences between horizontal scaling and vertical scaling?**

The difference between horizontal and vertical scaling is that horizontal scaling relies on upgrading the capacity of a single machine while vertical scaling relies on increasing the number of machines without haveing to upgrade CPU or storage.


**2. How does an autoscaler know when to increase/decrease the number of instances?**

An autoscaler should know when to increase the number of instances by detecting the CPU usage and seeing if the usage is too close to or above the maximum the instance can handle. When decreasing the number of instances, the autoscaler should see when the CPU usage is low or zero on an instance.


**3. Why is a load balancer necessary in our system?**

A load balancer is necessary because the people on the high CPU instance need to be moved to the instance that the autoscaler created. this way the CPU is split between the two instances and is at a more suitable state for both instances.


**4. Why does the HOSTNAME value change when we refresh the website?**

The HOSTNAME value changes when we refresh the website because we go into a different ECS container whenever we reload the website.


**5. What metric is our autoscaler tracking? How will it react to increased/decreased traffic?**

The metric our autoscaler is tracking is CPU use percentage. With increased traffic, it will create more containers; with decreased traffic it will delete some containers.


**6. What is locust and why is load testing useful?**

locust is a tool that simulates throusands of users performing tasks such as http requests. Load testing is useful because we can check to see if our website is slow and unresponsive depending on the number of users on it.


**7. What is the basic structure of a locustfile?**

A locustfile will have a MyLocust class which defines each simulated user in the swarm of thousands. A locustfile will aslo have a MyTaskSet class which defines what tasks each simulated user will take when in the swarm. In our case we also imported the HttpUser class to let our locusts make http calls.


**8. Why does the Locust response time first increase after we begin the test and then decrease soon after?**

The response time increases initially because locust is making more http requests for every new hatched user which slows down the system. The reason it decreases is because the autoloader creates new containers and the load balancer splits all of the locusts to the new containers which lets each container decrease its response time.
