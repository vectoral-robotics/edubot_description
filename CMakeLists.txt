cmake_minimum_required(VERSION 3.10)
project(omnibot_description)

find_package(ament_cmake REQUIRED)

# Install robot description files
install(
  DIRECTORY urdf assets launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()


