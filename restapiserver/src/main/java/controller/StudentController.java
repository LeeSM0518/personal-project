package controller;

import dto.Attend;
import dto.AttendPostRequest;
import dto.Course;
import dto.GetAttend;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import service.AttendService;
import service.CourseService;

import java.util.List;

@RestController
@RequestMapping("/students")
public class StudentController {

  @Autowired
  private CourseService courseService;
  @Autowired
  private AttendService attendService;

  @GetMapping("/{id}/courses")
  public List<Course> selectCourseListByStudentId(@PathVariable int id) {
    return courseService.selectListByStudentId(id);
  }

  @GetMapping("/{studentId}/courses/{courseId}/attendances")
  public List<GetAttend> selectAttendListByCourseId(@PathVariable("studentId") int studentId,
                                                    @PathVariable("courseId") int courseId) {
    return attendService.selectListByStudentIdAndCourseId(studentId, courseId);
  }

  @PostMapping("/{studentId}/courses/{courseId}/attendances")
  public void insertAttend(@PathVariable("studentId") int studentId,
                           @PathVariable("courseId") int courseId,
                           @RequestBody AttendPostRequest request) {
    attendService.insertAttend(studentId, courseId, request);
  }

}
