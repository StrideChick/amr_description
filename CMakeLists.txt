cmake_minimum_required(VERSION 3.8) 
project(amr_description) 

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang") 
  add_compile_options(-Wall -Wextra -Wpedantic) 
endif() 

# 依存関係を検索
find_package(ament_cmake REQUIRED) 
find_package (urdf REQUIRED) 
find_package(xacro REQUIRED) 

if(BUILD_TESTING) 
  find_package(ament_lint_auto REQUIRED) 
  ament_lint_auto_find_test_dependencies() 
endif() 

install( 
  DIRECTORY 
  rviz 
  launch 
  amr 
  DESTINATION share/${PROJECT_NAME}/ 
) 

ament_package()