package service;

import dto.*;
import error.AttendNotFoundException;
import mapper.AttendMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class AttendService {

  @Autowired
  private AttendMapper mapper;

  public List<GetAttend> selectListByStudentIdAndCourseId(int studentId, int courseId) {
    List<GetAttend> list = mapper.selectListByStudentIdAndCourseId(studentId, courseId)
        .stream()
        .map(element -> new GetAttend(element.getId(), element.getWeek(),
            element.getAttendance() == 1 ? "출석" :
                (element.getAttendance() != 0 ? "지각" : "결석"))).collect(Collectors.toList());
    if (list.size() == 0)
      throw new AttendNotFoundException();
    return list;
  }

  public List<Attend> selectListForProfessorByStudentIdAndCourseId(int studentId, int courseId) {
    List<Attend> list = mapper.selectListByStudentIdAndCourseId(studentId, courseId);
    if (list.size() == 0)
      throw new AttendNotFoundException();
    return list;
  }

  public List<GetAttendForProfessor> selectStudentAndAttendByStudentIdAndCourseId(int courseId) {
    List<GetAttendForProfessor> list = mapper.selectStudentAndAttendByStudentIdAndCourseId(courseId)
        .stream()
        .map(el -> new GetAttendForProfessor(el.getId(), el.getStudentCode(), el.getName(),
            el.getSum() + "/" + (double) el.getCount()))
        .collect(Collectors.toList());
    if (list.size() == 0)
      throw new AttendNotFoundException();
    return list;
  }

  public void insertAttend(int studentId, int courseId, AttendPostRequest request) {
    mapper.insertAttend(studentId, courseId, request.getWeek(), request.getAttendance());
  }

  public void updateAttend(Attend attend) {
    mapper.putAttend(attend);
  }

}
