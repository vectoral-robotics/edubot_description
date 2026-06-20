# edubot_description — Claude guidelines

ROS2 package holding the EduBot URDF/xacro model and the mesh assets under
`assets/`. Part of the EduBot ROS2 stack; also used standalone for
visualization and by `edubot_viz`.

These guidelines will grow over time. For now the most important rule:

## Commits

All commits MUST follow the [Conventional Commits](https://www.conventionalcommits.org) spec.

Format:

    <type>(<optional scope>): <short summary>

Common types: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

- Imperative mood ("add", not "added").
- Summary under ~72 characters, lower case, no trailing period.
- Scope is optional and names the affected area.

Example:

    fix(urdf): correct wheel joint origin
