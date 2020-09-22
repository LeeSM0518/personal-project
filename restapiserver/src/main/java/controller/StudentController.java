package controller;

import dto.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import service.AttendService;
import service.CourseService;
import service.StudentService;

import java.util.List;

@RestController
@RequestMapping("/students")
public class StudentController {

  @Autowired
  private StudentService studentService;
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

  @PutMapping("/{studentId}/fingerprint")
  public void updateFingerprintByStudentId(@PathVariable("studentId") int studentId,
                                           @RequestBody UpdateFingerPrint dto) {
    studentService.updateFingerprintByStudentId(dto.getFingerprint(), studentId);
  }

  @GetMapping("/fingerprint")
  public List<GetStudentFingerprint> selectListForFingerprint() {
    return studentService.selectListForFingerprint();
  }

}
