# task_muppet
Because I can.

## What is this?
Right now, vaporware. 
Soon, it will be a task management API. You'll be able to create tasks, edit tasks, complete tasks... yep, those things.
The vision is:
 + Tasks can be related to other tasks as parents and children
 + Aggregation of count and sum data for all child tasks in the tree
 + Can't complete tasks until all the child tasks are complete
 + Some sort of web interface that uses the API that gets built initially

## How do I run it?
```
docker run -d -p [port]:5000 apth/task-muppet:latest
```

## How can I use it?
Right now, you can't. It's buggy and I haven't fixed it yet.

In theory:

### Create task
```
http://localhost/?description='Task Description'
```

### Modify task
```
Coming soon!
```

### Delete task
```
Coming soon!
```

## How does it work?
Right now it's this horrific text file JSON mess. 
Soon it'll be nice.
I promise.

## Are there tests?
No, but there will be. Nice tests. Will lots of coverage.

## How can I monitor the service?
For now, check the container is up and the port is accessible I guess.
Later on I'll define how to test the actual API endpoints without changing the data. 