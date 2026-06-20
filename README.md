# edubot_description

URDF/Xacro model and meshes for the [EduBot](https://github.com/vectoral-robotics) robot — by Vectoral.

## What it is

`edubot_description` defines what the robot *is* geometrically: the URDF/Xacro
model, joints, and the 3D meshes under `assets/`. It is consumed by the bringup
stack (for `robot_state_publisher`) and by RViz, and can also be used
standalone to inspect the model on a development machine.

## Installation

Requires ROS 2 Humble.

```bash
cd ~/ros2_ws/src
git clone https://github.com/vectoral-robotics/edubot_description.git
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select edubot_description
source install/setup.bash
```

## Usage

View the robot model in RViz (no hardware needed):

```bash
ros2 launch edubot_description view_model.launch.py
```

The model files live in `urdf/` and the meshes in `assets/`. Other packages
reference this package via `FindPackageShare('edubot_description')`.

## Contributing

- Work on a short-lived feature branch and open a pull request against `main`
  (which is protected); changes land via PR review.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org)
  (`feat:`, `fix:`, `docs:`, …). See `CLAUDE.md` for repo conventions.

## License

PolyForm Perimeter 1.0.0 (source-available) — see [LICENSE](LICENSE).
