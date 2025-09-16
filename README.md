> [!NOTE]
> I have made changes to the code as of 4:45pm on 9/10. I don't anticipate any further code changes, but I will be updating the readme with more resources and information regularly.

# FEB Autonomous Recruitment Project

The goal of this project is to design and implement something to drive a car around a track while avoiding cones.

More specifically, you must write a function that takes in a single argument (the state of the car) $[x \, y \, \phi \, v \, \theta ]$ and returns a single control command $[a \, \dot{\theta}]$.

These variables represent the following quantities:
- $x$ and $y$ are the position of the car, in meters.
- $\phi$ is the heading of the car, in radians (zero is pointing directly left)
- $v$ is the velocity of the car, in meters per second.
- $\theta$ is the angle of the front wheels, in radians.
- $a$ is the requested acceleration for the car. Think of this more as the normalized force $\frac{F}{m}$ - the car is subject to aerodynamic drag and will not keep accelerating infinitely.
- $\dot{\theta}$ is the time derivative of the steering angle $\theta$. it is a control input. We assume that the steer-by-wire system can acheive high accelerations here, so we don't need to worry about changing this value quickly.

There are also the following constraints:

| variable       | lower bound | upper bound |
| -------------- | ----------- | ----------- |
| $\theta$       | -0.7        | 0.7         |
| $\dot{\theta}$ | -1.0        | 1.0         |
| $a$            | 10          | -4          |

The only other important numbers that you do not get to choose are:
- the wheelbase (distance between front and rear wheels) is 1.58 meters.
- the maximum acceleration the car can handle (in $x$ and $y$ combined) is 12 meters per second per second.
- the outer geometry of the car is a convex polygon with vertices accesible through the `Simulator.car_vertices` property.

## Implementation

Please write your implementation in the `controller` method of `main.py`. You may read or modify anything you want in `simulator.py` for development but make sure your code works with the original simulator class before submission.

Provided in `simulator.py` is the `Simulator` class, which has:
- some basic visualization utilities (`.plot()` and `.animate()`)
- the variable bounds (`.steering_limits`, `.lbu`, and `.ubu`)
- the car outline vertices (`.car_vertices`)
- `.get_results` to see how the simulation went
- `.run()` to run the simulation.
- a bunch of other things.

You can also get the centerline of the track, parameterized by distance (in meters), using the `centerline` function:
```
>>> help(centerline)
Help on vectorize in module numpy:

<lambda> = <numpy.vectorize object>
    get track centerline at distance `x` from the start.
    
    Args:
        x (float or array-like): distance along centerline to get.
    
    Returns:
        array: shape (2,) if `x` is a float or (N, 2) if `x` is an array-like of length N.
>>> 
```

In general, feel free to use any provided functions/properties that don't start with an underscore.

In order to run this simulation, you'll need to install `casadi`, `matplotlib`, and `numpy`.
All can be installed with `pip` (ie, `pip install casadi matplotlib numpy`)

We recommend you fork this repo and develop your code there (so you can keep history with git/github), but you do not need to. You can just clone this repo or download the .zip file and work locally.

### Other Options
If you don't want to run anything locally (if you don't have python, or there's something funny with your default C compiler, or any other reason), this code works in google colab and on the OCF

#### OCF

You can use the vscode remote ssh plugin to use vscode on the OCF's ssh server. Make an account and connect.
You can then clone the repo and work as normal. You may have to `pip install --upgrade matplotlib casadi`.
Viewing the animation likely won't work but you can save it to a file with `sim.animate(save=True)` and view that.

#### Colab

Just make a new notebook and add the following as the first cell:

```
!pip install casadi
!git clone git@github.com:FEBAutonomous/control-recruitment-project.git
```

Then you can copy the contents of `main.py` in: 

```python
import numpy as np
from simulator import Simulator, centerline

sim = Simulator()

def controller(x):
    """
    <docstring excluded for brevity>
    """
    ...

sim.set_controller(controller)
sim.run()
sim.animate()
sim.plot()
```

I'm not sure if `sim.animate()` will work in colab, but if it doesn't, you can just pass `sim.animate(save=True)` and look at the resulting gif.



## Presentation & Submission

When you present your project, you will have roughly 10-15 minutes to showcase everything you've done in just these two weeks (please do not show us anything not directly related to this project). The goal is to show:
- *why* you did what you did
    - how you made sure your controller is safe (won't hit any cones or exceed the acceleration limits)
    - what things you optimized for & why you think your controller is the right choice given those priorities
- what you learned
- what problems you encountered and how you solved them

Whatever medium you think is best for this is fine; we're not particularly concerned about your graphic design or presentation skills beyond what is needed to communicate the core ideas here.

You will also submit a zip file of your finalized code.

## Resources
outside of [office hours](https://docs.google.com/spreadsheets/d/1ifnzajpgu3X9_jV493kc64A2R6CjR8UqbLQ9SasroNY/edit?gid=1214868707#gid=1214868707), here are a couple resources to give various bits of background on controls:

- The Matlab control videos provide a very good introduction to the idea of control and control theory. 
  - [control intro](https://youtu.be/lBC1nEq0_nk?si=m6OHT0HWrKCxY3qO)
  - [PID controller](https://www.youtube.com/watch?v=wkfEZmsQqiA)
  - [LQR controller](https://www.youtube.com/watch?v=E_RDCFOlJx4)
  - [intro to state space](https://www.youtube.com/watch?v=hpeKrMG-WP0)
  - [practical controls](https://www.youtube.com/watch?v=ApMz1-MK9IQ)
- Steve Brunton's [control bootcamp](https://youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m&si=FHHTSASSBPVFrT2r) is very good for getting the mathematical foundations of control theory. It's a very long playlist and I don't recommend watching all of it (because it gets way more advanced that you need for this), but if you watch videos 1-6 as well as 12 and 13, it should really help you understand any control literature you read.
- [Intro to Robot Motion: Theory, Algorithms, and Implementations](https://reid.xz.ax/swbible) is way too long and in depth, but appendix J is a good primer on linear control.
- [Purdue SigBots](https://wiki.purduesigbots.com/software/control-algorithms) has a nice wiki.
- [WPIlib](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/state-space/index.html) may be familiar to you and has a good controls primer.


## Deliverables/Completion Criteria

To comply with Blue & Gold guidelines, we must provide a set of minimum criteria which, if completed, guarantee that you can work on a technical project. These are those criteria.

Here, "controller" just refers to your entire solution, not just the control portion (ie, distinct planners or dynamics models or whatever count as distinct controllers).

- Implement at least 2 different controllers and compare the results to make quantitatively motivated decisions on the best option.
- Implement at least one controller which can complete a lap without exceeding the net acceleration limits or hitting any cones.
- Provide some proof of safety (with respect to the aforementioned acceleration and cone collision constraints) for your controller. Does not need to be fully valid (ie, can use approximations like linearization and convexification), but any such approximations must be well motivated. (really this criteria is just 'provide some justification for why your controller shouldn't violate any of the constraints')
- Understand the math behind all implemented controllers and be able to provide first principles (or at least quantitative data-driven) reasoning for why they chose the ones they did.
- Provide reasoning for how setpoints are chosen for the controller (ie, provide motivation for how planning was done)

