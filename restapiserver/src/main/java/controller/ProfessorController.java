package controller;

import dto.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import service.AttendService;
import service.CourseService;
import service.SeatService;
import service.StudentService;

import java.util.List;

@RestController
@RequestMapping("/professors")
public class ProfessorController {

  @Autowired
  private CourseService courseService;
  @Autowired
  private SeatService seatService;
  @Autowired
  private StudentService studentService;
  @Autowired
  private AttendService attendService;

  @GetMapping("/{id}/courses")
  public List<GetProfessorCoursesResponse> selectCoursesByProfessorId(@PathVariable int id) {
    return courseService.selectListByProfessorId(id);
  }

  @GetMapping("/{professorId}/courses/{courseId}/seats")
  public List<Seat> selectSeatListByCourseId(@PathVariable("courseId") int id) {
    return seatService.selectListByCourseId(id);
  }

  @PutMapping("/{professorId}/courses/{courseId}/seats")
  public void updateAllSeatByCourseId(@PathVariable("courseId") int id) {
    seatService.updateByCourseId(id);
  }

  @GetMapping("/{professorId}/courses/{courseId}/students")
  public List<GetAttendForProfessor> selectStudentsByCourseId(@PathVariable("courseId") int id) {
    return attendService.selectStudentAndAttendByStudentIdAndCourseId(id);
  }

  @GetMapping("/{professorId}/courses/{courseId}/students/{studentId}/attendances")
  public List<Attend> selectAttendByStudentIdAndProfessorId(@PathVariable("studentId") int studentId,
                                                            @PathVariable("courseId") int courseId) {
    return attendService.selectListForProfessorByStudentIdAndCourseId(studentId, courseId);
  }

  @PutMapping("/{professorId}/courses/{courseId}/students/{studentId}/attendances/{attendanceId}")
  public void updateAttendById(@RequestBody Attend attend) {
    attendService.updateAttend(attend);
  }

}
