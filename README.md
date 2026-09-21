# Lab 5: SLAM and Pure Pursuit

## I. Learning Goals

- SLAM
- Localization with Particle Filter
- Pure Pursuit Algorithm

## II. Running slam_toolbox on the car

Follow the instructions in class to run `slam_toolbox` to make a map of Levine second floor. Save the map as `levine_2nd.pgm` and `levine_2nd.yaml`.

## III. Localization with Particle Filter

Follow the instructions in class to run `particle_filter` on the car using the new map you've made on Levine second floor.

## IV. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node. As per usual, test your algorithm first in the simulator before you test it on the car. When you're testing in the simulator, use the groud truth pose provided by the sim as the localization (`/ego_racecar/odom`). When you move to the car, use particle filter to provide localization.

As shown in the lecture, the curvature of the arc to track
can be calculated as:

$$\gamma=\frac{2|y|}{L^2}$$

In the [f1tenth_gym_ros](https://github.com/f1tenth/f1tenth_gym_ros/tree/dev-jazzy) simulator your node drives **two tracks**, and the autograder runs it on both. Set these in `config/sim.yaml` and your laptop run is the autograder's run:

| Track | `map_path` | `sx`, `sy`, `stheta` | Graded run |
| --- | --- | --- | --- |
| Levine | `'maps/levine_blocked'` | `-12.0`, `0.0`, `0.0` (the stock start pose) | three laps in a row, counter-clockwise |
| Spielberg | `'maps/Spielberg'` | `14.59`, `3.92`, `-2.877` | one lap, in the direction of its centerline |

Both maps come with a centerline, so the simulator counts your laps (`/ego_racecar/lap_count`, and a `completed lap N, last lap X s` line in the bridge log). Those lap times are exactly what the autograder reports and what the leaderboard ranks: a lap runs from the finish line back to it, the stretch from the start pose to the line is a run-up, so every lap is a flying lap.

**One launch file per track.** The autograder starts your code with the two launch files in `pure_pursuit/launch/`, and nothing else:

```bash
ros2 launch pure_pursuit levine_launch.py      # three laps of Levine (and the pose checks)
ros2 launch pure_pursuit spielberg_launch.py   # one lap of Spielberg
```

Each one is yours to edit: set `EXECUTABLE` to the node you wrote (`pure_pursuit_node.py` for Python, `pure_pursuit_node` for C++), give each track its own parameter values (lookahead, speeds), and start as many nodes as you like, in either language. Start your own nodes only: the autograder runs the simulator. As shipped, each file sets the string parameter `track` (`levine` or `spielberg`), which the skeleton node declares: load the matching waypoints. Without a track's launch file the autograder falls back to `ros2 run pure_pursuit <executable> --ros-args -p track:=<track>` with no parameter file, so tuned values must then be your node's defaults. Line F of your result tells you which way each run was started.

For Spielberg the simulator ships a centerline and an optimised raceline, `maps/Spielberg_centerline.csv` and `maps/Spielberg_raceline.csv`: you may use either, reshape them, or make your own. Mind that the raceline uses the whole track, walls included.

**Ship your waypoints with your package.** Put your CSV files in `pure_pursuit/waypoints/`; the skeleton's `CMakeLists.txt` installs that folder, and your node finds it with `get_package_share_directory('pure_pursuit')` (Python, `ament_index_python.packages`) or `ament_index_cpp::get_package_share_directory("pure_pursuit")` (C++). A path like `/home/you/sim_ws/...` only exists on your laptop: on the autograder your node would die at start-up.

## V. Logging Waypoints

There are several methods you can use to create waypoints for a specific map.

1. Recording a trajectory of joystick driven path. You can write a node that subscribe to the pose provided by the particle filter localization, and save the waypoints to a csv file. A similar script is provided [here](https://github.com/f1tenth/f1tenth_labs/blob/main/waypoint_logger/scripts/waypoint_logger.py). Note that this script is in ROS 1 and you'll have to write a ROS 2 node.

2. Find key points in the map (e.g. in the Levine loop, the four corner centers of the loop) and create a interpolated spline that goes through all four corners. You can use functions such as `scipy.interpolate.splprep` and `scipy.interpolate.splev`. You can find more documentaion on these [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splprep.html) and [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev).

Usually, you'll just save the waypoints as `.csv` files with columns such as `[x, y, theta, velocity, arc_length, curvature]`. With pure pursuit, the bare minimum is `[x, y]` positions of the waypoints. Another trick is that you can also smooth the waypoints if you decided to record it with the car. You can subsample the points you gathered and re-interpolate them with the `scipy` functions mentioned above to find better waypoints.

## VI. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

## VII. Deliverables and Submission

**This lab is done in teams**, the same teams as lab 4. Your team is already formed — you do not create one or invite anyone. **Every member of the team runs the same command**:

```bash
gh student accept RoboRacer-Class ese-6150 lab-5-pure-pursuit
```

Whoever runs it first creates the team's shared repository, `ese-6150-lab-5-pure-pursuit-group-<n>`; everyone else gets `Repository already exists` and the same URL. All of you push to that one repository, so **pull before you push**. One submission is the whole team's submission, and every member gets the same grade.

- **Deliverable 1**: Submit the map files in the `map` folder (`levine_2nd.pgm` and `levine_2nd.yaml`) that you've made using `slam_toolbox`.
- **Deliverable 2**: Commit your `pure_pursuit` package to your team's repository, waypoints included. Your commited code should run smoothly in simulation: three laps of Levine in a row and one lap of Spielberg, without touching a wall. The autograder watches both runs, and the leaderboard keeps your team's fastest lap on each track.
- **Deliverable 3**: Submit links to two videos in **`SUBMISSION.md`** (YouTube unlisted, or Google Drive shared as **"Anyone with the link can view"**): your pure pursuit in the simulator with your waypoints visualized, and the real car following waypoints in Levine hallway with the particle filter running, including a screen recording of rviz. You may use different parameters (i.e a separate launch file) for the on-car deployment.

### Submitting

You can commit and push your work as often as you need, but a plain push does **not** count as a submission. When your team is ready to submit, any one of you pushes a tag named `submission` — it counts for the whole team, so agree on the commit first:

```bash
# Make sure you've pulled before or switch branches
git push                            # your commits
git tag submission
git push origin submission          # this triggers the autograder
```

The autograder builds your package, checks your map, probes your controller and drives it around both tracks in the simulator, then posts your score as a **Release** on your repo (check the Releases page or the commit's status check a few minutes after you tag). To resubmit, move the tag to a new commit:

```bash
git tag -f submission
git push --force origin submission
```

The best scored `submission` push is counted as your team's final submission, and its grade is every member's grade for the lab. The two leaderboards are independent: each keeps your team's fastest clean lap on its track, and each track has its own launch file, so one submission carries a tuning for Levine and another for Spielberg. You will only have a SLAM map once you have been on the car; submit without it as often as you like, the leaderboards do not ask for it.

**The autograder finds your work by name.** Package `pure_pursuit`, launch files `levine_launch.py` and `spielberg_launch.py` (or, without them, an executable it can start with `ros2 run pure_pursuit <executable>`, the skeleton's `pure_pursuit_node`, reading the `track` parameter), taking its pose from `/ego_racecar/odom` and publishing `AckermannDriveStamped` on `/drive`. Otherwise, the autograder will not be able to grade your work and your submission may get the wrong grade.

## VIII: Grading Rubric
- Compilation: **10** Points (autograded)
- Running slam_toolbox and producing a map: **10** Points (autograded: `levine_2nd.yaml` and `levine_2nd.pgm` are in the repo and are a valid occupancy map; the TAs look at the map itself)
- Running particle_filter: **10** Points (TA-graded from the real-car video)
- Implementing pure pursuit: **50** Points
  - **20** Points (autograded without the simulator: your node is given the pose of a car standing to the left and to the right of your path, turned to the left and to the right, and half way round a corner, and must steer the right way each time — whatever your path and lookahead)
  - **20** Points (autograded in simulation: three counter-clockwise laps of `levine_blocked` in a row without touching a wall; a run that ends early earns partial credit for the fraction covered; the fastest of the three laps goes to the leaderboard)
  - **10** Points (autograded in simulation: one lap of `Spielberg` without touching a wall, with partial credit; the lap time goes to the Spielberg leaderboard)
- 2x Videos (TA-graded from the links in `SUBMISSION.md`):
  - In-sim **10** Points
  - On-Car **10** Points
