package service;

import dto.Course;
import dto.GetProfessorCoursesResponse;
import error.CourseNotFoundException;
import mapper.CourseMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class CourseService {

  @Autowired
  private CourseMapper mapper;

  public List<Course> selectListByStudentId(int id) {
    List<Course> list = mapper.selectListByStudentId(id);
    if (list == null || list.size() == 0)
      throw new CourseNotFoundException();
    return list;
  }

  public List<GetProfessorCoursesResponse> selectListByProfessorId(int id) {
    List<Course> list = mapper.selectListByProfessorId(id);
    if (list == null || list.size() == 0)
      throw new CourseNotFoundException();
    return list.stream().map(GetProfessorCoursesResponse::new).collect(Collectors.toList());
  }

}
